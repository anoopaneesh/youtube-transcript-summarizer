import flask
from flask import request, jsonify
import summary
from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    id=None
    if 'id' in request.args:
        id=request.args['id']
    else:
        print("Error : No id was provided")
    return jsonify({'text':summary.get_text_summary(id)})

app.run()