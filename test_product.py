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

#Test that creating a product with invalid details (empty name, negative price) invokes an exception.

def test_new_product_empty_name():
    with pytest.raises(ValueError):
        Product("", price=250, quantity=500)

def test_new_product_negative_price():
    with pytest.raises(ValueError):
        Product("Bose QuietComfort Earbuds", price=-250, quantity=500)


#Test that when a product reaches 0 quantity, it becomes inactive.

def test_inactive_product_when_zero_quantity():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.is_active() == True
    bose.buy(500)
    assert bose.is_active() == False


#Test that product purchase modifies the quantity and returns the right output.

def test_quantity_after_purchase():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose._quantity == 500
    bose.buy(50)
    assert bose._quantity == 450

#Test that buying a larger quantity than exists invokes exception.

def test_purchase_larger_than_quantity():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    with pytest.raises(ValueError):
        bose.buy(600)

