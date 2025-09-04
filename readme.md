# 📊 Telecom Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Machine Learning](https://img.shields.io/badge/ML-DecisionTree%20%7C%20XGBoost-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Project Overview
Customer churn is one of the most critical problems in the telecom industry.  
This project aims to **predict customer churn** using machine learning and provide **actionable business insights** for customer retention.

The workflow covers:
- Data exploration & visualization  
- Data cleaning & preprocessing  
- Model building (Decision Tree & XGBoost)  
- Evaluation (Accuracy, F1, ROC AUC, Cross-Validation)  
- Feature importance & insights  
- Saving the best model for future use  

---

## 📂 Dataset
- **Source:** IBM Sample Dataset (Telco Customer Churn)  
- **File used:** `Telco_customer_churn.xlsx`  
- **Target variable:** `Churn` (`Yes` → 1, `No` → 0)  
- **Size:** ~7,000 customers, 20+ features  

**Features include:**
- **Demographics:** Gender, SeniorCitizen, Partner, Dependents  
- **Services:** InternetService, Streaming, OnlineSecurity, TechSupport  
- **Contracts:** Contract type, Payment method, Paperless billing  
- **Financials:** Tenure, MonthlyCharges, TotalCharges  

---

## ⚙️ Methodology
### 1. Data Cleaning & Preprocessing
- Dropped identifiers and leakage columns (CustomerID, Churn Reason, etc.)  
- Converted `TotalCharges` to numeric  
- Handled missing values with imputation (median for numeric, most_frequent for categorical)  
- Scaled numeric features  
- One-hot encoded categorical features  

### 2. Exploratory Data Analysis
- Visualized churn distribution (imbalanced dataset: ~26% churners)  
- Explored key drivers: Tenure, Contract type, Monthly charges  
- Correlation heatmap for numeric variables  

### 3. Model Building
- **Decision Tree (baseline):** simple, interpretable  
- **XGBoost (advanced):** robust gradient boosting model  

Both models were wrapped inside **sklearn Pipelines** for clean preprocessing + modeling.  

### 4. Evaluation
Metrics used:
- Accuracy  
- Precision, Recall, F1-score  
- ROC AUC  
- 5-fold Cross-Validation (for XGBoost)  

### 5. Feature Importance
- Extracted top churn drivers from XGBoost  
- Visualized the top 15 most important features  

---

## 🏆 Results
| Model            | Accuracy | F1 Score | ROC AUC |
|------------------|----------|----------|---------|
| Decision Tree    | ~0.73    | ~0.62    | ~0.74   |
| **XGBoost**      | **~0.82**| **~0.71**| **~0.85**|

- **XGBoost outperformed the Decision Tree** across all metrics.  
- **Top churn drivers** (example): Contract type, Tenure, MonthlyCharges, PaymentMethod, InternetService.  

---

## 📊 Visualizations
Here are some key visuals from the analysis:  

- **Churn Distribution**  
  ![Churn Distribution](plots/churn_distribution.png)

- **Feature Importance**  
  ![Feature Importance](plots/feature_importance.png)

- **ROC Curve**  
  ![ROC Curve](plots/roc_curve.png)

---

## 💡 Business Insights
1. **Contract Type matters**: Month-to-Month customers churn the most.  
   → Offer discounts or loyalty benefits for longer-term contracts.  
2. **Early Tenure churn risk**: Customers in their first year are more likely to leave.  
   → Focus on onboarding experience and engagement campaigns.  
3. **High Monthly Charges**: Customers with higher bills show higher churn.  
   → Consider competitive pricing or bundling offers.  

---

## 🚀 Tech Stack
- **Python 3.9+**  
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`,  
  `scikit-learn`, `xgboost`, `joblib`  

---

## 📦 How to Run

```bash
# 1. Clone this repo
git clone https://github.com/VedikaSankhe/Telecom-Customer-Churn.git
cd Telecom-Customer-Churn

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the notebook
jupyter notebook notebooks/customerchurn.ipynb

