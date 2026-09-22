import streamlit as st
import pandas as pd
import os
from Utils.preprocessing import TextPreprocessor, load_and_prepare_data
from Utils.visualization import create_word_cloud, create_sentiment_bar_chart, create_sentiment_pie_chart


st.set_page_config(page_title="Sentiment Analysis", layout="wide")


def load_dataset(path):
	if not os.path.exists(path):
		return None
	try:
		return load_and_prepare_data(path)
	except Exception:
		try:
			return pd.read_csv(path)
		except Exception:
			return None


def simple_heuristic_sentiment(text):
	# Minimal fallback sentiment heuristic (for demo only)
	pos_words = {"nzuri", "safi", "furaha", "awesome", "good", "great", "love"}
	neg_words = {"mbaya", "takataka", "mbovu", "bad", "hate", "terrible", "sad"}

	words = set(str(text).lower().split())
	score = len(words & pos_words) - len(words & neg_words)
	if score > 0:
		return "positive"
	if score < 0:
		return "negative"
	return "neutral"


def main():
	st.title("Sentiment Analysis — Streamlit Demo")

	st.sidebar.header("Data")
	default_path = os.path.join("Data", "swahili.csv")

	uploaded = st.sidebar.file_uploader("Upload CSV (must contain a text column)", type=["csv"]) 
	use_sample = False
	if uploaded is not None:
		df = pd.read_csv(uploaded)
	else:
		df = load_dataset(default_path)
		if df is not None:
			use_sample = True

	if df is None:
		st.warning("No dataset found. Upload a CSV or add `Data/swahili.csv`.")
		st.info("You can still try the preprocessor on custom text below.")

	st.sidebar.markdown("---")
	st.sidebar.header("Preprocessing")
	run_preproc = st.sidebar.button("Run preprocessing")

	preprocessor = TextPreprocessor()

	if df is not None and run_preproc:
		# Try to detect a text column
		text_cols = [c for c in df.columns if df[c].dtype == object][:2]
		if not text_cols:
			st.error("No text-like column found in the dataset.")
		else:
			text_col = st.sidebar.selectbox("Text column", text_cols, index=0)
			st.write(f"Using text column: {text_col}")

			df["processed_text"] = df[text_col].fillna("").astype(str).apply(preprocessor.preprocess)

			st.subheader("Sample processed texts")
			st.dataframe(df[[text_col, "processed_text"]].head(50))

			# Add simple heuristic sentiment
			df["sentiment"] = df["processed_text"].apply(simple_heuristic_sentiment)

			st.subheader("Sentiment counts")
			counts = df["sentiment"].value_counts().to_dict()
			st.plotly_chart(create_sentiment_pie_chart(counts), use_container_width=True)
			st.plotly_chart(create_sentiment_bar_chart(counts), use_container_width=True)

			# Word cloud
			texts = df["processed_text"].tolist()
			wc_fig = create_word_cloud(texts)
			if wc_fig is not None:
				st.subheader("Word Cloud")
				st.pyplot(wc_fig)

			csv = df.to_csv(index=False).encode("utf-8")
			st.download_button("Download processed CSV", data=csv, file_name="processed.csv")

	st.markdown("---")
	st.subheader("Quick preprocessor demo")
	sample_input = st.text_area("Enter text to preprocess", value="Nataka bidhaa nzuri lakini huduma ni mbaya")
	if st.button("Preprocess text"):
		processed = preprocessor.preprocess(sample_input)
		st.write("Processed:", processed)
		st.write("Heuristic sentiment:", simple_heuristic_sentiment(processed))


if __name__ == "__main__":
	main()

