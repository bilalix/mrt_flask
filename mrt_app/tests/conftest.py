import pytest
from flask import Flask
from flask_appbuilder import AppBuilder

from app import db
from app.models import Publisher


@pytest.fixture(scope='module')
def create_db():
    return db


@pytest.fixture(scope='module')
def test_client():
    flask_app = Flask(__name__)
    flask_app.config.from_object("config")
    appbuilder = AppBuilder(flask_app, db.session)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    # this is where the testing happens!
    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert data
    pub1 = Publisher()
    pub1.publisher_name = 'Free Press'
    db.session.add(pub1)

    # Commit the changes
    db.session.commit()

    # this is where the testing happens!
    yield db

    db.drop_all()
