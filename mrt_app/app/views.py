from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, has_access

from . import appbuilder, db

from flask_appbuilder import AppBuilder, expose, BaseView

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm
from flask import flash
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _


class ContactUsForm(DynamicForm):
    title = StringField('Title',
                        description="Reason why you're contacting us!",
                        validators=[DataRequired()], widget=BS3TextFieldWidget())
    description = StringField('Description',
                              description='Your message...', widget=BS3TextFieldWidget())


class ContactUsFormView(SimpleFormView):
    form = ContactUsForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    def form_get(self, form):
        form.title.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')


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

    @expose('goodBye/<string:username>')
    @has_access
    def good_bye(self, username):
        msg = "Good Bye " + username + " !"
        self.update_redirect()
        return self.render_template('good_bye.html', message=msg)


appbuilder.add_view(MyBooks, "All My Books", category='My Books')
appbuilder.add_link("Fetch a book", href='/mybooks/fetch_book/684531', category='My Books')
appbuilder.add_link("Good bye", href='/mybooks/goodBye/Bilal', category='My Books')
appbuilder.add_view(ContactUsFormView, "Contact Us", icon="far fa-question-circle", label=_('Contact Us'),
                    category="Help", category_icon="far fa-question-circle")


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
