import datetime


import berserk
import os

from market import db
from market.models import Item, User, bcrypt
from tools import time


def show():
    for item in Item.query.all():
        print("id: ", item.id)
        print("price: ", item.price)
        print("name: ", item.name)
        print("description: ", item.description)


def add(id_api, name):
    item1 = Item(id_api=id_api, name=name, price=100000000, barcode="11",
                 description="Proszę nie dołączać do tego turnieju")

    db.session.add(item1)
    db.session.commit()


def berserk_start():
    session = berserk.TokenSession(os.environ["OAuth2"])
    client = berserk.Client(session=session)
    return client


def add_turniej():
    client = berserk_start()

    data = client.tournaments.create(5, 0, 45)

    print(data["id"])

    add(data["id"], "test")


def get_turniej(id_api):
    client = berserk_start()

    print(client.tournaments.export_games(id_api))


def if_start():
    client = berserk_start()

    data = client.tournaments.create(5, 0, 45)

    time = data["startsAt"]

    add(data["id"])

    print(time.tzname())


def test():
    time = datetime.datetime(2021, 12, 6, 13, 30, 6, 4144, tzinfo="UTC")
    # test = time > database_time

    database_time = datetime.time()

    print(time.time())
    print(database_time)

    print(test)

    print(database_time)


def delete(id):
    Item.query.filter_by(id=id).delete()
    db.session.commit()

# if_start()
def test_start():

    test = User(username="admin", email_address="admin@example.pl", password="adminadmin")

    db.session.add(test)
    db.session.commit()

# db.create_all()