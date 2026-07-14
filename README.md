# Multilingual Sentiment Analysis for Kenyan Retail Feedback

A machine learning system for classifying customer sentiment in **English, Swahili, and Sheng**, built to reflect how Kenyan consumers actually write retail feedback online, rather than assuming a single-language input.

## Overview

Most sentiment analysis tools are trained and tuned for standard English, which makes them unreliable for markets like Kenya where feedback is frequently written in code-switched language, blending English, Swahili, and Sheng within the same sentence or review. This project addresses that gap by building a sentiment classifier specifically trained and evaluated on multilingual, code-switched retail feedback.

## Key Features

- **Multilingual support** — handles English, Swahili, and Sheng, including code-mixed text
- **Dual-model approach** — implements and compares Naïve Bayes and Support Vector Machine (SVM) classifiers
- **Retail-focused dataset** — trained on customer feedback representative of the Kenyan e-commerce/retail context
- **86.3% accuracy** achieved on the evaluation set

## Motivation
Kenyan businesses increasingly rely on online customer feedback to guide decisions, but off-the-shelf NLP tools often misclassify sentiment when text switches between languages mid-sentence, a common feature of everyday Kenyan communication. This project explores whether a model trained specifically on this kind of text can produce more reliable results than general-purpose sentiment tools.

## Tech Stack
- Python
- scikit-learn (Naïve Bayes, SVM)
- NLP preprocessing for code-mixed/multilingual text

## Future Improvements
- Expand training data across more retail categories
- Explore transformer-based models (e.g. multilingual BERT) for comparison
- Deploy as an API for real-time feedback classification

---

*This project was developed as a final-year capstone at JKUAT (Jomo Kenyatta University of Agriculture and Technology).*
