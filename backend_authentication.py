
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

def authenticat_mail(username):
    uri = "mongodb+srv://projectusagedev:Ss1901107@cluster0.4xoe7pk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri)
    db = client["dev"]
    user_db = db["Authentication"]
    user = user_db.find_one({"email": username})
    if user:
        return True
    else:
        return False

def create_user(user_email,pasword):
    uri = "mongodb+srv://projectusagedev:Ss1901107@cluster0.4xoe7pk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client["dev"]
    user_db = db["Authentication"]

    if authenticat_mail(user_email):
        return 1
    else:
        #user = user_db.find_one({"email": username, "password": password})
        insert_result = user_db.insert_one({"email": user_email, "password": pasword})
        if insert_result:
            return 0
        else:
            return 2

