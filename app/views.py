from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder, db
from app.models import Publisher, Book


class BookModelView(ModelView):
    datamodel = SQLAInterface(Book)
    label_columns = {'publisher': 'Publisher'}
    list_columns = [
        'book_title', 'book_summary', 'book_avg_rating',
        'book_is_approved', 'publisher']

    show_fieldsets = [
        (
            'Main Informations',
            {'fields': ['book_cover', 'book_title', 'book_summary', 'book_avg_rating', 'publisher']}
        ),
        (
            'Details',
            {'fields': ['book_isbn', 'book_pages', 'book_publication_date', 'book_is_approved'], 'expanded': False}
        ),
    ]


class PublisherModelView(ModelView):
    datamodel = SQLAInterface(Publisher)
    related_views = [BookModelView]


db.create_all()
appbuilder.add_view(
    BookModelView,
    "Books List",
    icon="fas fa-book",
    category="Manage Books",
    category_icon="fas fa-book"
)
appbuilder.add_view(
    PublisherModelView,
    "Publishers List",
    icon="fas fa-building",
    category="Manage Books",
)
