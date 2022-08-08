from pymongo import MongoClient
import requests


class Comics:
    def agregar_comics(self, idd, title, image, onsaleDate, token):
        client = MongoClient(
            "mongodb+srv://ichigoabarai:yabinyabin@cluster0.d03gnab.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client.get_database("coppel")
        records = db.usuarios
        try:
            records.update_one(
                {"token": token},
                {
                    "$push": {
                        "comics": {
                            "id": idd,
                            "title": title,
                            "image": image,
                            "onsaleDate": onsaleDate,
                        }
                    }
                },
            )
        except:
            return False

    def buscar(self, categoria, nombre):
        busca = {"categoria": categoria, "nombre": nombre}
        response = requests.post("https://127.0.0.1:5000/searchToAdd", json=busca)
        return response.json()

    def verificar_token(self, token):
        client = MongoClient(
            "mongodb+srv://ichigoabarai:yabinyabin@cluster0.d03gnab.mongodb.net/?retryWrites=true&w=majority"
        )
        db = client.get_database("coppel")
        records = db.usuarios
        find = records.find_one({"token": token})
        if find == None:
            return False
        else:
            return True

    def run_buscador(self, categoria, nombre, token):
        if self.verificar_token(token):
            return self.buscar(categoria, nombre)
        else:
            return False
