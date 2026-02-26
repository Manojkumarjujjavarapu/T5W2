import pandas as pd
import os

os.makedirs("bulk_data", exist_ok=True)

for i in range(200):
    df = pd.DataFrame({
        "id": range(1000),
        "value": range(1000)
    })
    
    file_path = f"bulk_data/file_{i}.csv"
    df.to_csv(file_path, index=False)

print("✅ Bulk data created successfully!")