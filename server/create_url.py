from urllib import request
import json
from urllib.request import urlopen
import requests

my_url = "http://food2fork.com/api/search"

##def main():
##    get_url("chicken", "511b874130772a9a0775f18fa6822b9e")
##    print("hello")
##    print(my_url)

def get_url(q, api_id):
    global my_url
    my_url += "?key=" + api_id
    my_url += "&q=" + q

#    return json.loads(urlopen(my_url, data=None, cafile=None, capath=None, cadefault=False, context=None))

#    if (sort == 'r' or sort == 't'):
#        my_url += "&sort=" + sort

#    obj_str = urlopen(my_url);
    
#    return json.loads(obj_str);

# main()

#    print(my_url)
    #return json.loads(urlopen(my_url, data=None, cafile=None, capath=None, cadefault=False, context=None))
    return requests.get(my_url)
#main()

