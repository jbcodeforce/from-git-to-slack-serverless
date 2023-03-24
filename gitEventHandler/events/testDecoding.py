import json
import base64

f = open('encr.txt','r')
for line in f:
        bodyE=json.loads(line)
        decodedTxt=base64.b64decode(bodyE['body']).decode("utf-8")
        print(decodedTxt)
