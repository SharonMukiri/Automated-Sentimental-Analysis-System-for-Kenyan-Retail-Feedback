# Sentiment Analysis — Streamlit demo

This repository contains utilities for preprocessing Swahili/English code-switched text and visualization helpers. `app.py` is a minimal Streamlit app that demonstrates preprocessing and simple heuristic sentiment labeling.

Quick start (locally):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Deploy to Streamlit Cloud:

- Ensure `requirements.txt` and `app.py` are at the repo root.
- Create (or connect) a Streamlit Cloud app and point it to this repository. Streamlit Cloud will install dependencies and run `streamlit run app.py` by default.

Notes:
- `app.py` uses a simple heuristic for sentiment when no trained model is available. Replace this with your trained model from `Models/` if you have one (e.g., load with `joblib`).
- Ensure `Data/swahili.csv` exists or upload a CSV via the app UI when running.

**Security / Sensitive data**

- Never commit secrets (API keys, private keys, passwords) into the repository. Keep them in environment variables or use Streamlit Cloud's secrets management.
- This repo now includes a `.gitignore` that excludes virtual environments, `.env` files, and the `.streamlit/` folder. Review it and add any additional paths you don't want tracked (for example large `Data/` files or model binaries).
- To add secrets for Streamlit Cloud, use the app's Secrets Manager in the Streamlit Cloud UI — do not store `secrets.toml` in source control.

If you'd like, I can help scan the repository for likely secrets and prepare a cleaned commit before pushing to GitHub.
