from flask import Flask, render_template, url_for
from datetime import date

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download')
def download():
    return render_template("download.html")

@app.route('/docs')
def docs():
    return render_template("docs.html")

@app.route('/develop')
def develop():
    return render_template("develop.html")

@app.context_processor
def inject_year():
    return dict(year=date.today().strftime("%Y"))

@app.route('/devel_subscribe')
def devel_subscribe():
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run()
