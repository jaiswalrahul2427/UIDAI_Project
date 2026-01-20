import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD ALL FILES
files = [
    "api_data_aadhar_1.csv",
    "api_data_aadhar_2.csv",
    "api_data_aadhar_3.csv",
    "api_data_aadhar_4.csv",
    "api_data_aadhar_5.csv"
]



dfs = [pd.read_csv(file) for file in files]
data = pd.concat(dfs, ignore_index=True)

print(data)

print("Total rows after merge:", len(data))


# 2. BASIC CLEANING
data["state"] = (
    data["state"]
    .astype(str)
    .str.lower()
    .str.strip()
)

print("Unique states before fixing:", data["state"].nunique())


# 3. FIX COMMON WRONG NAMES
fix_map = {
    "orissa": "odisha",
    "pondicherry": "puducherry",
    "uttaranchal": "uttarakhand",
    "chhatisgarh": "chhattisgarh",
    "west bengli": "west bengal",
    "jammu & kashmir": "jammu and kashmir",
    "andaman & nicobar islands": "andaman and nicobar islands",
    "100000": np.nan
}

data["state"] = data["state"].replace(fix_map)

data = data[data["state"].notna()]
data = data[data["state"] != ""]


# 4. OFFICIAL STATES & UTs
valid_states = [
    "andhra pradesh","arunachal pradesh","assam","bihar","chhattisgarh","goa",
    "gujarat","haryana","himachal pradesh","jharkhand","karnataka","kerala",
    "madhya pradesh","maharashtra","manipur","meghalaya","mizoram","nagaland",
    "odisha","punjab","rajasthan","sikkim","tamil nadu","telangana","tripura",
    "uttar pradesh","uttarakhand","west bengal",

    "andaman and nicobar islands","chandigarh",
    "dadra and nagar haveli and daman and diu","delhi",
    "jammu and kashmir","ladakh","lakshadweep","puducherry"
]

data = data[data["state"].isin(valid_states)]

final_states = sorted(data["state"].unique())

print("\nFinal unique state list:")
print(final_states)
print("\nTotal administrative divisions:", len(final_states))
# print([col for col in data.columns if "age" in col.lower()])


# 5. STATE-WISE COUNT
state_counts = data["state"].value_counts().sort_values(ascending=False)

states = state_counts.index
counts = state_counts.values



# 6. MAKING GRAPH
plt.figure(figsize=(12,6))
plt.bar(states, counts)
plt.title("State-wise Aadhaar Count")
plt.xlabel("State")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()


# STATE-WISE AGE GROUP TOTALS
state_age = data.groupby("state")[[
    "demo_age_5_17",
    "demo_age_17_"
]].sum()

print("\nState-wise age group totals:")
print("Minimum number of people age between 5-17:\n",state_age.sort_values(by="demo_age_5_17",ascending=True))


# STATE-WISE AGE GROUP TOTALS
state_age = data.groupby("state")[[
    "demo_age_5_17",
    "demo_age_17_"
]].sum()

states = state_age.index
age_5_17 = state_age["demo_age_5_17"].values
age_17_plus = state_age["demo_age_17_"].values

x = np.arange(len(states))  
width = 0.4                  


# SINGLE COMBINED GRAPH
plt.figure(figsize=(16,7))

plt.bar(x - width/2, age_5_17, width, label="Age 5–17")
plt.bar(x + width/2, age_17_plus, width, label="Age 17+")


plt.xlabel("State")
plt.ylabel("Total Aadhaar Count")
plt.title("State-wise Aadhaar Distribution by Age Group")
plt.xticks(x, states, rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# 7. SAVE CLEAN DATA
# data.to_csv("clean_aadhar_data.csv", index=False)
# print("\nCleaned file saved as: clean_aadhar_data.csv")
