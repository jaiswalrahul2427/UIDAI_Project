📊 Aadhaar Demographic Data Analysis (UIDAI)
📌 Project Overview

This project focuses on the analysis of UIDAI Aadhaar demographic data to uncover meaningful state-wise and age-wise patterns that can support informed decision-making and system-level improvements. The raw Aadhaar demographic datasets were fragmented and inconsistent, making direct analysis unreliable. This project builds a complete data pipeline to clean, standardize, analyze, and visualize Aadhaar demographic records.

🎯 Objectives

Integrate multiple UIDAI Aadhaar demographic CSV files into a single dataset

Clean and standardize inconsistent geographical data

Analyse state-wise distribution of Aadhaar demographic records

Compare age-group participation (5–17 years vs 17+ years) across states

Visualize patterns, disparities, and potential coverage gaps

📂 Dataset

Source: UIDAI Aadhaar Demographic Enrolment Dataset

Example files used:

api_data_aadhar_demographic_0_500000.csv

api_data_aadhar_demographic_500000_1000000.csv

api_data_aadhar_demographic_1500000_2000000.csv

api_data_aadhar_demographic_2000000_2071700.csv

Key columns:

state – State / Union Territory

demo_age_5_17 – Aadhaar demographic records (Age 5–17)

demo_age_17_ – Aadhaar demographic records (Age 17+)

🛠 Tools & Technologies

Python

Pandas, NumPy

Matplotlib

Jupyter Notebook / VS Code

⚙ Methodology

Merged multiple UIDAI Aadhaar demographic datasets

Standardized state names and removed noisy values

Validated data using the official list of Indian states and UTs

Aggregated records for state-wise and age-wise analysis

Generated visualizations to extract and communicate insights

📈 Analysis Performed

Univariate analysis: State-wise Aadhaar demographic distribution

Bivariate analysis: State × Age group comparison (5–17 vs 17+)

Detection of regional disparities and demographic imbalances

📊 Visualizations

Bar chart showing state-wise Aadhaar demographic distribution

Grouped bar chart comparing age groups across states

(All graphs are generated from real UIDAI Aadhaar demographic data using Matplotlib.)

🔍 Key Insights

Significant regional variation exists in Aadhaar demographic records

Adult (17+) enrolments dominate across all states

Youth (5–17) participation varies considerably by region

Highlights states that may require targeted enrollment strategies

🌍 Impact & Applicability

Supports demographic monitoring and administrative planning

Helps identify state-level coverage gaps

Can assist UIDAI and policymakers in targeted digital inclusion initiatives

Forms a base for dashboards, reporting systems, and predictive analytics

▶ How to Run the Project
pip install pandas numpy matplotlib
python main.py


Ensure all Aadhaar demographic CSV files are placed in the project directory.

🌍Some Graph

C:\Users\91945\Desktop\UIDAI project\State-wise Aadhar Count.png
C:\Users\91945\Desktop\UIDAI project\State-wise Aadhar Distribution by Age Group.png



