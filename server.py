from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from ExpertSystem import ExpertSystem
from experta import Fact

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.post("/get-data")
@cross_origin()
def get_data():
    content = request.json
    contentCost = content["input"]
    
    engine = ExpertSystem()
    engine.reset()
    engine.declare(Fact(input=contentCost))
    engine.run()
    
    result = engine.result()
    return jsonify({"lugar": result})
