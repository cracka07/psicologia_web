
import requests

def actualizar_access_token(get_response):
    def middleware(request):
        print("MIDDLEWARE EJECUTANDOSE.....")
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
    print(middleware)
    return middleware


