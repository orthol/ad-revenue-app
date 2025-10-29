from flask import Flask, render_template, request, redirect, url_for
import random
import time
import os

app = Flask(__name__)

# Configuration
REDIRECT_URL = "https://t.me/halowbot"  # Change this to your target URL
AD_DELAY = 10  # Seconds user must wait before redirect

# Ad networks (you can enable/disable these)
AD_NETWORKS = {
    'google_adsense': True,
    'media_net': True,
    'amazon_native': True,
    'propeller_ads': True,
    'adsterra': True
}

@app.route('/')
def index():
    """Main page with ads and countdown"""
    return render_template('index.html', 
                         redirect_url=REDIRECT_URL,
                         ad_delay=AD_DELAY,
                         ad_networks=AD_NETWORKS)

@app.route('/redirect')
def redirect_user():
    """Final redirect endpoint"""
    return redirect(REDIRECT_URL)

@app.route('/health')
def health():
    """Health check for deployment"""
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
