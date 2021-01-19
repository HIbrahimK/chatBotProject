from flask import Flask, render_template, request
app = Flask(__name__)
app.static_folder = 'static'

# conda activate chatBot
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")  # post
def get_bot_response():
    userText = request.args.get('msg')
   # cevap = chatMain.chat(userText)[0]
    #tag = chatMain.chat(userText)[1]

    #veritabanıKayit(tag, userText, cevap)
    # print(chatMain.chat(userText)[0])
    return (userText)
if __name__ == "__main__":
    app.run(debug=False)