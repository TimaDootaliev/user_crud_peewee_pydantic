import peewee as pw
from core.settings import settings


def get_db():
    return pw.PostgresqlDatabase(settings.db)

a = 10
b = 20

c = 30
d = 40

def good_bye():
    return 'good_bye
