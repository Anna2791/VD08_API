from flask import Flask, render_template

import requests
import ssl
import urllib3

# Отключаем предупреждения
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Игнорируем проверку SSL
context = ssl._create_unverified_context()
response = urllib3.PoolManager(cert_reqs='CERT_NONE', ssl_context=context)
response = requests.get('https://api.quotable.io/random', verify=False)
print(response.text)

app = Flask(__name__)

def get_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        return response.json()
    else:
        return {'content': 'Could not fetch quote', 'author': 'Unknown'}

@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)