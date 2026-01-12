from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST', 'GET'])

def index():
    file_path = "checkphp.txt"
    if request.method == 'POST':
        tring = str(request.form.get('trex'))

        def check_string(file_path, line_string):
            with open(file_path, 'r') as file:
                content = file.read()
                return line_string in content

        chk_result = check_string(file_path, tring)
        if len(tring) == 125 and chk_result == False:
            with open(file_path, 'a') as append_file:
                append_file.write(f"{tring}\n")
            return "10011001001100111"
        else:
            return "100110010011001"

    else:
        return 'Priest(e)'


if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=8000)