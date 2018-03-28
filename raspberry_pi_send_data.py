import requests
import pprint
import json
import subprocess

endpoint = 'http://35.229.175.184/predict'
filename = './waves.mp3'

def send_raw(wav):
    files = {'file': open(wav,'rb')}
    r = requests.post(endpoint, files=files)

    print('Response for file upload')
    print('Status: '+str(r))
    # print(r.content)
    pprint.pprint(json.loads(r.content))
    print('Time elapsed: ' + str(r.elapsed))


send_raw(filename)

# while (True):
#     p = subprocess.run(["arecord", "sample.wav", "-d", "5"], input=stdin, stdout=subprocess.PIPE, universal_newlines=True)
#     out = p.stdout.strip()
#     err = p.stderr
#     if stdin == out:
#         print('OK')
#     else:
#         print('failed: ' + out)
#         print('error: ' + err)
