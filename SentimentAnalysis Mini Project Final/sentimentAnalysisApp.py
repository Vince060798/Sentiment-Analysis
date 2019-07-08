from flask import Flask,render_template,request
import os
from textblob import TextBlob
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    result = ''
    if request.method=='POST':
        sentence = request.form.get('sentence')
        #print(sentence)
        testimonial = TextBlob(sentence)
        
        polarity = testimonial.sentiment.polarity
        if polarity == 0:
            result = 'Neutral'
        elif polarity <= 0:
            result = 'Negative'
        elif polarity >= 0:
            result = 'Positive'
        #print(result)
        return render_template('latest.html',result=result,pol=polarity)
    return render_template('latest.html')

if __name__ == "__main__":
    app.run(debug=True)