from bs4 import BeautifulSoup

# Open the input file in read mode
with open('input.txt', 'r') as f:
    # Read the HTML content
    html_content = f.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class starting with 'ng-tns-c' and ending with 'ng-star-inserted'
table_parents = soup.find_all(class_=lambda value: value and value.startswith('ng-tns-c') and value.endswith('ng-star-inserted'))

# Open the output file in write mode
with open('output.txt', 'w') as f:
    for parent in table_parents:
        # Find the table name within the parent
        table = parent.find(class_='entityName trimmedTextWithEllipsis')
        if table is not None:
            # Write the table name to the file
            f.write('Table Name:\n')
            f.write(table.get_text() + '\n')

            # Extract all the field names within the current table parent
            fields = parent.find_all(class_='field-name')

            # Write the field names to the file
            f.write('Field Names:\n')
            for field in fields:
                f.write(field.get_text() + '\n')

            # Write a separator
            f.write('\n')
