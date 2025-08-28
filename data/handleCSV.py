import csv
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the project root (parent of script directory)
project_root = os.path.dirname(script_dir)
# Data directory is the script directory
data_dir = script_dir
# Output file in project root
output_file = os.path.join(project_root, 'formatted_sales_data.csv')

# Find all CSV files
csv_files = [f for f in os.listdir(data_dir) if f.startswith('daily_sales_data_') and f.endswith('.csv')]
csv_files.sort()  # Sort for consistent order

output_rows = []

# Process each CSV file
for filename in csv_files:
    file_path = os.path.join(data_dir, filename)
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = row.get('product', '').strip()
                if product.lower() == 'pink morsel':
                    try:
                        quantity = int(row['quantity'].strip())
                        price_str = row['price'].strip()
                        price = float(price_str.replace('$', ''))
                        sales = quantity * price
                        output_rows.append({
                            'Sales': f'{sales:.2f}',
                            'Date': row['date'].strip(),
                            'Region': row['region'].strip()
                        })
                    except (ValueError, KeyError):
                        continue
    except FileNotFoundError:
        continue

# Write the output CSV
with open(output_file, 'w', newline='', encoding='utf-8') as outcsv:
    fieldnames = ['Sales', 'Date', 'Region']
    writer = csv.DictWriter(outcsv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"Processed {len(output_rows)} rows and saved to {output_file}")
