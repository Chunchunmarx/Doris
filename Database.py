from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
from pytz import timezone

eastern = timezone('Europe/Bucharest')

db = SQLAlchemy()



class DatabaseResults(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    date= db.Column(db.DateTime,nullable=False,default=datetime.now(eastern))
    test_name=db.Column(db.String(60), nullable=False,default='Test default' )
    test_result=db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"id('{self.id}'), date('{self.date}'), test_name('{self.test_name}'), test_result('{self.test_result}') \n"

class DatabaseResultsHandler:
    @staticmethod
    def get_entries():
        return DatabaseResults.query.order_by(desc(DatabaseResults.date)).all()

    @staticmethod
    def add(test_name, test_result):
        db.session.add(DatabaseResults(test_result=test_result, test_name=test_name))
        db.session.commit()

    @staticmethod
    def print():
        entries = DatabaseResultsHandler.get_entries()
        for entry in entries:
            print(entry)

# ========================================================================================
class DatabaseMetadata(db.Model):
    __bind_key__ = 'sql_metadata'
    db_testname = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    db_author = db.Column(db.String(80), unique=True, nullable=False, primary_key=False)
    db_trs = db.Column(db.String(80), unique=True, nullable=False, primary_key=False)

    def __repr__(self):
        return '<Test {0} - made by {1} for TRS {2}>'.format(self.db_testname, self.db_author, self.db_trs)


class DatabaseMetadataHandler:

    @staticmethod
    def get_entries():
        return DatabaseMetadata.query.all()

    @staticmethod
    def add(testname, author, trs):
        db.session.add(DatabaseMetadata(db_testname=testname, db_author=author, db_trs=trs))
        db.session.commit()

    @staticmethod
    def print():
        entries = DatabaseMetadataHandler.get_entries()
        for entry in entries:
            print(entry)