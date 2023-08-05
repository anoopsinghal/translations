# import flast module
from flask import Flask
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import tensorflow

# instance of flask application
app = Flask(__name__)

model_id="google/flan-t5-large"

model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# home route that returns below text when root url is accessed
@app.route("/")
def translate():
    str = "translate English to German: The house is wonderful."
    inputs = tokenizer(str, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_new_tokens=10000)

    str = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return str

if __name__ == '__main__':
    app.run()
