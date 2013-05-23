from flask import Flask, render_template, url_for, redirect
from datetime import date

import requests
from flask import request
from config import api_key, debug

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

@app.route('/devel_subscribe', methods=["POST"])
def devel_subscribe():
    requests.post(
            'https://api.mailgun.net/v2/lists/devel@lists.luftengine.org/members',
            auth=('api', api_key),
            data={'subscribed': True,
                'address': request.form['email']})
    return redirect(url_for('devel_subscribed'))

@app.route('/devel_subscribed')
def devel_subscribed():
    return render_template("devel_subscribed.html")

if __name__ == "__main__":
    app.debug = debug
    app.run()
