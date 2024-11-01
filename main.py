import requests
import json
from bs4 import BeautifulSoup


def extract_table_data(url):
    """Extracts table data from the given URL and converts it to a list of dictionaries.

    Args:
        url (str): The URL of the webpage containing the table.

    Returns:
        list: A list of dictionaries, where each dictionary represents a table row.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')

    # Write the table HTML to a file for debugging purposes (optional)
    with open('current-table.html', 'w', encoding='utf-8') as f:
        f.write(str(table))

    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 5 and not cols[0].get('colspan'):  # Skip rows with colspan
            data.append({
                'number': int(cols[0].text.strip()),
                'column': cols[1].text.strip(),
                'name': cols[2].text.strip(),
                'required': 'ja' in cols[3].text.strip(),
                'description': cols[4].text.strip(),
                'dataType': determine_data_type(cols[4].text.strip())

            })

    return data


def determine_data_type(description):
    """Determines the data type based on the given description text.

    Args:
        description (str): The description text used to infer the data type.

    Returns:
        str: The inferred data type (e.g., "boolean", "int", "string", "date", "float").
    """

    if "(0=nein, 1=ja)" in description:
        return "boolean"
    elif "reserviert, muss leer sein" in description:
        return "null"
    elif description.startswith(("0", "'0", "1", "'1")):
        return "int"
    elif "Ganzzahl" in description:  # German for "integer"
        return "int"
    elif "Text" in description:
        return "string"
    elif "Datumsangabe" in description:  # German for "date specification"
        return "date"
    elif "Zahl " in description:  # German for "number"
        return "float"
    else:
        return "string"  # Default to string for unknown types


def step1_get_latest_state():
    """Fetches table data from the provided URL and saves it as JSON."""

    url = 'https://www.eautoseller.de/doku/mobilede_csv_api_ext.html'
    data = extract_table_data(url)

    with open('mobile_de_csv.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    step1_get_latest_state()
