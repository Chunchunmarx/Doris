from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from TextEditorStatic import app, db
from flask_login import UserMixin



class Results(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date= db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    test_name=db.Column(db.String(60), nullable=False,default='Test default' )
    test_result=db.Column(db.String(60),nullable=False)
