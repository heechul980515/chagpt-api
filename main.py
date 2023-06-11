from flask import Flask, request, render_template
import openai
openai.api_key = "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"

app = Flask(__name__)


@app.route("/translater", methods=["post"])
def translater():
    data = request.json
    language = data["language"]
    text = data["text"]

    prompt = f"{text}\n\nTranslate this sentence into {language}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {
                "role": "system",
                "content": "you are a translater"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
    )
    return response["choices"][0]["message"]["content"]


@app.route("/chatbot", methods=["post"])
def chatbot():
    data = request.json
    text = data["text"]

    prompt = f"{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are a assistant"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
        temperature=2
    )
    return response["choices"][0]["message"]["content"]


@app.route("/image", methods=["post"])
def image():
    data = request.json
    text = data["text"]
    image = data["image"]

    prompt = f"{text}"
    response = openai.Image.create(
        prompt = f"{text}",
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    print(response["data"])
    print(image_url)
    return response['data'][0]['url']


@app.route("/webtranslater")
def webtranslater():
    return render_template("indextranslater.html")

@app.route("/webimage")
def webimage():
    return render_template("indeximage.html")

@app.route("/webchat")
def webchat():
    return render_template("indexchat.html")


@app.route("/chat1")
def chat1():
    return render_template("chat1.html")

@app.route("/chat2")
def chat2():
    return render_template("chat2.html")

@app.route("/")
def index():
    return render_template("home.html")


app.run(host="0.0.0.0", port=80)
