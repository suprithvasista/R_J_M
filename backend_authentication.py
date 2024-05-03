
from pymongo.mongo_client import MongoClient

def authenticate(username, password):
    uri = "mongodb+srv://projectusagedev:Ss1901107@cluster0.4xoe7pk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    db = client["dev"]
    user_db = db["Authentication"]
    user = user_db.find_one({"email": username, "password": password})
    if user:
        return True
    else:
        return False

