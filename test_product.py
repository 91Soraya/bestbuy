import pytest
from products import Product
import store
import main

#Test that creating a normal product works.

def test_name_normal_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.name == "Bose QuietComfort Earbuds"