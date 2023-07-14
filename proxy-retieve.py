import requests
import json

url = 'https://proxylist.geonode.com/api/proxy-list?limit=10&page=1&sort_by=lastChecked&sort_type=desc'

response = requests.get(url)
data = response.json()

# Deserializza i dati JSON e accedi alla lista 'data'
proxy_list = data['data']

# Stampa i dettagli dei proxy
for proxy in proxy_list:
    print("ID:", proxy['_id'])
    print("IP:", proxy['ip'])
    print("Anonymity Level:", proxy['anonymityLevel'])
    print("ASN:", proxy['asn'])
    print("City:", proxy['city'])
    print("Country:", proxy['country'])
    print("Created At:", proxy['created_at'])
    # Aggiungi altri campi se necessario

    print()  # Stampa una riga vuota per separare i proxy

# Stampa il numero totale di proxy e il numero di pagina corrente
print("Total:", data['total'])
print("Page:", data['page'])
