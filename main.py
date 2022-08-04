# import requests module
import requests

import json

import logging

from time import time, sleep

# Create and configure logger
logging.basicConfig(filename="log.txt",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Making a get request
#response = requests.get('https://api-shipx-pl.easypack24.net/')

try:
    response = requests.get('https://api-shipx-pl.easypack24.net/')
    # command line arguments
    #host = sys.argv[0]
    #response=requests.get(host)



    logger.debug("1. Wysyłał żądanie GET na zadany host")
    #logger.info(response.elapsed.total_seconds())

except requests.ConnectionError:
    print("failed to connect")
    logger.info("failed to connect")

# print response
print(response)


try:
    print(response.elapsed.total_seconds())
    logger.debug("2. Mierzył czas od wysłania żądania do czasu otrzymania odpowiedzi")
    logger.info(response.elapsed.total_seconds())

except requests.ConnectionError:
    print("failed to elapsed.total_seconds.Connection")
    logger.info("failed to elapsed.total_seconds.Connection")

# print request status_code
try:
    #response = requests.get('http://api.nbp.pl/')
    #response=requests.head("http://api.nbp.pl/")
    print(response.status_code)

    logger.debug("3. Sprawdzał kod odpowiedzi HTTP")
    logger.info(response.status_code)

except requests.ConnectionError:
    print("failed to connect")
    logger.info("failed to connect")

#resp_content = response.content
#resp_content=response.headers.get('content-type')
#print(resp_content)


try:
    #response = requests.get(' https://api-shipx-pl.easypack24.net')
    resp_content = response.headers.get('content-type')
    print(resp_content)

    logger.debug("4. Sprawdzał czy odpowiedź to JSON")
    logger.info(resp_content)

except ValueError:
    resp_content = response.content


try:
    #response = requests.get(' https://api-shipx-pl.easypack24.net')
    resp_content = response.json()
    print(resp_content)

    logger.debug("5. Walidował czy JSON z odpowiedzi ma prawidłową składnię")
    logger.info(resp_content)

except ValueError:
    resp_content = response.content
    print(resp_content)


#Wykonywał X sprawdzeń, co Y sekund.

n = 4
# command line arguments
#n = sys.argv[1]

c = 6
#host = sys.argv[2]

for i in range(0, n):
    print(i)
    # response=requests.get(host)
    sleep(c - time() % c)




try:
    #response = requests.get(' https://api-shipx-pl.easypack24.net')
    resp_content = response.content
    my=json.loads(resp_content)
    print(my)
except ValueError:
    resp_content = response.content
    print(resp_content)