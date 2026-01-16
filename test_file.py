from test import product_details

def test_product_details():
    expected_output = (
        "product_name: Headphones\n"
        "product_id: HP1001\n"
        "quanity: 2\n"
        "price: 199.99"
    )

    assert product_details("Headphones", "HP1001", 2, 199.99) == expected_output