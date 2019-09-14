from app import app

#Decorator, aplica uma funcao em cima de outra
@app.route("/")
def index():
  return "Hello world!"