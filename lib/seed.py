#!/usr/bin/env python3
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()

    fake = Faker()
    
    company_1 = Company(name='Google', founding_year=1998)
    company_2 = Company(name='Apple', founding_year=1976)
    company_3 = Company(name='Facebook', founding_year=2004)
    session.add(company_1)
    session.add(company_2)
    session.add(company_3)
    session.commit()

    dev_1 = Dev(name='Alice')
    dev_2 = Dev(name='Bob')
    dev_3 = Dev(name='Charli')
    session.add(dev_1)
    session.add(dev_2)
    session.add(dev_3)
    session.commit()

    freebie_1 = Freebie(item_name = 'T-shirt', value = 15, company_id = company_1.id, dev_id = dev_1.id)
    freebie_2 = Freebie(item_name = 'Mug', value = 10, company_id = company_2.id, dev_id = dev_2.id)
    freebie_3 = Freebie(item_name = 'Sticker', value = 5, company_id = company_3.id, dev_id = dev_3.id)
    session.add(freebie_1)
    session.add(freebie_2)
    session.add(freebie_3)
    session.commit()