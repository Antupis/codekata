from collections import Counter
from typing import Dict, List


class Checkout(object):
    """
     My checkout implementation. Calculates total sum from scanned items based on rules that has given when class is initialized.


     Attributes
    ----------
    rules : Dict
        Rules which is used total sum calculation.
    """
    rules: Dict
    items: List[str]

    def __init__(self, rules: Dict):

        if not rules:
            raise ValueError('rules missing')

        self.rules = rules
        self.items = []

    def scan(self, item: str):
        """
        scans items.

        Parameters
        ----------
        item:str
            list of items which is scanned.
        """
        if item not in self.rules.keys():
            raise KeyError('item is missing from rules')

        self.items.append(item)

    def total(self) -> int:
        """
        Calculates total sum of items based on rules.

        :return:int
            returns total sum of prices.
        """
        total_item_counts = Counter(self.items)
        total = 0

        for item, count in total_item_counts.items():

            rules_for_item = self.rules[item]
            if 'special_price' in rules_for_item and count > 1:
                sale_count, sale_price = rules_for_item['special_price']
                total += count // sale_count * sale_price
                total += count % sale_count * rules_for_item['price']
            else:
                total += rules_for_item['price'] * count

        return total
