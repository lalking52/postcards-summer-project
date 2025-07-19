from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Postcard Service</h1>
    <p>Доступные эндпоинты:</p>
    <ul>
        <li>GET /postcards - получить все открытки</li>
        <li>POST /postcards - создать новую открытку</li>
    </ul>
    """

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database='postcard_db',
        user='user',
        password='password'
    )
    return conn

@app.route('/postcards', methods=['GET'])
def get_postcards():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM postcards;')
    postcards = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(postcards)

@app.route('/postcards', methods=['POST'])
def create_postcard():
    new_postcard = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO postcards (recipient, message) VALUES (%s, %s) RETURNING id;',
                (new_postcard['recipient'], new_postcard['message']))
    postcard_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'id': postcard_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
