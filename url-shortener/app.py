from flask import Flask, request, jsonify, redirect
from models import Base, URL
from database import engine, SessionLocal
from utils import generate_short_id
import validators

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('original_url')

    if not original_url or not validators.url(original_url):
        return jsonify({'error': 'Invalid URL'}), 400

    db = SessionLocal()
    existing = db.query(URL).filter_by(original_url=original_url).first()
    if existing:
        db.close()
        return jsonify({'short_url': request.host_url + existing.short_id}), 200

    short_id = generate_short_id()
    new_url = URL(original_url=original_url, short_id=short_id)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    db.close()

    return jsonify({'short_url': request.host_url + short_id}), 201

@app.route('/<short_id>')
def redirect_url(short_id):
    db = SessionLocal()
    url = db.query(URL).filter_by(short_id=short_id).first()
    db.close()
    if url:
        return redirect(url.original_url)
    return jsonify({'error': 'URL not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)
