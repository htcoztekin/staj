
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


musics = [
    {'id': 0,
     'sarki': 'Ah Yillar',
     'sanatci': 'Sezen Aksu',
     'album': 'Kalpten',
     'album_yili': '2014'},
    {'id': 1,
     'sarki': 'Allahaskina',
     'sanatci': 'Sezen Aksu',
     'album': 'Allahaskina',
     'album_yili': '1979'},
    {'id': 2,
     'sarki': 'Bana Ellerini Ver',
     'sanatci': 'Sezen Aksu',
     'album': 'Beni Affet',
     'album_yili': '1991'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>müzik arşivi</h1>
<p>Bu site,Sezen Aksu şarkılarının dinlenmesi için prototip API'dir.</p>'''


@app.route('/api/a1/resources/musics/all', methods=['GET'])
def api_all():
    return jsonify(musics)


@app.route('/api/a1/resources/musics', methods=['GET'])
def api_id():
   
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

   
    results = []

   
    for music in musics:
        if music['id'] == id:
            results.append(music)

    
    return jsonify(results)

app.run()