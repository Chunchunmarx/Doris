from datetime import datetime
from TextEditorStatic import app, db
from TextEditorStatic.lib.flaskcode.views import resource_data
from pytz import timezone

eastern= timezone('Europe/Bucharest')



class Results(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date= db.Column(db.DateTime,nullable=False,default=datetime.now(eastern))
    test_name=db.Column(db.String(60), nullable=False,default='Test default' )
    test_result=db.Column(db.Integer,nullable=False)

    def __repr__(self):
    	return f"id('{self.id}'), date('{self.date}'), test_name('{self.test_name}'), test_result('{self.test_result}') \n"
