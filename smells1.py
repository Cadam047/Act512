# smells1.py

PRICES = {
    "apple": 1.00,
    "banana": 0.50,
    "cherry": 0.75,
    "mango": 1.00,
    "pineapple": 1.50,
    "dragonfruit": 2.00,
    "durian": 2.75
}

DISCOUNT_THRESHOLD = 10.00
DISCOUNT_RATE = 0.10

def get_item_price(item):
    """Returns the price of a valid item or logs if unknown."""
    price = PRICES.get(item)
    if price is None:
        print(f"Unknown item: {item}")
        return 0
    return price

def calculate_subtotal(items):
    """Calculates the subtotal for the given list of items."""
    return sum(get_item_price(item) for item in items)

def apply_discount(total):
    """Applies a discount if the total reaches the threshold."""
    if total >= DISCOUNT_THRESHOLD:
        return total * (1 - DISCOUNT_RATE)
    return total

def calculate_total_price(items):
    """Calculates the final price after possible discounts."""
    subtotal = calculate_subtotal(items)
    return apply_discount(subtotal)

if __name__ == "__main__":
    print("Run `pytest tests/smells1_test.py` instead.")
