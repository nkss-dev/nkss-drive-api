# TODO flask
from flask import Flask
import db

app = Flask(__name__)

# add a route that calls db.list_files()
@app.route("/files")
def files():
   return db.list_files()

if __name__ == "__main__":
   app.run(debug=True, port=8000)
   
