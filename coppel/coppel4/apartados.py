from pymongo import MongoClient


class Apartados:
    def buscar_apartados(self, token):
        client = MongoClient(
            "mongodb+srv://ichigoabarai:yabinyabin@cluster0.d03gnab.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client.get_database("coppel")
        records = db.usuarios
        try:
            find = records.find_one({"token": token}, {"comics": 1})
            if find == None:
                return False
            elif find["comics"] == []:
                return None
            else:
                return find["comics"]
        except Exception as e:
            return "No"
