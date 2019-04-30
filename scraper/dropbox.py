

import dropbox
import tempfile

def SubirDropbox(subida):
    file_from ='datos/datos.csv'
    file_to = '/datos/'+subida
    print(file_to)
    dbx = dropbox.Dropbox('c_uLk304JZAAAAAAAAAAGmBbP1ofQmaY52zRtIm7z8_p3NT-1hRwx-ZV3E_DlPeo')
    print(file_to)
    dbx.files_upload(open(file_from, 'rb').read(),file_to, mode=dropbox.files.WriteMode.overwrite)



def DescargarDropbox(subida):
    dbx = dropbox.Dropbox('c_uLk304JZAAAAAAAAAAGmBbP1ofQmaY52zRtIm7z8_p3NT-1hRwx-ZV3E_DlPeo')
    try:
        metadata, f = dbx.files_download(subida)
        out = open('datos/datos.csv', 'wb')
        out.write(f.content)
        out.close()
        return 1
    except:
        print("No se ha podido descargar")
        return 0


