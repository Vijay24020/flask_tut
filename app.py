from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    # values = [int(x) for x in request.form.values()]  #
    ram = int(request.form.get("ram"))
    rom = int(request.form.get("rom"))
    ss = float(request.form.get("size"))
    bc = int(request.form.get("back"))
    fc = int(request.form.get("front"))
    battery = int(request.form.get("battery"))
    values=[ram,rom,ss,bc,fc,battery]
    final = np.array(values)
    prediction = model.predict(final.reshape(1,-1))
    output=prediction[0]
    return render_template('index.html',sent_value = f"Expected price of the Phone is {output}")
        #use of fstring or Formatted string

if __name__=="__main__":
    app.run(debug=True)