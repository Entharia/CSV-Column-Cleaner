import csv
import sys

# Set a large field size limit
csv.field_size_limit(2**31 - 1)

def remove_empty_columns(csv_path):
    try:
        with open(csv_path, 'r', newline='', encoding='cp1252') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)

        # Extract headers and data
        headers = data[0]
        data_rows = data[1:]

        # Transpose data to work with columns as rows
        transposed_data = list(zip(*data_rows))

        # Identify indices of non-empty columns
        non_empty_indices = [i for i, col in enumerate(transposed_data) if any(cell.strip() for cell in col)]

        # Filter headers and data based on non-empty column indices
        filtered_headers = [headers[i] for i in non_empty_indices]
        filtered_data_rows = [[row[i] for i in non_empty_indices] for row in data_rows]

        # Write the cleaned data to a new CSV file
        new_csv_path = csv_path.replace('.csv', '_cleaned.csv')
        with open(new_csv_path, 'w', newline='', encoding='cp1252') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(filtered_headers)
            writer.writerows(filtered_data_rows)

        print(f"Cleaned CSV saved as: {new_csv_path}")
        print(f"Number of columns removed: {len(headers) - len(filtered_headers)}")

    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python CSVCC.py file.csv")
    else:
        csv_path = sys.argv[1]
        remove_empty_columns(csv_path)

