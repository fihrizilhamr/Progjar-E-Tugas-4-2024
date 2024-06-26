import os
import json
import base64
from glob import glob

class FileInterface:
    def __init__(self):
        if not os.path.exists('files/'):
            os.makedirs('files/')
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if filename == '':
                return None
            with open(filename, 'rb') as fp:
                isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def post(self, params=[]):
        try:
            filename = params[0]
            filedata = params[1]
            decoded_data = base64.b64decode(filedata)
            
            if os.path.exists(filename):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(f"{base}({counter}){ext}"):
                    counter += 1
                filename = f"{base}({counter}){ext}"
                
            with open(filename, 'wb') as fp:
                fp.write(decoded_data)

            return dict(status='OK', data=filename)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def delete(self, params=[]):
        try:
            filename = params[0]
            if os.path.exists(filename):
                os.remove(filename)
                return dict(status='OK', data_namafile=filename)
            else:
                return dict(status='ERROR', data='File not found')
        except Exception as e:
            return dict(status='ERROR', data=str(e))

if __name__ == '__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
