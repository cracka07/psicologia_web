
# import requests

# def actualizar_access_token(get_response):
#     def middleware(request):
#         if hasattr(request, 'access_token') and request.access_token is not None:
#             # Verificar si el access token ha expirado
#             url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
#             params = {"access_token": request.access_token}
#             response = requests.get(url, params=params)

#             if response.status_code == 200:
#                 token_info = response.json()
#                 if 'error_description' in token_info:
#                     print("Error al verificar el token:", token_info['error_description'])
#                 else:
#                     # Token válido, continuar con la solicitud
#                     return get_response(request)
#             else:
#                 print("Error al verificar el token. Código de estado:", response.status_code)

#         # Si el access token no es válido o ha expirado, obtener uno nuevo
#         refresh_token = "1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"  # Asegúrate de tener el refresh token actualizado
#         # Resto del código para obtener un nuevo access_token...

#         url = "https://oauth2.googleapis.com/token"
#         headers = {
#             "Content-Type": "application/x-www-form-urlencoded"
#         }
#         data = {
#         "grant_type": "refresh_token",
#         "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
#         "client_secret": "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",
#         "refresh_token": refresh_token
#     }
#         try:
#             response = requests.post(url, headers=headers, data=data)
#             response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
#             access_token = response.json()["access_token"]
#             request.access_token = access_token  # Almacena el access token en el objeto request para usarlo en la vista
#             print("¡Se ha renovado el token con éxito!")
#         except requests.exceptions.HTTPError as errh:
#             print ("Error HTTP:", errh)
#             request.access_token = None  # Si hay un error, establece el access token a None
#         except requests.exceptions.RequestException as err:
#             print ("Error en la solicitud:", err)
#             request.access_token = None  # Si hay un error, establece el access token a None

#         return get_response(request)
#     return middleware
import requests

def actualizar_access_token(get_response):
    def middleware(request):
        if hasattr(request, 'access_token') and request.access_token is not None:
            # Verificar si el access token está a punto de expirar
            expiration_time = request.token_info.get('expires_in')
            if expiration_time is not None and expiration_time < 300:  # Renovar si quedan menos de 5 minutos
                try:
                    response = requests.post(
                        "https://oauth2.googleapis.com/token",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data={
                            "grant_type": "refresh_token",
                            "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
                            "client_secret": "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",
                            "refresh_token": "1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"
                        }
                    )
                    response.raise_for_status()
                    access_token = response.json()["access_token"]
                    request.access_token = access_token
                    print("¡Token renovado con éxito!")
                except requests.exceptions.HTTPError as errh:
                    print("Error HTTP al renovar el token:", errh)
                except requests.exceptions.RequestException as err:
                    print("Error en la solicitud al renovar el token:", err)

        return get_response(request)

    return middleware
