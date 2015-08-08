from django.db.models import *
from django.contrib.auth.models import User


class Account(Model):
    user = ForeignKey(User)


class Transaction(Model):
    account = ForeignKey(Account)
    vendor = ForeignKey(Vendor)
    bill = ForeignKey(Bill)
    items = ManyToMany(Item)


class Vendor(Model):
    name = CharField(max_length=4096)
    location = CharField(max_length=4096)


class Item(Model):
    name = CharField(max_length=4096)
    classification = ForeignKey(Classification)


class Time(Model):
    time = DateTime()


class Classification(Model):
    pass


class Price(Model):
    items = ManyToMany(Item)


class Bill(Model):
    amount = DecimalField(max_digits=10, decimal_places=2)


class Statistic(Model):
    pass
