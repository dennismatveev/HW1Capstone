from dataclasses import dataclass
from typing import List


@dataclass
class merchandise:
    item_name: str
    item_price: float
    item_type: str


def calculate_total(state: str, list_of_records: List):
    total_to_pay = 0
    tax_total = 0
    if state == "MA":
        tax = .0625
    elif state == "ME":
        tax = .055
    elif state == "NH":
        tax = 0

    if list_of_records:
        for element in list_of_records:
            if element.item_type == 'WIC':
                total_to_pay += element.item_price
            elif element.item_type == "Clothing":
                if element.item_price < 175:
                    total_to_pay += element.item_price
                else:
                    tax_total += (element.item_price - 175) * tax
                    total_to_pay += element.item_price + tax_total
            elif element.item_type == "Other":
                tax_total += element.item_price * tax
                total_to_pay += element.item_price + tax_total

    return total_to_pay


def main():
    cart = [merchandise('banana', .49, 'Other'), merchandise('apple', .49, 'Other')]
    print(calculate_total("NH", cart))


if __name__ == '__main__':
    main()
