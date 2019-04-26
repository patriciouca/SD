

import dropbox
import tempfile

def SubirDropbox(subida){

file_from='FicheroNombre'


dbx = dropbox.Dropbox('Token aquí')
#subir archivos
dbx.files_upload(open(file_from, 'rb').read(),subida)

}

def DescargarDropbox(subida){
# Autenticación
token = "INTRODUCIR TOKEN GENERADO"
dbx = dropbox.Dropbox(token)

# Obtiene y muestra la información del usuario
user = dbx.users_get_current_account()
print(user)

# Descarga archivo
dbx.files_download_to_file(subida, '/nombre.txt')
}