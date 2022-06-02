from flask import Flask,render_template, request
import numpy as np
import pickle

model2=pickle.load(open('rl_vive.pkl','rb'))

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7])
    pred = model2.predict([features])
    
    def statement():
        if pred == 0:
            return 'Resultado:- El modelo ha pronosticado que los síntomas descritos no ponen en riesgo su vida pero debe cuidarse.'
        elif pred == 1:
            return 'Resultado:-  Debe consultar con el médico, el modelo ha predicho que sus síntomas ponen en riesgo su vida.'
    
    return render_template('new.html',statement=statement())


if __name__=='__main__':
    app.run()