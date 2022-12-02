import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://HMTD-Links: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@github.com/HMTD-Links/Mogenius $REPO ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
