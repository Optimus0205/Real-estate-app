<div align="center">

# 🏡 Gurgaon Real Estate

### Predict prices. Explore the market. Discover your next home.

A multi-page **Streamlit** web app that combines machine learning, interactive analytics, and a content-based recommendation engine to make sense of Gurgaon's residential real estate market.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://gurgaonreal-estate.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**[🚀 Try the Live App](https://gurgaonreal-estate.streamlit.app)**

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#️-project-structure)
- [Getting Started](#-getting-started-locally)
- [Tech Stack](#️-tech-stack)
- [Notes](#-notes)
- [License](#-license)
- [Author](#️-author)

---

## ✨ Features

<table>
<tr>
<td width="33%" valign="top">

### 💰 Price Predictor
Get an instant price estimate for a property by entering details like property type, sector, bedrooms, bathrooms, balconies, built-up area, and furnishing status — powered by a trained `scikit-learn` regression pipeline with categorical encoding via `category_encoders`.

</td>
<td width="33%" valign="top">

### 📊 Analytics Dashboard
Explore the market visually:
- 🗺️ Interactive **sector-wise price map**
- ☁️ **Word clouds** of top property features
- 📈 **Distribution plots** comparing flats vs. independent houses

</td>
<td width="33%" valign="top">

### 🏘️ Apartment Recommender
Discover similar apartments using a **cosine-similarity** based content recommendation engine built on location, pricing, and feature-similarity matrices.

</td>
</tr>
</table>

---

## 🗂️ Project Structure

```
Real-estate-app/
├── Home.py                          # Landing page
├── pages/
│   ├── 1_Price Predictor.py         # ML-based price prediction
│   ├── 2_Analysis App.py            # Visual analytics dashboard
│   └── 3_Recommended Appartments.py # Apartment recommender
├── Datasets/
│   ├── data_viz1.csv                # Data for analytics dashboard
│   ├── feature_text.pkl             # Word cloud source text
│   ├── location_distance.pkl        # Location similarity data
│   └── cosine_sim1/2/3.pkl          # Precomputed similarity matrices
├── df.pkl                           # Cleaned dataset used by the predictor
├── pipeline.pkl.gz                  # Trained price-prediction pipeline (compressed)
└── requirements.txt                 # Python dependencies
```

---

## 🚀 Getting Started Locally

**1. Clone the repository**
```bash
git clone https://github.com/Optimus0205/Real-estate-app.git
cd Real-estate-app
```

**2. Create a virtual environment** *(recommended)*
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run Home.py
```

The app will open automatically at `http://localhost:8501` 🎉

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|:---|:---|
| **App Framework** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) |
| **Data Handling** | ![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![numpy](https://img.shields.io/badge/-numpy-013243?style=flat-square&logo=numpy&logoColor=white) |
| **Machine Learning** | ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) `category_encoders` |
| **Visualization** | ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) `Matplotlib` `Seaborn` `WordCloud` |
| **Statistics** | `statsmodels` |

</div>

---

## 📌 Notes

> **Pre-trained artifacts**: The prediction pipeline (`pipeline.pkl.gz`) and datasets are pre-trained/precomputed — no training step is needed to run the app.

> **Version sensitivity**: If you retrain the model, keep `requirements.txt` versions in sync with the training environment. scikit-learn and category_encoders pipelines are version-sensitive when unpickled, and mismatches can break the deployed app.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## 🙋‍♂️ Author

**[Optimus0205](https://github.com/Optimus0205)**

⭐ If you found this project useful, consider giving it a star!

</div>
category_encoders pipelines are version-sensitive when unpickled.

---

## 📄 License

This project currently has no license file. Add one (e.g., MIT) if you'd like to make reuse terms explicit.

---

## 🙋‍♂️ Author

**[Optimus0205](https://github.com/Optimus0205)**
