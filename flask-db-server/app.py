# import flast module
import logging
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import utils.utils
from orm.article import Article

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# instance of flask application
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

db_conn_str = 'sqlite:///translations.db'

@app.route("/", methods = ['GET'])
def ping():
  return "I am alive"
# end ping

# translate according to params in post. Returns a json
@app.route("/saveTranslation", methods = ['POST'])
def saveTranslation():
  """
  We post a json to this function and it returns a json with translated text
  Supported languages are:
    en - English
    de - German
    fr - French
    es - Spanish
  Input Json:
    fromLang : source language code
    toLang : result language code
    fromStr : String in source language
    toStr : translated string
  """

  jsonPost = getJSONFromRequest(request)
  logger.info(jsonPost)

  engine = utils.utils.create_db_engine(db_conn_str)
  db_session = utils.utils.create_db_session(engine)

  Article.saveTranslation(db_session, jsonPost)

  return jsonPost
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
  app.run(debug=True, port=5001)
