import requests

kleur = input('welke kleur wilt u aan de selectie toevoegen ')
# Define the headers
headers = {'Content-type': 'application/json'}

# Define the request body
request_body = {
    "invul_veld1": kleur 
}

#print(request_body)
url = 'http://localhost:8080/extra_kleur'  
response = requests.post(url, json=request_body)
print(response.status_code)
print(response.json())

#let op je moet dit programma runnen in een eigen (nieuw) terminal window
