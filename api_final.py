import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>müzik arşivi</h1>
<p>Bu site,Sezen Aksu şarkılarının dinlenmesi için prototip API'dir..</p>'''


@app.route('/api/a1/resources/musics/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('musics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_musics = cur.execute('SELECT * FROM musics;').fetchall()

    return jsonify(all_musics)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/a1/resources/musics', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    sarki = query_parameters.get('sarki')
    album = query_parameters.get('album')

    query = "SELECT * FROM musics WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if sarki:
        query += ' sarki=? AND'
        to_filter.append(sarki)
    if album:
        query += ' album=? AND'
        to_filter.append(album)
    if not (id or sarki or album):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('musics.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()