import requests
from bs4 import BeautifulSoup

def get_dkp_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ambil data DKP di sini
    dkp_table = soup.find('table', {'id': 'dkp_table'})
    dkp_data = []
    for row in dkp_table.find_all('tr')[1:]:  # Melewati header tabel
        cols = row.find_all('td')
        player_name = cols[0].text.strip()
        dkp_score = cols[1].text.strip()
        dkp_data.append({'name': player_name, 'dkp': dkp_score})

    return dkp_data

if __name__ == "__main__":
    url = 'https://your-alliance-website.com/dkp'
    dkp_data = get_dkp_data(url)
    for data in dkp_data:
        print(f"Player: {data['name']}, DKP: {data['dkp']}")
      
