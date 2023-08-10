# import flast module
import logging
import os
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# instance of flask application
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route("/", methods = ['GET'])
def ping():
  return "I am alive"
# end ping

# translate according to params in post. Returns a json
@app.route("/translate", methods = ['POST'])
def translateString():
  """
  We post a json to this function and it returns a json with translated text.
  It also saves the generated translation into a db as configured through an env var
  Supported languages are:
    en - English
    de - German
    fr - French
    es - Spanish
  Input Json:
    fromLang : source language code
    toLang : result language code
    fromStr : String in source language
  :return:
  output Json:
    fromLang : source language code
    toLang : result language code
    fromStr : String in source language
    toStr : translated string
  """

  url = os.environ["MODEL_SERVER_API_URL"]
  headers = {'Content-type': 'application/json; charset=UTF-8', 'Accept':'application/json', "Access-Control-Allow-Origin": "*"}
  jsonPost = getJSONFromRequest(request)

  response = requests.post(url, json=jsonPost, headers=headers)

  return response.json()
# end translate

def getJSONFromRequest(request):
  setLogLevel()
  return request.get_json(force = True)
# end getJSONFromRequest

def setLogLevel():
  logger.setLevel(logging.WARNING)
  if "LOG_LEVEL" in os.environ:
    level = os.environ["LOG_LEVEL"]
    logLevels = {"debug": logging.DEBUG, "info": logging.INFO}
    if level in logLevels:
      loglev = logLevels[level]
      logger.setLevel(loglev)
    #end level
  #end loglevel environ if
#end setLogLevel

if __name__ == '__main__':
  app.run()
