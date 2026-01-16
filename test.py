def product_details(product_name, product_id,quanity,price):
    return (
        f"product_name: {product_name}\n"
        f"product_id: {product_id}\n"
        f"quanity: {quanity}\n"
        f"price: {price}"
    )

if __name__ == "__main__":
    product_name = "Laptop"
    product_id = "LP1001"
    quanity = 5
    price = 999.99
    print(product_details(product_name, product_id,quanity,price))