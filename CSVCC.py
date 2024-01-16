import csv
import sys

# Set a large field size limit
csv.field_size_limit(2**31 - 1)

def remove_empty_columns(csv_path):
    try:
        with open(csv_path, 'r', newline='', encoding='cp1252') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Count and transpose data to work with columns as rows
    original_column_count = len(data[0])
    transposed_data = list(zip(*data))
    
    #Filter out empty columns
    filtered_data = [col for col in transposed_data if any(cell.strip() for cell in col)]

    # Transpose data back to original format
    cleaned_data = list(zip(*filtered_data))
    cleaned_column_count = len(cleaned_data[0])
    columns_removed = original_column_count - cleaned_column_count

    # Write the cleaned data to a new CSV file
    new_csv_path = csv_path.replace('.csv', '_cleaned.csv')
    with open(new_csv_path, 'w', newline='', encoding='cp1252') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(cleaned_data)

    print(f"Cleaned CSV saved as: {new_csv_path}")
    print(f"Number of columns removed: {columns_removed}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: CSVCC.py file.csv")
    else:
        csv_path = sys.argv[1]
        remove_empty_columns(csv_path)
