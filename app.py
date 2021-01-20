from flask import Flask, render_template, request
import chatMain
import uuid
import sqlite3
app = Flask(__name__)
app.static_folder = 'static'
conn = sqlite3.connect('database/sorular.sqlite', check_same_thread=False)
c = conn.cursor()
my_id = uuid.uuid4()

# conda activate chatBot
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")  # post
def get_bot_response():
    userText = request.args.get('msg')
    cevap = chatMain.chat(userText)[0]
    tag = chatMain.chat(userText)[1]

    veritabanıKayit(tag, userText, cevap)
    print(chatMain.chat(userText)[0])
    return (cevap)

def veritabanıKayit(tag, soru, cevap):
    c.execute("INSERT INTO sorular VALUES(?,?,?,?,?)", (str(my_id), tag, soru, cevap, " "))
    conn.commit()
if __name__ == "__main__":
    app.run(debug=False)