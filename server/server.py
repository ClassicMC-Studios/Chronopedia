import os
import json
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
from model import Model
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="provider",
    api_key="key",
)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
last_output = "None"
llm_model = Model()


@app.post("/post")
def handle_post():
    global last_output
    settings = request.get_json()  # Gets post values (This will throw an error if not in json)
    print(settings["content"])
    print(settings["year"])
    print(settings["lang"])  # Prints post
    # Runs model with updated settings
    last_output = llm_model.get_output(settings["content"], settings["year"], settings["lang"])
    return json.dumps(last_output)  # Should update settings, run model, return model output, and save model output


@app.get("/get")
def handle_get():
    global last_output
    return last_output  # Should last model output


@app.get("/audio")
def audio():
    if os.path.exists("audio_file/hello.mp3"):
        return send_file("audio_file/hello.mp3", download_name="hello.mp3")
    else:
        print("????")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

