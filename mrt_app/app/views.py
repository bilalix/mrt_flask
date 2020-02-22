from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, has_access

from . import appbuilder, db

from flask_appbuilder import AppBuilder, expose, BaseView


class MyBooks(BaseView):
    # route_base = "/mybooks"
    default_view = 'fetch_all_books'

    @expose('/fetch_all_books')
    @has_access
    def fetch_all_books(self):
        return "Fetched all books"

    @expose('/fetch_book/<int:isbn>')
    @has_access
    def fetch_book(self, isbn):
        return "Fetched book with isbn: " + str(isbn)


appbuilder.add_view(MyBooks, "All My Books", category='My Books')
appbuilder.add_link("Fetch a book", href='/mybooks/fetch_book/684531', category='My Books')

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
