import inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

server = ''
database = 'AdventureWorks2022'
connection_string = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'

engine = create_engine(connection_string)

# reflect the tables
Base.prepare(autoload_with=engine, schema='Production')

# mapped classes are now created with names by default
# matching that of the table name.
Product = Base.classes['Product']
# Address = Base.classes.address
# print(product)

# print class declaration
print("Class Name: ", Product.__name__)
# print("Attributes and Methods: ", inspect.getmembers(Product, lambda a:not(inspect.isroutine(a))))
print(type(Product))



# define new class to represent the Product table using SqlAlchemy ORM
# class Product(Base):
#     __tablename__ = 'Product'
#     __table_args__ = {'autoload': True}
#
#     def __repr__(self):
#         return f"<Product(ProductID='{self.ProductID}', Name='{self.Name}', ProductNumber='{self.ProductNumber}')>"
#
# # query top 10 in Product table
# session = Session(engine)
# products = session.query(Product).limit(10).all()
# for product in products:
#     print(product)