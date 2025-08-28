import csv
import os

data_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(data_dir, 'formatted_sales_data.csv')

# List all relevant CSV files in the data directory
csv_files = [f for f in os.listdir(data_dir) if f.startswith('daily_sales_data_') and f.endswith('.csv')]

output_rows = []

for filename in csv_files:
	file_path = os.path.join(data_dir, filename)
	with open(file_path, 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['product'].strip().lower() == 'pink morsel':
				try:
					quantity = int(row['quantity'])
					price = float(row['price'].replace('$', ''))
					sales = quantity * price
					output_rows.append({
						'Sales': f'{sales:.2f}',
						'Date': row['date'],
						'Region': row['region']
					})
				except Exception:
					continue

# Write the output CSV
with open(output_file, 'w', newline='') as outcsv:
	fieldnames = ['Sales', 'Date', 'Region']
	writer = csv.DictWriter(outcsv, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerows(output_rows)
