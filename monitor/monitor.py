from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  return 'This interface is not supported. Go away.'

if __name__ == '__main__':
  app.run()
