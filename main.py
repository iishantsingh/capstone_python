import pandas as pd

# ------------------------------
# Load the 3 building CSV files
# ------------------------------
a = pd.read_csv("building_A_2025.csv")
b = pd.read_csv("building_B_2025.csv")
c = pd.read_csv("building_C_2025.csv")

# Convert timestamps
for df in [a, b, c]:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Rename columns
a = a.rename(columns={"kwh": "building_a_kwh"})
b = b.rename(columns={"kwh": "building_b_kwh"})
c = c.rename(columns={"kwh": "building_c_kwh"})

# ------------------------------
# Merge into a single dataset
# ------------------------------
df = a.merge(b, on="timestamp").merge(c, on="timestamp")

# Total kWh
df["total_kwh"] = df[["building_a_kwh", "building_b_kwh", "building_c_kwh"]].sum(axis=1)

# Save cleaned dataset
df.to_csv("cleaned_energydata.csv", index=False)

# ------------------------------
# Building Summary
# ------------------------------
building_summary = pd.DataFrame({
    "building": ["Building A", "Building B", "Building C"],
    "total_kwh": [
        df["building_a_kwh"].sum(),
        df["building_b_kwh"].sum(),
        df["building_c_kwh"].sum()
    ]
})

building_summary.to_csv("building_summary.csv", index=False)

# ------------------------------
# Summary Text File
# ------------------------------
total_campus = df["total_kwh"].sum()
highest_building = building_summary.loc[building_summary["total_kwh"].idxmax(), "building"]
peak_row = df.loc[df["total_kwh"].idxmax()]

daily = df.set_index("timestamp").resample("D")["total_kwh"].sum()
weekly = df["total_kwh"].sum()  # All data is in one week

summary_text = f"""
TOTAL CAMPUS CONSUMPTION
------------------------
Total campus energy consumption: {total_campus} kWh

HIGHEST CONSUMING BUILDING
--------------------------
{highest_building}

PEAK LOAD TIME
--------------
Peak time: {peak_row['timestamp']} with {peak_row['total_kwh']} kWh

DAILY TREND
-----------
{daily.to_string()}

WEEKLY TREND
------------
Weekly total: {weekly} kWh
"""

with open("summary.txt", "w") as f:
    f.write(summary_text)