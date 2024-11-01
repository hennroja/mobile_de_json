import requests
import json
from bs4 import BeautifulSoup

def extract_table_data(url):
    """Extrahiert die Tabelle von der angegebenen URL und wandelt sie in JSON um.

    Args:
        url (str): Die URL der Webseite.

    Returns:
        list: Eine Liste von Dictionaries, wobei jedes Dictionary eine Tabellenzeile darstellt.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    with open('current-table.html', 'w', encoding='utf-8') as f:
        f.write(str(table))

    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 5 and not cols[0].get('colspan'):  # Überspringen von Zeilen mit colspan
            data.append({
                'Number': int(cols[0].text.strip()),
                'Column': cols[1].text.strip(),
                'Name': cols[2].text.strip(),
                'Required': 'ja' in cols[3].text.strip(),
                'Description': cols[4].text.strip()
            })

    return data

if __name__ == '__main__':
    url = 'https://www.eautoseller.de/doku/mobilede_csv_api_ext.html'
    data = extract_table_data(url)

    with open('mobile_de_csv.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
