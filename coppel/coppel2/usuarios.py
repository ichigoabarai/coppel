import uuid
from pymongo import MongoClient


class Usuarios:
    def agregar_nuevo(self, usuario, nombre, edad, password):
        token = str(uuid.uuid4()).replace("-", "")
        client = MongoClient(
            "mongodb+srv://ichigoabarai:yabinyabin@cluster0.d03gnab.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client.get_database("coppel")
        records = db.usuarios
        data = {
            "usuario": usuario,
            "name": nombre,
            "password": password,
            "age": edad,
            "token": token,
            "comics": [],
        }
        try:
            find = records.find_one({"usuario": usuario})
            if find == None:
                records.insert_one(data)
                return token
            else:
                return False
        except Exception as e:
            return "No"

    def login(self, usuario, password):
        client = MongoClient(
            "mongodb+srv://ichigoabarai:yabinyabin@cluster0.d03gnab.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client.get_database("coppel")
        records = db.usuarios
        find = records.find_one(
            {"usuario": usuario, "password": password}, {"password": 0, "comics": 0}
        )
        if find == None:
            return False
        else:
            find["_id"] = str(find["_id"])
            return find
