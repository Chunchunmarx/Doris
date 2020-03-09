import Database
from Database import db
from app import app

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



with app.app_context():
    db.init_app(app)

    test_results()
    test_metadata()
