from flask import Flask , render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///asmit.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
from sql_config.sql_actions import INSERT_INTO_TABLE


@app.route("/", methods=['GET','POST'])  #now we have inserted values in my table Todo tarpor oi database er sob kota query er value gulo ke tule ami alltodo variable a store kore html a pass kore dilam 
def hello_world():
    if request.method=='POST':
        Title=request.form["title"]
        desc=request.form["desc"]
        INSERT_INTO_TABLE(Title, desc)
    #todo= Todo(title="first todo", decs="start investing in stock market")
    #chips=Todo(title="second todo", decs="start investing in stock market")
    #protein=Todo(title="third todo", decs="start investing in stock market")
    #db.session.add(todo)
    #db.session.add(chips)
    #db.session.add(protein)
    #db.session.commit()
    alltodo= Todo.query.all()
    return render_template('asmit.html', alltodo=alltodo)
    #return "<p>Hello, World!</p>"

@app.route("/show")
def product():
    alltodo= Todo.query.all()
    print(alltodo)
    return "wassshuppppp.......?!"

@app.route("/Delete/<int:slno>")
def delete(slno):
    todo= Todo.query.filter_by(slno=slno).first()
    db.session.delete(todo)
    db.session.commit() 
    return redirect("/")




if __name__== "__main__":
    app.run(debug=True)