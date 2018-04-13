import requests
import pprint
import json
import subprocess
import time

endpoint = 'http://35.229.175.184/predict'
filename = 'sample.wav'

def send_raw(wav):
    files = {'file': open(wav,'rb')}
    r = requests.post(endpoint, files=files)

    print('Response for file upload')
    print('Status: '+str(r))
    # print(r.content)
    pprint.pprint(json.loads(r.content))
    print('API Time elapsed: ' + str(r.elapsed))


#send_raw(filename)

while (True):
    start_time = time.time()
    #p = subprocess.run(["arecord", "sample.wav", "-d", "5"], input=stdin, stdout=subprocess.PIPE, universal_newlines=True)
    p = subprocess.run(["arecord", filename, "-d", "3", "-r", "22050", "-f", "S16_LE"])
    #out = p.stdout.strip()
    #err = p.stderr
    #if stdin == out:
    #    print('OK')
    #else:
    #    print('failed: ' + out)
    #    print('error: ' + err)
    print('subprocess: ')
    print(p)

    send_raw(filename)
    print("Total time: %s seconds"%(time.time()-start_time))
    print('sleep for 5 seconds')
    time.sleep(5)
    print()
