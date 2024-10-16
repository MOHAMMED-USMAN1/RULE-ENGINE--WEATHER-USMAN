# database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule_string = Column(String)
    ast = Column(String)  # Store AST as a JSON-encoded string

# Database connection
engine = create_engine('sqlite:///rules.db')
Session = sessionmaker(bind=engine)
session = Session()

def store_rule(rule_string, ast):
    rule = Rule(rule_string=rule_string, ast=ast)
    session.add(rule)
    session.commit()
