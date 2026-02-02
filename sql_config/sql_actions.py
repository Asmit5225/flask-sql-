from app import db, Todo

class Todo(db.Model):#here we created a table and assigned it's rowns and columns in my asmit.db database
    slno= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    decs=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return f"{self.slno}-{self.title}"


def INSERT_INTO_TABLE(title, desc):
    todo = Todo(title=title, decs=desc)
    db.session.add(todo)
    db.session.commit()