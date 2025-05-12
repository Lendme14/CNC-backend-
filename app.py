from flask import Flask, request, jsonify, render_template
from bot_handler import handle_update
from web3_helper import get_token_balance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    handle_update(update)
    return jsonify({"status": "ok"})

@app.route('/balance/<wallet_address>')
def balance(wallet_address):
    balance = get_token_balance(wallet_address)
    return jsonify({"CNC_balance": balance})

if __name__ == '__main__':
    app.run()