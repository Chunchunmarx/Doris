import Database
from Database import db
from Database import DatabaseResults
from app import app
import datetime

now = datetime.datetime.now()

def test_results():
    Database.DatabaseResultsHandler.add("001", "Success - 001")
    Database.DatabaseResultsHandler.add("002", "Success - 002")
    Database.DatabaseResultsHandler.add("003", "Failed - 003")
    Database.DatabaseResultsHandler.add("004", "Success - 004")

    Database.DatabaseResultsHandler.print()

# ======================================================

def test_metadata():
    Database.DatabaseMetadataHandler.add("test 001", "some_author", "trs 1")
    Database.DatabaseMetadataHandler.add("test 002", "another author", "trs 2")
    Database.DatabaseMetadataHandler.add("test 003", "third author", "trs 3")
    Database.DatabaseMetadataHandler.add("test 004", "tbd", "trs 4")

    Database.DatabaseMetadataHandler.print()

# ======================================================

def test_query():
    print(Database.DatabaseResults.query.filter(DatabaseResults.test_result.like('Success%')).all())

# ======================================================

def test_filter():
    #Database.DatabaseResultsHandler.filter('date','2020-03-17')
    success_list = Database.DatabaseResultsHandler.filter('test_result','Success')
    fail_list = Database.DatabaseResultsHandler.filter('test_result','Failed')
    print(len(success_list))
    print(len(fail_list))

# ======================================================

def test_ultra_filter():
    columns = ['date', 'test_result'] 
    values = [ '2020-03-23', 'Failed']
    print(Database.DatabaseResultsHandler.filter(columns, values))

# ======================================================

with app.app_context():
    db.init_app(app)
   
    test_results()
    #test_metadata()
    #test_query()
    #test_filter()
    #session.query(Customer).filter(Customer.first_name == 'Carl').all()
    #test_ultra_filter()
    #print (now.strftime("%Y-%m-%d"))

