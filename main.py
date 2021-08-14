from datetime import datetime
import os
import json
from flask import Flask

app = Flask(__name__)

if not os.path.isfile('resources/logs.json'):
    print('Creating new json file...')

    with open('resources/logs.json', 'w') as f:
        text_dict = {'main_text': "Test text",
                     'last_text': None,
                     'connect_log': list()}
        json.dump(text_dict, fp = f)

    print('...json new file created')
else:
    print('Json file already exists ')

i = 0

@app.route('/')
def main_page():
    with open('resources/logs.json', 'r') as f:
        json_obj = json.load(f)

    now = datetime.now()
    now_str = now.strftime("%d/%m/%Y, %H:%M:%S")
    json_obj['connect_log'].append(now_str)

    with open('resources/logs.json', 'w') as f:
        json.dump(json_obj, fp=f)
        return json_obj

if __name__  == '__main__':
    app.run(host='0.0.0.0', port='8010', debug=True)
