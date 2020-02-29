from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, Boolean, Date
from sqlalchemy.orm import relationship, backref

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Publisher(Model):
    __tablename__ = 'publisher'

    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String(60), nullable=False)

    def __repr__(self):
        return self.publisher_name

class Book(Model):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    book_isbn = Column(String(255), nullable=False, unique=True)
    book_cover = Column(String(255), nullable=False)
    book_title = Column(String(255), nullable=False)
    book_pages = Column(Integer)
    book_summary = Column(Text)
    book_avg_rating = Column(Float)
    book_publication_date = Column(Date)
    book_is_approved = Column(Boolean, default=False)
    publisher_id = Column(
        Integer,
        ForeignKey(
            # _constraint='books_publisher_id_fk',
            # column='publisher.publisher_id',
            'publisher.publisher_id'
            # ondelete='RESTRICT',
            # onupdate='RESTRICT'
        )
    )
    publisher = relationship("Publisher")

    def __repr__(self):
        return self.book_title

