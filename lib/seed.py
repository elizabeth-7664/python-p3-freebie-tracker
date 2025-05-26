from models import Base, Dev, Company, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create companies
google = Company(name="Google", founding_year=1998)
amazon = Company(name="Amazon", founding_year=1994)

# Create devs
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Create freebies
f1 = Freebie(item_name="T-shirt", value=10, dev=alice, company=google)
f2 = Freebie(item_name="Sticker", value=2, dev=alice, company=amazon)
f3 = Freebie(item_name="Mug", value=8, dev=bob, company=google)

session.add_all([google, amazon, alice, bob, f1, f2, f3])
session.commit()
