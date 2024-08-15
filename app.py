from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/double', methods = ['POST'])
def process():
    double = request.form['number']
    return render_template('index.html', result = int(double) * 2)

@app.route('/reset')
def reset_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)