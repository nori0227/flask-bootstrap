from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p1_homepage_bootstrap.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('p2_homepage_bootstrap.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

