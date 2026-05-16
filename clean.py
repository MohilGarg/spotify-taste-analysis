import pandas as pd
import sys
import os

input_path = sys.argv[1]
df = pd.read_csv(input_path)

original_count = len(df)
df = df.drop_duplicates(subset=['Track Name', 'Artist Name(s)'], keep='first')
removed = original_count - len(df)

base, ext = os.path.splitext(input_path)
output_path = f"{base}_cleaned{ext}"
df.to_csv(output_path, index=False)

print(f"Removed {removed} duplicate(s). Cleaned file saved to {output_path}")