from flask import Flask, render_template,request,redirect 
from database import Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session  
app = Flask(__name__)

def getdb():
    engine=create_engine('sqlite:///project.sqlite')
    DBSession=sessionmaker(bind=engine)
    session=scoped_session(DBSession)
    return session

@app.route('/')
def about():
    return render_template('about.html',title="WebApp-About")

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        # if request.form['submit_button'] == 'Submit':
        trans_type=request.form.get('trans_type') 
        trans_amt=request.form.get('trans_amt')
        trans_nameOrig=request.form.get('trans_nameOrig')
        trans_oldbalanceOrig=request.form.get('trans_oldbalanceOrg')
        trans_newbalanceOrig=request.form.get('trans_newbalanceOrig')
        trans_nameDest=request.form.get('trans_nameDest')
        trans_oldbalanceDest=request.form.get('trans_oldbalanceOrg')
        trans_newbalanceDest=request.form.get('trans_newbalanceOrig')

        db = getdb()
        db.add(Transaction(type=trans_type, amount=trans_amt, nameOrig=trans_nameOrig, oldbalanceOrig=trans_oldbalanceOrig, newbalanceOrig=trans_newbalanceOrig, nameDest=trans_nameDest, oldbalanceDest=trans_oldbalanceDest, newbalanceDest=trans_newbalanceDest))
        db.commit()
        db.close()
        print('Data Saved Successfully')
        return redirect('/home')
    else:
        return render_template('home.html',title="WebApp-Home")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 