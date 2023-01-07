'''
Receipt Scanner Functionality using Asprise OCR API
'''

import requests as rq    # pip3 install requests
import json
import pickle

url = "https://ocr.asprise.com/api/v1/receipt"
receipts = "figure1.jpg"

res = rq.post(url, 
                data = {'api_key': 'TEST', 'recognizer': 'auto', 'ref_no': 'oct_python_123'},
                files = {'file': open(receipts, 'rb')})

with open("output1.json", "w") as f:
    json.dump(json.loads(res.text), f)