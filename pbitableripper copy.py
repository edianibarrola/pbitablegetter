import csv
from bs4 import BeautifulSoup

# Open the input file in read mode
with open('input.txt', 'r') as f:
    # Read the HTML content
    html_content = f.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class starting with 'ng-tns-c' and ending with 'ng-star-inserted'
table_parents = soup.find_all(class_=lambda value: value and value.startswith('ng-tns-c') and value.endswith('ng-star-inserted'))

# Open the output CSV file in write mode
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    for parent in table_parents:
        # Find the table name within the parent
        table = parent.find(class_='entityName trimmedTextWithEllipsis')
        if table is not None:
            # Write the table name to the CSV file
            writer.writerow(['Table Name:', table.get_text()])

            # Extract all the field names within the current table parent
            fields = parent.find_all(class_='field-name')

            # Write the field names to the CSV file
            writer.writerow(['Field Names:'])
            for field in fields:
                writer.writerow([field.get_text()])

            # Write an empty row as separator between tables
            writer.writerow([])
