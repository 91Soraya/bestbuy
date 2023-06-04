import pytest
from products import Product
import store
import main

#Test that creating a normal product works.

def test_name_normal_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose._name == "Bose QuietComfort Earbuds"

def test_price_normal_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose._price == 250

def test_quantity_normal_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose._quantity == 500