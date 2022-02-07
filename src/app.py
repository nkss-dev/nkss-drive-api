from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route('/files', methods=['GET'])
def files():
   # FIXME: don't do this every time
   db.connect("./data/db.sqlite3")
   tags = request.args.get("tags")
   if tags is None: 
      tags = []
   else:
      tags = tags.split(",")    
   return jsonify(db.list_files(tags))


if __name__ == "__main__":
   app.run(debug=True, port=8000)
   
