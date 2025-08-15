from flask import Flask, request, jsonify
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db', 'app.sqlite')
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(open(os.path.join(os.path.dirname(__file__),'..','db','schema.sql')).read())

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        with get_db() as conn:
            rows = conn.execute('SELECT id, name, price, stock FROM items').fetchall()
            return jsonify([dict(r) for r in rows])
    data = request.get_json(force=True)
    with get_db() as conn:
        cur = conn.execute(
            'INSERT INTO items(name, price, stock) VALUES(?,?,?)',
            (data.get('name'), float(data.get('price', 0)), int(data.get('stock', 0)))
        )
        conn.commit()
        return jsonify(id=cur.lastrowid), 201

@app.route('/items/<int:item_id>', methods=['PUT', 'DELETE'])
def item_detail(item_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        with get_db() as conn:
            conn.execute('UPDATE items SET name=?, price=?, stock=? WHERE id=?',
                         (data.get('name'), float(data.get('price', 0)), int(data.get('stock', 0)), item_id))
            conn.commit()
            return jsonify(updated=True)
    else:
        with get_db() as conn:
            conn.execute('DELETE FROM items WHERE id=?', (item_id,))
            conn.commit()
            return jsonify(deleted=True)

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        init_db()
    app.run(host='0.0.0.0', port=8000)
