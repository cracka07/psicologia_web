# import requests

# def actualizar_access_token(request):
#     refresh_token = "1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"
#     url = "https://oauth2.googleapis.com/token"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {
#         "grant_type": "refresh_token",
#         "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
#         "client_secret": "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",
#         "refresh_token": refresh_token
#     }

#     try:
#         response = requests.post(url, headers=headers, data=data)
#         response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
#         access_token = response.json()["access_token"]
#         request.access_token = access_token  # Almacena el access token en el objeto request para usarlo en la vista
#     except requests.exceptions.HTTPError as errh:
#         print ("Error HTTP:", errh)
#         request.access_token = None  # Si hay un error, establece el access token a None
#     except requests.exceptions.RequestException as err:
#         print ("Error en la solicitud:", err)
#         request.access_token = None  # Si hay un error, establece el access token a None

import requests

def actualizar_access_token(get_response):
    def middleware(request):
        refresh_token = "1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"
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
            access_token = response.json()["access_token"]
            request.access_token = access_token  # Almacena el access token en el objeto request para usarlo en la vista
        except requests.exceptions.HTTPError as errh:
            print ("Error HTTP:", errh)
            request.access_token = None  # Si hay un error, establece el access token a None
        except requests.exceptions.RequestException as err:
            print ("Error en la solicitud:", err)
            request.access_token = None  # Si hay un error, establece el access token a None

        response = get_response(request)

        # Código que se ejecuta después de la vista

        return response

    return middleware
