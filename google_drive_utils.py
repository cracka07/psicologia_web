from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()

# Cargar las credenciales desde el archivo credentials_module.json
gauth.LoadCredentialsFile("./credentials_module.json")

# Si no hay credenciales o si el token de acceso ha caducado, solicitar nuevas credenciales
if gauth.credentials is None or gauth.access_token_expired:
    # Iniciar sesión y obtener nuevas credenciales
    gauth.LocalWebserverAuth()

# Inicializar el objeto GoogleDrive con las credenciales cargadas o recién adquiridas
drive = GoogleDrive(gauth)
