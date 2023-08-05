# import flast module
import logging
import os

from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import tensorflow

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger()

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# instance of flask application
app = Flask(__name__)

model_id="google/flan-t5-large"

model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

@app.route("/", methods = ['GET'])
def ping():
  return "I am alive"
# end ping

@app.route("/test", methods = ['POST'])
def test():
  return "i got post"

# translate according to params in post. Returns a json
@app.route("/translate", methods = ['POST'])
def translateString():
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
  :return:
  output Json:
    fromLang : source language code
    toLang : result language code
    fromStr : String in source language
    toStr : translated string
  """

  RK_FROM_LANG = 'fromLang'
  RK_TO_LANG = 'toLang'
  RK_FROM_STR = 'fromStr'
  RK_TO_STR = 'toStr'

  langMap = {"en" : "English", "de" : "German", "fr" : "French", "es" : "Spanish"}

  jsonPost = getJSONFromRequest(request)
  logger.info(jsonPost)
  print(jsonPost)

  fromLang = jsonPost[RK_FROM_LANG]
  fromStr = jsonPost[RK_FROM_STR]
  toLang = jsonPost[RK_TO_LANG]

  str = f"translate {langMap[fromLang]} to {langMap[toLang]}: {fromStr}"
  inputs = tokenizer(str, return_tensors="pt")
  outputs = model.generate(inputs.input_ids, max_new_tokens=10000)
  jsonPost[RK_TO_STR] = tokenizer.decode(outputs[0], skip_special_tokens=True)

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
  app.run()
