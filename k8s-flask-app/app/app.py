from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL", "postgresql://flaskuser:postgrespw@postgres-service:5432/flaskdb")

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(DB_URL)
        conn.close()
        return "Connected to PostgreSQL!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)