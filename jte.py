
import pandas as pd
import json

# Input JSON file
input_file = "Books.json"

# Output Excel file
output_file = "Booksoutput.xlsx"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert JSON data into a table
df = pd.json_normalize(data)

# Save as Excel
df.to_excel(output_file, index=False)

print(f"Conversion completed: {output_file}")