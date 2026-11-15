from flask import Flask, render_template
from app.authentication.auth import *
from app.admin import admin_bp

app = Flask(__name__)
app.secret_key = "Gangadhar- hi-Shaktiman-hai"
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)