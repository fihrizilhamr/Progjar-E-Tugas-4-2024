import json
import logging
import shlex
import base64
from file_interface import FileInterface

class FileProtocol:
    def __init__(self):
        self.file = FileInterface()
        
    def proses_string(self,string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        c = shlex.split(string_datamasuk)
        try:
            c_request = c[0].strip()
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            if c_request == 'POST':
                filename=params[0]
                filedata=' '.join(params[1:])
                params=[filename, filedata]    
            cl = getattr(self.file,c_request.lower())(params)
            return json.dumps(cl)
        except Exception as e:
            return json.dumps(dict(status='ERROR', data=f'request tidak dikenali: {str(e)}'))
                                   

if __name__=='__main__':
    #contoh pemakaian
    fp = FileProtocol()