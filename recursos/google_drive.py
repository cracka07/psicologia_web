import json
import pprint
import requests


def obtener_access_token(refresh_token):
    url = "https://oauth2.googleapis.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
        "client_secret": "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",
        "refresh_token": refresh_token
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        return response.json()["access_token"]
    except requests.exceptions.HTTPError as errh:
        print ("Error HTTP:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error de conexión:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout de la solicitud:",errt)
    except requests.exceptions.RequestException as err:
        print ("Error en la solicitud:",err)

def obtener_subcarpetas(folder_id, access_token):
    url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        contenido = response.json()
        files = contenido["files"]
        for n in files:
            pprint.pprint(n["name"])
        return contenido
    except requests.exceptions.HTTPError as errh:
        print ("Error HTTP:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error de conexión:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout de la solicitud:",errt)
    except requests.exceptions.RequestException as err:
        print ("Error en la solicitud:",err)

refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"
access_token = obtener_access_token(refresh_token)


folder_id = "1axJ3Yb0BrgJ7YKCp34K8peSE_HuV_6AE"
subcarpetas = obtener_subcarpetas(folder_id, access_token)
