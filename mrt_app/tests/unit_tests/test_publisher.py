import pytest
import sys
sys.path.append("../..")
from app.models import Publisher


@pytest.fixture(scope='module')
def new_publisher():
    new_publisher = Publisher()
    new_publisher.name = 'PublisherOne'
    return new_publisher


def test_new_publisher(new_publisher):
    """
    GIVEN a Publisher model
    WHEN a new Publisher is created
    THEN check if the pulisher_name field is defined correctly
    """
    assert new_publisher.name == 'PublisherOne'
