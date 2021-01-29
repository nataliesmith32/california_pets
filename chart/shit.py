# Import dependencies
import json
import pandas as pd

# List to hold unique list of animal types
types = []
typeCounts = {}

# Function to read in all json files and compile all of their animal types into a single list of unique types
def addTypes(dataset):
    with open(dataset, "r", encoding = "utf8") as f_in:
        df = pd.read_json(f_in)
        typeCounts_gb = df.groupby(["type"]).count().sort_values(by=["id"], ascending = False)
        print(typeCounts_gb.head(10))
    
# List of datasets containing address info to be merged
datasets = ["testdata.json"]

# Pass each dataset through addAddresses function to build list of unique addresses
for dataset in datasets:
    addTypes(dataset)
