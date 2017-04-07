from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
import urllib
import urllib2

listen_ip = "127.0.0.1"
listen_port = "8089"

app = Flask(__name__)

@app.route("/", methods=['POST'])


def wait_message():
        if not request.json or not 'text' in request.json or not 'chatid' in request.json or not 'token' in request.json:
                abort(400)
        
        msg = {
               'token': request.json['token'], 
               'chatid': request.json['chatid'], 
               'text': request.json['text'],
        }

        msg_chat = urllib.quote(request.json['text'])

        msg_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(request.json['token'], request.json['chatid'], msg_chat ).encode('UTF-8')

        get = urllib2.urlopen(msg_url)

        return jsonify({'text': msg}), 201


if __name__ == "__main__":
        app.run(host=listen_ip, port=listen_port)
