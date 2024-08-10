from flask import Flask, render_template

app = Flask(__name__)

# Define the data
dataI = ['I', 'G', 'S']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/igs')
def igs():
    return render_template('igs.html', data=dataI)

if __name__ == '__main__':
    app.run(debug=True)