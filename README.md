# 🏡 Gurgaon Real Estate

A multi-page **Streamlit** web app for exploring, analyzing, and predicting residential property prices in Gurgaon. Built end-to-end — from a trained ML pricing pipeline to interactive geographic analytics and a content-based apartment recommender.

**🔗 Live app:** [gurgaonreal-estate.streamlit.app](https://gurgaonreal-estate.streamlit.app)

---

## ✨ Features

### 💰 Price Predictor
Estimate the price of a property by entering details like property type, sector, number of bedrooms/bathrooms, balconies, built-up area, furnishing status, and more. Powered by a trained `scikit-learn` regression pipeline (with categorical encoding via `category_encoders`).

### 📊 Analytics Dashboard
Explore Gurgaon's real estate market visually:
- **Geographic price map** — sector-wise average price per sqft plotted on an interactive map (Plotly + Mapbox)
- **Word clouds** of frequently mentioned property features
- **Distribution plots** comparing prices across flats vs. independent houses
- Additional visual breakdowns using `matplotlib` and `seaborn`

### 🏘️ Apartment Recommender
Get similar apartment recommendations based on a chosen property, using a **cosine-similarity** based content recommendation engine built on location, pricing, and feature-similarity matrices.

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

**2. Create a virtual environment (recommended)**
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

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| App Framework | [Streamlit](https://streamlit.io/) |
| Data Handling | pandas, numpy |
| Machine Learning | scikit-learn, category_encoders |
| Visualization | Plotly, Matplotlib, Seaborn, WordCloud |
| Statistics | statsmodels |

---

## 📌 Notes

- The prediction pipeline (`pipeline.pkl.gz`) and datasets are pre-trained/precomputed artifacts — no training step is needed to run the app.
- If you retrain the model, make sure to keep `requirements.txt` versions in sync with the environment used for training, since scikit-learn and category_encoders pipelines are version-sensitive when unpickled.

---

## 📄 License

This project currently has no license file. Add one (e.g., MIT) if you'd like to make reuse terms explicit.

---

## 🙋‍♂️ Author

**[Optimus0205](https://github.com/Optimus0205)**
