import time
import os
import json
from products import json_updater

def exec():
    while True:
        json_ls = os.listdir("../json_files")
        username_ls = [i[:-5] for i in json_ls]
        json_ls = [str("../json_files/")+i for i in json_ls]
        print(json_ls)

        for i in range(len(json_ls)):
            with open(json_ls[i],'r') as json_obj:
                json_obj = json.load(json_obj)
                print(json_obj)
                json_updater.json_update(username=username_ls[i], url=json_obj["query"])
        time.sleep(1000)

exec()
