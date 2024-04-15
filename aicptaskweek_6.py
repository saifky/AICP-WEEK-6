class Sack:
    def __init__(self, content, weight):
        self.content = content
        self.weight = weight

    def check_contents_and_weight(self):
        if self.content not in ['C', 'G', 'S']:
            return "Invalid content: must be 'C' (cement), 'G' (gravel), or 'S' (sand)"
        
        if (self.content == 'C' and not (24.9 < self.weight < 25.1)) or \
           ((self.content == 'G' or self.content == 'S') and not (49.9 < self.weight < 50.1)):
            return "Invalid weight for content"

        return True


class Order:
    def __init__(self):
        self.sacks = {'C': 0, 'G': 0, 'S': 0}

    def add_sack(self, sack):
        self.sacks[sack.content] += 1

    def check_order(self):
        total_weight = 0
        sacks_rejected = 0

        for content, count in self.sacks.items():
            total_weight += count * (25 if content == 'C' else 50)

        for content, count in self.sacks.items():
            if content == 'C':
                price = 3
            else:
                price = 2

            if count * price != total_weight:
                sacks_rejected += count

        return total_weight, sacks_rejected

    def calculate_price(self):
        total_price = 0
        special_packs = min(self.sacks['C'], self.sacks['G'] // 2, self.sacks['S'] // 2)
        total_price += (self.sacks['C'] - special_packs) * 3
        total_price += (self.sacks['G'] - 2 * special_packs) * 2
        total_price += (self.sacks['S'] - 2 * special_packs) * 2
        discount_price = total_price + special_packs * 10

        if discount_price < total_price:
            return discount_price, total_price - discount_price
        else:
            return total_price, 0


def main():
    # Task 1 - Check the contents and weight of a single sack
    print("Task 1 - Check the contents and weight of a single sack:")
    content = input("Enter content (C for cement, G for gravel, S for sand): ")
    weight = float(input("Enter weight of the sack: "))
    sack = Sack(content.upper(), weight)
    result = sack.check_contents_and_weight()
    if result is True:
        print("Accepted sack:")
        print(f"Content: {sack.content}, Weight: {sack.weight} kg")
    else:
        print("Rejected sack:")
        print(result)

    # Task 2 - Check a customer's order for delivery
    print("\nTask 2 - Check a customer's order for delivery:")
    order = Order()
    order.add_sack(Sack('C', 25))
    order.add_sack(Sack('G', 50))
    order.add_sack(Sack('S', 50))
    total_weight, sacks_rejected = order.check_order()
    print(f"Total weight of the order: {total_weight} kg")
    print(f"Number of sacks rejected from the order: {sacks_rejected}")

    # Task 3 - Calculate the price for a customer's order
    print("\nTask 3 - Calculate the price for a customer's order:")
    regular_price, discount_saved = order.calculate_price()
    if discount_saved > 0:
        print(f"Regular price for the order: ${regular_price}")
        print(f"Discounted price for the order: ${regular_price - discount_saved}")
        print(f"Amount saved: ${discount_saved}")
    else:
        print(f"Price for the order: ${regular_price}")


if __name__ == "__main__":
    main()
