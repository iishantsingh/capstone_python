# 📊 Energy Consumption Analysis & Dashboard

This project analyzes energy usage data from three buildings (A, B, C) on a campus.
It processes raw CSV files, cleans the data, generates summaries, and produces a visual dashboard showing daily trends, building usage, and peak-hour consumption.


---

# 📁 Project Structure

project/
│
├── building_A_.csv
├── building_B_.csv
├── building_C_.csv
│
├── cleaned_energydata.csv
├── building_summary.csv
├── summary.txt
│
├── dashboard.png
├── main.py


---

# 📌 Features of This Project

## Data Cleaning & Merging

1. Loads raw CSV data for Buildings A, B, and C

2. Converts timestamps into datetime format

3. Merges all buildings into one clean dataset

4. Calculates total campus consumption per timestamp


## Summary Outputs

The project automatically generates:

1. cleaned_energydata.csv → merged dataset

2. building_summary.csv → total usage per building

summary.txt containing:

1. Total campus consumption

2. Highest consuming building

3. Peak load timestamp

4. Daily trend

5. Weekly trend



## Dashboard Visualization

dashboard.png includes three charts:

1. Daily Campus Consumption (line chart)


2. Average Weekly Usage per Building (bar chart)


3. Peak-hour Consumption for All Buildings (scatter plot)



These visuals help understand energy patterns and peak usage times.


---

# 📊 Example Insights (based on your dataset)

Total campus usage: 2470 kWh

Highest consuming building: Building C

Peak load time: 2025-01-03 12:00 (463 kWh)

Daily trend: Increase → then slight decrease

Weekly trend: All data lies within one week



---

# 🐍 How to Run the Project

## 1️⃣ Install dependencies

pip install pandas matplotlib

## 2️⃣ Place the building CSV files in the project folder

building_A_.csv

building_B_.csv

building_C_.csv


## 3️⃣ Run the Python script

python main.py

The script will automatically generate:

Clean dataset

Summary files

Dashboard image



---

# 📦 Output Files Explained

cleaned_energydata.csv

## Merged dataset with columns:

timestamp, building_a_kwh, building_b_kwh, building_c_kwh, total_kwh

building_summary.csv

Total kWh consumed by each building during the week.

summary.txt

Plain-text summary containing key insights.

dashboard.png

## A three-part dashboard showing:

Daily trend

Average weekly building usage

Peak-hour usage



---

# 📘 Purpose of This Project

This project is designed for:

Energy monitoring

Campus/facility management

Academic assignments

Understanding and visualizing energy trends



---

# 🙌 Author

Ishant Singh

2501410067

BTech CSE (Cyber Security)


---
