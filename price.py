def discounted(price, discount):
    if discount >= 100:
        price_with_discount = price 
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)

price = 100
discount = 10
