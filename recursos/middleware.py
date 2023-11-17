from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Ruta al archivo JSON de la cuenta de servicio
SERVICE_ACCOUNT_FILE = 'client_secrets.json'

# Cargar las credenciales desde el archivo JSON



gauth = GoogleAuth()
gauth.service_account_file = SERVICE_ACCOUNT_FILE
drive = GoogleDrive(gauth)