import json
import os
import glob
import shutil

try:
    os.mkdir("./processed")
except OSError:
    print('"processed" directory have been already created.')

receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')
    './new/receipt-1.json'.split()
