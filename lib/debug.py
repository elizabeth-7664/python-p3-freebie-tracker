#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # ✅ Add test data if not already present
    if not session.query(Company).first():
        company = Company(name="OpenAI", founding_year=2015)
        dev = Dev(name="Alice")
        freebie = Freebie(item_name="T-Shirt", value=20, company=company, dev=dev)

        session.add_all([company, dev, freebie])
        session.commit()

    import ipdb; ipdb.set_trace()

    try:
        c = session.query(Company).first()
        print("Company:", c)
        print("Freebies:", c.freebies)
        print("Developers:", c.devs)
    except Exception as e:
        print("Error:", e)
        import ipdb; ipdb.set_trace()
