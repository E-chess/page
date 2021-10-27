from market.models import Item
from market import db
import berserk, os


def list():
	for item in Item.query.all():
		print(item.id)
		print(item.price)
		print(item.name)
		print(item.description)


def add():
	item1 = Item(name ="test", price =1, barcode = "11", description = "Proszę nie dołączać do tego turnieju")

	db.session.add(item1)
	db.session.commit()

def berserk_start():
	session = berserk.TokenSession(os.environ["OAuth2"])
	client = berserk.Client(session=session)
	return client

def add_turniej():
	client = berserk_start()

	print(client.tournaments.create(5, 0, 45))

def get_turniej():
	client = berserk_start()

	print(client.tournaments.export_games("kHFTwbi1"))



get_turniej()


