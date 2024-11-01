import json
import re

def normalize_column_name(name):
    """Normalizes a column name by replacing special characters and spaces.

    Args:
        name (str): The original column name.

    Returns:
        str: The normalized column name.
    """

    name = name.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    name = re.sub(r'[()]', '', name)  # Remove brackets from column name
    return re.sub(r'[^a-zA-Z0-9_]', '_', name).strip('_')

def generate_postgres_schema(json_file, sql_file):
    """Generates a PostgreSQL schema based on a JSON schema.

    Args:
        json_file (str): The path to the JSON file.
        sql_file (str): The path to the output SQL file.
    """

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(sql_file, 'w', encoding='utf-8') as f:
        f.write("CREATE TABLE vehicles (\n")

        for item in data:
            column_name = normalize_column_name(item["name"])
            data_type = item["dataType"]

            # Mapping of JSON data types to PostgreSQL data types
            postgres_type = {
                "boolean": "boolean",
                "date": "date",
                "float": "numeric",
                "int": "integer",
                "string": "text"
            }.get(data_type, "text")  # Default to text

            # Ignore columns with the data type "null"
            if data_type != "null":
                f.write(f"    {column_name} {postgres_type},\n")

        f.write(");\n")

generate_postgres_schema("mobile_de_csv.json", "mobile_de_vehicle_schema.sql")