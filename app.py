from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import json
from bson import json_util, ObjectId

app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb+srv://TeamCatViz:RockingTeam#1@cluster0.jityt.mongodb.net/pet_db?retryWrites=true&w=majority"
mongo = PyMongo(app)

# Route to render webpage
@app.route("/")
def index():
    # # Retrieve the first 100 records from the MongoDB collection for testing (limit 100 set for quick demo)
    pets_coll = mongo.db.pet_data.find(limit=100)
# # Convert PyMongo cursor to json string
    pets_json = json.loads(json_util.dumps(pets_coll))
    return render_template("index.html", pets_data=pets_json)

# Route to retrieve pet data from cloud database. Called by all JavaScript files.
@app.route("/getPetData")
def getPetData():

     # # Retrieve the first 100 records from the MongoDB collection for testing
    pets_coll = mongo.db.pet_data.find(limit=100)
# # Convert PyMongo cursor to json string
    pets_json = json_util.dumps(pets_coll)
    return pets_json

# Route to retreive lat/long look-up table. Called by map.js.
@app.route("/lookUpLocation")
def lookUpLocation():
    with open("data/location_lookup.json", "r") as file:

        return file.read()
        
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)