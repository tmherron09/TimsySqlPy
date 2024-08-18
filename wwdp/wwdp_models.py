from sqlalchemy import String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine, select
from pprint import pprint

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = "investment"
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))





if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    bitcoin = Investment(coin='Bitcoin', currency='USD', amount=1.0)

    with Session(engine) as session:
        session.add(bitcoin)
        session.commit()

    # stmt = select(Investment).where(Investment.coin.__eq__('Bitcoin'))
    # stmt = select(Investment).where(Investment.coin.is_('Bitcoin'))# == 'Bitcoin')
    stmt = select(Investment).where(Investment.amount.is_(1.0))# == 'Bitcoin')
    bitcoin = session.execute(stmt).scalar_one()
    pprint(bitcoin.id)
    pprint(bitcoin.coin)
    pprint(bitcoin.currency)
    pprint(bitcoin.amount)
