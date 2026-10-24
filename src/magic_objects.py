class InventoryItem:
    """
    A class representing an item in the inventory.
    """

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(item={self.item},quantity={self.quantity})"

    # arthemetic operations
    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.item == other.item:
            return InventoryItem(self.item, self.quantity + other.quantity)
        raise ValueError("Cannot add items of different types")

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.item == other.item:
            if self.quantity >= other.quantity:
                return InventoryItem(self.item, self.quantity - other.quantity)
            raise ValueError("Cannot subtract more than available quantity")
        raise ValueError("Cannot subtract items of different types")

    def __mul__(self, factor):
        if isinstance(factor, int):
            return InventoryItem(self.item, self.quantity * factor)
        raise ValueError("Can only multiply by an integer")


I1 = InventoryItem("Apple", 5)
I2 = InventoryItem("Banana", 10)
I3 = InventoryItem("Apple", 10)

res_add = I1 + I3
print(repr(res_add))  # Output: InventoryItem(item=Apple,quantity=15)

res_sub = res_add - I1
print(repr(res_sub))  # Output: InventoryItem(item=Apple,quantity=10)

res_mul = I2 * 3
print(repr(res_mul))  # Output: InventoryItem(item=Banana,quantity=30)

res_mul_invalid = I1 * 2.5  # Raises ValueError: Can only multiply by an integer
