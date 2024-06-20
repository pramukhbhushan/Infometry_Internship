import re

def extract_tables(sql_query):
    # Regex patterns to find source and destination tables
    source_pattern = re.compile(r'\bFROM\s+([\w.]+)|\bJOIN\s+([\w.]+)', re.IGNORECASE)
    dest_pattern = re.compile(r'\bINSERT\s+(?:INTO|OVERWRITE)\s+([\w.]+)', re.IGNORECASE)  # Adjusted pattern   
    source_tables = set()
    dest_tables = set()
    
    # Find all source tables
    for match in source_pattern.finditer(sql_query):
        for group in match.groups():
            if group:
                source_tables.add(group.strip())
    
    # Find all destination tables

    for match in dest_pattern.finditer(sql_query):  
        for group in match.groups():
            if group:
                dest_tables.add(group.strip())
    
    return source_tables, dest_tables

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        sql_query = file.read()
    
    source_tables, dest_tables = extract_tables(sql_query)
    
    print("Source Tables:")
    for table in sorted(source_tables):
        print(table)
    
    print("\nDestination Tables:")
    for table in sorted(dest_tables):
        print(table)

# Example usage:
input_file = 'store_prouc_process_dta.txt'  # Replace with your actual file path
main(input_file)
