import csv

# Open the input CSV file
with open('input_file.csv', 'r') as infile:
    reader = csv.reader(infile)

    # Skip the header row
    next(reader)

    # Initialize variables for statistics
    total_sales = 0
    max_sales = 0
    min_sales = float('inf')

    # Loop through each row in the CSV file
    for row in reader:
        # Extract the sales data from the row
        sales = float(row[1])

        # Update the statistics variables
        total_sales += sales
        max_sales = max(max_sales, sales)
        min_sales = min(min_sales, sales)

    # Calculate additional statistics
    average_sales = total_sales / (reader.line_num - 1)
    num_sales = reader.line_num - 1

# Open the output CSV file and write the statistics to it
with open('output_file.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write the header row
    writer.writerow(['Total Sales', 'Average Sales',
                    'Max Sales', 'Min Sales', 'Number of Sales'])

    # Write the statistics data
    writer.writerow([total_sales, average_sales,
                    max_sales, min_sales, num_sales])
