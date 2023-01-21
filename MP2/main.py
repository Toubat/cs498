from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        seed = request.json['num']
        with open('seed', 'w') as f:
            f.write(str(seed))
        return str(seed)
    else:
        with open('seed', 'r') as f:
            seed = f.read()
        return seed

if __name__ == '__main__':
    with open('seed', 'w') as f:
        f.write('0')
    app.run(debug = True)