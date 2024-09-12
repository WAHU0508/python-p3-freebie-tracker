from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

company_dev = Table(
    'company_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref=backref('company'))
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')
    
    def give_freebie(self, dev, item_name, value):
        if isinstance(dev, Dev):
            freebie = Freebie(item_name = item_name, value = value, company_id = self.id, dev_id = dev.id)
            session.add(freebie)
            session.commit()
    @classmethod        
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()
    
    def __repr__(self):
        return f'Company(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'founding_year={self.founding_year})'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    
    freebies = relationship('Freebie', backref=backref('dev'))
    companies = relationship('Company', secondary=company_dev, back_populates='devs')
    
    def received_one(self, item_name):
        freebies = [freebie for freebie in self.freebies if freebie.item_name == item_name]
        if freebies:
            return True
        else:
            return False
        
    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev
            session.commit()
            
    def __repr__(self):
        return f'Dev(id={self.id}, ' + \
            f'name={self.name})'
    
class Freebie(Base):
    __tablename__ = 'freebies'
    
    id = Column(Integer, primary_key = True)
    item_name = Column(String)
    value = Column(Integer)
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))


    def __repr__(self):
        return f'Freebie(id={self.id}, ' + \
            f'item_name={self.item_name}, ' + \
            f'value={self.value})'
    
    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
    