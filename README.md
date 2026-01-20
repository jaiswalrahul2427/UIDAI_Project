# UIDAI Aadhaar Demographic Data Analysis

## 📌 Project Overview

This project focuses on analysing UIDAI Aadhaar demographic data to identify meaningful geographical and age-based patterns. The objective is to transform fragmented and inconsistent raw Aadhaar demographic datasets into a clean, standardized, and analysis‑ready format, and to extract insights that can support informed decision‑making and system improvements.

---

## 🎯 Problem Statement

Raw UIDAI Aadhaar demographic data is distributed across multiple files and contains inconsistencies such as spelling variations in state names, city‑level entries, and invalid values. These issues limit the ability to conduct reliable demographic and regional analysis.

This project solves this problem by building a reproducible data cleaning and analysis pipeline and uncovering state‑wise and age‑wise Aadhaar demographic patterns.

---

## 📂 Dataset Used

UIDAI Aadhaar Demographic Enrolment Dataset (CSV files)

Example files:

* api_data_aadhar_1.csv
* api_data_aadhar_2.csv
* api_data_aadhar_3.csv
* api_data_aadhar_4.csv

Key columns used:

* `state`
* `demo_age_5_17`
* `demo_age_17_`

Final dataset:

* 2M+ records
* 36 official Indian states and union territories

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib

---

## ⚙️ Methodology

1. Merged multiple Aadhaar demographic CSV files into one dataset.
2. Standardized and cleaned the `state` column.
3. Corrected spelling variations and removed invalid entries.
4. Filtered records using the official list of Indian states and UTs.
5. Aggregated demographic features using group‑by operations.
6. Performed univariate and bivariate analysis.
7. Created visualizations to interpret patterns and trends.

---

## 📊 Analysis Performed

* State‑wise Aadhaar demographic distribution
* State‑wise comparison of age groups (5–17 vs 17+)
* Detection of regional disparities and demographic imbalance

Visual outputs:

* Bar chart: State‑wise Aadhaar count
* Grouped bar chart: State‑wise age group comparison

---

## 🔍 Key Insights

* Significant regional variation exists in Aadhaar demographic records.
* Adult (17+) enrolments dominate across all states.
* Youth participation varies notably between states.
* Some regions indicate potential coverage gaps.

---

## 🌍 Impact & Applicability

* Supports demographic monitoring and reporting
* Helps identify states requiring targeted enrollment strategies
* Assists in administrative planning and digital inclusion initiatives
* Provides a foundation for dashboards and predictive systems

---

## 📁 Project Structure (Example)

* data/ → Raw Aadhaar demographic CSV files
* notebooks/ → Analysis scripts or notebooks
* outputs/ → Cleaned data and graphs
* README.md → Project documentation

---

## Some Graphs

<img width="1539" height="700" alt="State-wise Aadhar Distribution by Age Group" src="https://github.com/user-attachments/assets/0aee2920-348c-48a4-8022-233913786c29" />
<img width="1200" height="600" alt="State-wise Aadhar Count" src="https://github.com/user-attachments/assets/d6672ed3-f6f6-4334-bba8-e0306225212a" />

## 🏁 Conclusion

This project demonstrates how UIDAI Aadhaar demographic data can be transformed from fragmented raw records into a structured analytical framework that reveals meaningful demographic and geographical insights to support evidence‑based decision‑making.

---

## 👤 Author

Rahul Jaiswal
