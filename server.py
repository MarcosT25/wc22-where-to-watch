from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from ExpertSystem import WhereToGo
from experta import Fact

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.post("/get-data")
@cross_origin()
def get_data():
    content = request.json
    print(content)
    engine = WhereToGo()
    engine.reset()
    for key, value in content.items():
        engine.declare(Fact.from_iter({key: value}))
    engine.run()
    
    result = engine.result()
    if result == '':
        result = 'casa'
    
    print(result)
    return {"lugar": result}
