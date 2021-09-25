# created virtual enviorment
# virtualenv newsapp
#! source newsapp/scripts/activate
# pip install pandas numpy sklearn flask gunicorn(for deployment)

# from itertools import Predicate

from flask import Flask, escape, request, render_template
import pickle

vector=pickle.load(open("vectorizer.pkl", 'rb'))

# model name , mode for opening (read binary)
model=pickle.load(open("finalized_model.pkl", 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news= request.form['news']

        predict = model.predict(vector.transform([news]))[0] # get 0th element
        print(predict)

        return render_template("prediction.html", prediction_text="News Headline is -> {}".format(predict))
    else:
        return render_template("prediction.html")

if __name__ == '__main__':
    app.run()