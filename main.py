from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/createWeekend', methods=['GET'])
def create_weekend():
    print('Request received !!')
    return 'success'

if __name__ == '__main__':
    app.run()