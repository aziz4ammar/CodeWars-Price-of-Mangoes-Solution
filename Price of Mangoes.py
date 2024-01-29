def mango(quantity, price):
    total_cost = (quantity // 3) * (2 * price) + (quantity % 3) * price
    return total_cost