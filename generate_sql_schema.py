import json

def generate_postgres_schema(json_file, sql_file):
    """Generiert ein PostgreSQL-Schema basierend auf einem JSON-Schema.
    Args:
        json_file (str): Der Pfad zur JSON-Datei.
        sql_file (str): Der Pfad zur zu erstellenden SQL-Datei.
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(sql_file, 'w') as f:
        f.write("CREATE TABLE vehicles (\n")

        for item in data:
            column_name = item["name"]
            data_type = item["dataType"]

            # Mapping von JSON-Datentypen zu PostgreSQL-Datentypen
            postgres_type = {
                "boolean": "boolean",
                "date": "date",
                "float": "numeric",
                "int": "integer",
                "string": "text"
            }.get(data_type, "text")  # Default zu text

            # Ignoriere Spalten mit dem Datentyp "null"
            if data_type != "null":
                f.write(f"    {column_name} {postgres_type},\n")

        f.write(");\n")

generate_postgres_schema("mobile_de_csv.json", "mobile_de_vehicle_schema.sql")