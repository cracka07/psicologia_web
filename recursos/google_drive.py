import json
import requests
import pprint

def obtener_access_token(refresh_token):
    refresh_token="1//06cJxoiclJv6PCgYIARAAGAYSNwF-L9IrrqEvW_ywinYJbKtVoylSkMxnPWzRzZpnYG9RM3b9HhgItjPSXGiOif6Grqs1oWpz3XU"
    url = "https://oauth2.googleapis.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "client_id": "551019562811-u3tcv1mlj69f53kq0017rcpqtluk5ih6.apps.googleusercontent.com",  # Reemplaza con tu client ID
        "client_secret": "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",  # Reemplaza con tu client secret
        "refresh_token": refresh_token
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def obtener_subcarpetas(folder_id, access_token):
    url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    contenido = response.json()
    files=contenido["files"]
    for n in files:
        pprint.pprint(n["name"])
    return contenido

refresh_token = "1//06cJxoiclJv6PCgYIARAAGAYSNwF-L9IrrqEvW_ywinYJbKtVoylSkMxnPWzRzZpnYG9RM3b9HhgItjPSXGiOif6Grqs1oWpz3XU"  # Reemplaza con tu refresh token
access_token = obtener_access_token(refresh_token)
folder_id = "1P8OOHEBpi5B2WkbhFqJ0tb35kN6WSbHt"

subcarpetas = obtener_subcarpetas(folder_id, access_token)

