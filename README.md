# Car Price Prediction 🚗📊

This repository contains a Data Science project focused on predicting car prices using machine learning. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model building, and evaluation.

## Project Overview 🌟

Accurate car price prediction helps buyers and sellers in the automotive market. This project leverages historical sales data to predict car prices based on features like make, model, year, mileage, and more.

## Table of Contents 📑

- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Modeling Approach](#modeling-approach)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Dataset 📊

The dataset includes:
- Name of Car
- Year of Manufacture
- Km Driven
- Fuel Type
- Seller Type
- Transmission
- Number of Owners
- Mileage (km/ltr/kg)
- Engine CC
- Selling Price (Target Variable)

## Technologies Used 🛠️

- **Python**
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost/LightGBM
- **Frameworks:** Falsk, Bootstrap-5

## Project Structure 🗂️

```
├── data
│   └── Cardetails.csv
├── model
│   └── Model.pkl
├── notebook
│   └── research.ipynb
├── static
│   ├── script.js
│   ├── style.css
│   ├── bootstrap.min.css.map
│   ├── logo.ico
│   ├── jquery.min.js
│   └── Others
├── templates
│   └── base.html
├── .gitignore
├── LICENSE
├── app.py
├── notebookFunction.py
├── requirements.txt
└── research.py
```

## Setup Instructions ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/Prathmeshpawar21/DS-Used-Car-Price-Prediction.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
    OR

3. Create and activate a virtual environment using Anaconda:
   ```bash
   conda create -n venv python=3.10 -y
   conda activate venv 
   ```


3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Modeling Approach 📈

1. **Data Preprocessing:** Handle missing values, encode categories, scale features.
2. **EDA:** Analyze trends, distributions, and correlations.
3. **Modeling:** Test models (
Linear Regression, DecisionTreeRegression,  KNeighborsRegressor, RandomForestRegressor, GradientBoostingRegressor, 
SVR),Tune hyperparameters.
4. **Evaluation:** Metrics (MAE, R-squared), visualizations (residual plots, feature importance).

## Results 🏆

- Best Model: KNeighborsRegressor 
- Performance:
  - Train: 86.77599637074338 %
  - Test: 85.2558171403603 %

## Future Improvements 🚀

- Add more features (e.g., macroeconomic factors, car condition).
- Experiment with deep learning models.

## Contributing 🤝

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
