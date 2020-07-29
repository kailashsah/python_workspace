

try:
    import os
    from flask.app import Flask
    from flask_sqlalchemy import SQLAlchemy
except:
    print("No modules found")
    
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, "temp.sql")

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __rpsr__(self):
        return "Name : {},, age : {}".format(name, age)
        
    
def CreateDatabse():
    db.drop_all()
    db.create_all()
    
    amit = Person("amit", 24)
    vivek = Person("vivek", 30)

    db.session.add(amit)
    db.session.add (vivek)
    
    db.session.commit()

def QueryDb():
    data = Person.query.all()
    k = 0
    for i in data:
        
#         print(Person.query.get(k+1).name)
        print(data[k].name) # print(i.name)        
        print(data[k].age)
        k += 1

    data4 = Person.query.with_entities(Person.name).filter_by(age=24)
    print(data4.all())

if __name__ == '__main__':
#     CreateDatabse()
    QueryDb()