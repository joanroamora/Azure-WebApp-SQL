from flask import Flask, render_template, request, jsonify
from logic.py import process_form_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Recoger los datos del formulario
    name = request.form.get('name')
    last_name = request.form.get('last-name')
    account_number = request.form.get('account-number')
    
    # Procesar los datos con la función del archivo logic.py
    result = process_form_data(name, last_name, account_number)
    
    # Enviar una respuesta al frontend (esto podría ser una redirección o un JSON con la respuesta)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
