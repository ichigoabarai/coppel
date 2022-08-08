import requests


class Buscador:
    def buscar_personaje(self, nombre):
        datos = []
        if nombre == "":
            try:
                response = requests.get(
                    "https://gateway.marvel.com/v1/public/characters?orderBy=name&ts=1&apikey=3e187c3b3668d0001c85763b92813a46&hash=cd5c6dff6c034615a4d1ceb8795cfe7c"
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return {"data": "hubo un error con la aplicacion"}
        else:
            try:
                response = requests.get(
                    f"https://gateway.marvel.com/v1/public/characters?name={nombre}&orderBy=name&ts=1&apikey=3e187c3b3668d0001c85763b92813a46&hash=cd5c6dff6c034615a4d1ceb8795cfe7c"
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return {"data": "hubo un error con la aplicacion"}
        response_json = response.json()
        if response_json["data"]["count"] == 0:
            return [{"id": False, "data": "no se encontraron resultados"}]
        else:
            for data in response_json["data"]["results"]:
                datos.append(
                    {
                        "id": data["id"],
                        "name": data["name"],
                        "image": data["thumbnail"]["path"]
                        + "."
                        + data["thumbnail"]["extension"],
                        "appearances": data["comics"]["available"],
                    }
                )
            return datos

    def buscar_comic(self, nombre):
        datos = []
        if nombre == "":
            try:
                response = requests.get(
                    "http://gateway.marvel.com/v1/public/comics?&ts=1&apikey=3e187c3b3668d0001c85763b92813a46&hash=cd5c6dff6c034615a4d1ceb8795cfe7c"
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return {"data": "hubo un error con la aplicacion"}
        else:
            try:
                response = requests.get(
                    f"http://gateway.marvel.com/v1/public/comics?title={nombre}&ts=1&apikey=3e187c3b3668d0001c85763b92813a46&hash=cd5c6dff6c034615a4d1ceb8795cfe7c"
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return {"data": "hubo un error con la aplicacion"}

        response_json = response.json()
        if response_json["data"]["count"] == 0:
            return [{"id": False, "data": "no se encontraron resultados"}]
        else:
            for data in response_json["data"]["results"]:
                datos.append(
                    {
                        "id": data["id"],
                        "title": data["title"],
                        "image": data["thumbnail"]["path"]
                        + "."
                        + data["thumbnail"]["extension"],
                        "onsaleDate": data["dates"][0]["date"],
                    }
                )
            return datos

    def run_buscador(self, categoria, nombre):
        if categoria == "personaje":
            resultado = self.buscar_personaje(nombre)
        else:
            resultado = self.buscar_comic(nombre)
        return resultado
