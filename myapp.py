# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
import pickle

app= Flask(__name__)
@app.route('/')
def home():
    return render_template('Main.html')

@app.route('/predict',methods=['POST'])
def predict():
    PS = PorterStemmer()
    text = request.form['Feedback']
    model = pickle.load(open('model.pkl','rb'))   
    cv = pickle.load(open('cv.pkl','rb'))
    msg = re.sub('[^a-zA-Z]',' ',text).lower().split()
    msg = [PS.stem(word) for word in msg if not word in stopwords.words('english')]
    msg = ' '.join(msg)
    x = cv.transform([msg])
    x = x.toarray()
    
    str1= str(model.predict(x))
    if str1=='[1]':
        return ('<h1>' + request.form['Name']+'!'+'<br>'+ "Thank You for liking our restaurant." + '</h1>')
    else:
        return('<h1>' + request.form['Name']+'!'+'<br>'+"We apologize that our service did not satisfy your expectations." + '</h1>')
     
 
    

if __name__ =='__main__':
    app.run(debug=True)
