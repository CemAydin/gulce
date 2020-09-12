import json
import requests
headers = {"Authorization": "Bearer ya29.a0AfH6SMCJmHCQdVEfnpcFDDttwq4SF-h9VmmONdGIs9kyFgWaIrBkNC9W9NiWRW9c5OGPTPLF71Ksxc2SxRHSRjy3dzhVzPaxKFqL83nZR-5VXqA9MZunAJumkgHIt4_LPbOgjax5La46Ey8SH_Do9I-hSVucrjrdjUE"}
para = {
    "name": "samplefile.png",
    "parents":["1jXlIG2gXIlvMO7vDA6ck1ggetFQ6oVTV"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./Financial Sample.xlsx", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)


print(r.text)