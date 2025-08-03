from flask import Flask
from routes.users import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db

db.init_app(app)
app.register_blueprint(user_bp)

@app.route('/')
def health_check():
    return {'status': 'OK'}, 200

if __name__ == '__main__':
    app.run(debug=True)
