from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/speed.html')
def my_link():
    print('I got clicked 811213')

    return 'Click.'
if __name__ =='__main__':
    app.run(debug = True)
