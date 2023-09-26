from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

names = {'loki': {'age':23, 'desg':'ML' },
         'Hanif': {'age':23, 'desg':'front-end'}}
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    # def post(self):
    #     return {'data': 'posted'}
@app.route('/')
api.add_resource(HelloWorld, "/helloworld/<string:name>")
if __name__ == "__main__":
    app.run(debug=True)