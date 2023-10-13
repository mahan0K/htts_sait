from flask import Flask  # объект 


app = Flask(__name__)

@app.route("/") # GET - по умолчанию
def main ():
    return "<h1>Егор, послушай свой голос он тебе говорит не останавливайся работай твои знания твоя сила иди вперёд  неостанавливаййся ! </h1>"


@app.route("/info") # GET - по умолчанию
def info ():
    return "<h1>Меня создал человек которому всё по силам ! Его зовут Егор </h1>"


@app.route("/summa/<x>/<y>") # GET - по умолчанию
def summa (x,y):
    return f"<h1>{x} + {y} = {int(x) + int(y)}</h1>"


if __name__ == "__main__":
    app.run()




