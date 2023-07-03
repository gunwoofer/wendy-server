from flask import Flask

app = Flask(__name__)

@app.route('/createWeekend', methods=['GET'])
def create_weekend():
    print('Request received !!')
    return 'success'

if __name__ == '__main__':
    app.run()