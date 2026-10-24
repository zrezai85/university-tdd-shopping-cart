from shopping_cart import ShoppingCart


def test_add_product_to_empty_cart():
    cart = ShoppingCart()
    cart.add_product('book',100000)
    assert cart.total() == 100000

