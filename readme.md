# 🏦 End-to-End Fraud Detection System on Azure

## 📌 Project Overview
This project focuses on detecting fraudulent financial transactions and identifying hidden anomalies within a massive financial dataset. The primary goal is to uncover illicit activities, enabling financial institutions to take proactive security measures and minimize monetary losses.

The project consists of four main phases: **Cloud Data Engineering** to build an automated, scalable data ingestion pipeline on Microsoft Azure, **Exploratory Data Analysis (EDA)** to understand the data and uncover key fraud patterns,  **Advanced Anomaly Detection** to build predictive solutions focused on cost-sensitive business optimization and **Model Deployment** 

## 📊 Dataset Information
The data used in this project comes from Synthetic Financial Datasets For Fraud Detection dataset  available on Kaggle.
* **Source:** https://www.kaggle.com/datasets/ealaxi/paysim1
* **Records:** 6362620
* **Features:** 10 columns (9 features + 1 target variable)
* **Class imbalance:** isFraud = 1: 8213 (~ 0,13 %) | isFraud = 0: 6354407 (~ 99,87 %)
> Column descriptions sourced from the official Kaggle dataset page.


## 🛠️ Tech Stack & Tools
* **Languages:** Python, SQL
* **Cloud & Data Engineering:** Azure Data Factory (ADF), Azure Data Lake Storage Gen2, Azure SQL Database
* **Data Manipulation & Analysis:** `pandas`
* **Data Visualization:** `seaborn`, `matplotlib`
* **Machine Learning:** `scikit-learn`, `lightgbm`


## 📂 Project Architecture
The project follows a Medallion architecture (Bronze → Silver → Gold) to ensure structured and scalable data processing.
### 1️⃣ Phase 1: Cloud Data Engineering

#### 🥉 Bronze Layer – Data Ingestion
Currently, the raw data ingestion pipeline is implemented.
##### Architecture
1. **Data Lake:** Stored securely in **Azure Data Lake Storage Gen2** (`raw-data` container).
2. **Orchestration:** **Azure Data Factory (ADF)** pipeline created to dynamically read the CSV and auto-create the schema.
3. **Database:** Data loaded into **Azure SQL Database** (Serverless tier for cost optimization).

##### Data Ingestion Proof
**1. Raw Data in Azure Data Lake:**
![Data Lake](images/01_datalake_raw_data.png)

**2. ADF Pipeline Success:**
![ADF Pipeline](images/02_adf_pipeline_success.png)

##### Data Validation (SQL) 
Initial data profiling:
- Total records: 6362620
- Fraud cases: 8213 (~ 0,13 %)
- Non-fraud cases: 6354407 (~ 99,87 %)
##### SQL Validation Script
All data profiling queries are stored in:
File `01_data_profiling.sql`

File: `sql/01_data_profiling.sql`

This script includes:
- Row count verification
- Schema inspection
- Target variable distribution (class imbalance)
- Basic data preview

#### 🥈 Silver Layer – Data Filtering  & Feature Engineering
In this stage, the raw data was transformed into a model-ready format using SQL Views. This approach ensures resource optimization (no data duplication) and dynamic updates.

##### Key Transformations:
1. **Data Filtering:** Reduced the dataset from 6.3M to ~2.77M records by focusing exclusively on `TRANSFER` and `CASH_OUT` transaction types, where the majority of fraud cases occur.
2. **Feature Engineering:** Created two new analytical columns to capture mathematical discrepancies in account balances:
    - `errorBalanceOrig`: Calculates the difference between the intended and actual balance of the sender.
    - `errorBalanceDest`: Calculates the difference between the intended and actual balance of the receiver.

##### SQL Transformation Script
File `sql/02_feature_engineering.sql`

### 2️⃣ Phase 2: Exploratory Data Analysis & 🥇 Gold Layer Preparation
Building upon the **Silver Layer** generated via Azure SQL, this phase utilizes Python (`pandas`, `seaborn`) to perform deep EDA and construct the **Gold Layer** — a highly enriched, model-ready dataset.

**1. Data Cleaning & Validation:**
* Verified and corrected column data types for memory optimization.
* Conducted data quality checks (missing values and duplicates validation) to ensure data integrity.

**2. Exploratory Data Analysis:**
* **Univariate & Bivariate Analysis:** Visualized individual feature distributions and their relationships with the `isFraud` target. 
* **Correlation Analysis:** Evaluated linear relationships between numerical variables to identify potential multi-collinearity and predictive power.

**3. Python-Based Feature Engineering (Gold Layer Enablers):**
To finalize the Gold Layer for machine learning, additional predictive features were engineered to capture behavioral and temporal patterns:
* **Temporal Features:** Extracted `hour` and `day_of_week` from the continuous `step` variable to model the 24/7 nature of automated fraud.
* **`accountDrained` Flag:** A binary indicator (`1` or `0`) capturing transactions that completely emptied the sender's account (`newbalanceOrig == 0` and `amount > 0`).
* **`isHighAmount` Flag:** A dynamic binary flag marking transactions that exceed the 95th percentile of transfer amounts, effectively isolating high-risk monetary movements.

### 3️⃣ Phase 3: Advanced Anomaly Detection (In Progress)
*Currently training predictive machine learning models (Logistic Regression, Isolation Forest, LightGBM) to detect anomalies based on the engineered Gold Layer...*
### 4️⃣ Phase 4: Model Deployment (In Progress)
*Planning to containerize the solution and build an interactive web interface for fraud analysts...*
## 📈 Results (In Progress)

## 🔍 Key Findings (In Progress)

## 🚀 How to Run (Local Setup) (In Progress)
