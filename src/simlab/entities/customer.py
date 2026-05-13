# src/simlab/entities/customer.py

from simlab.ids import Identifier

class Customer:
    def __init__(self, identifier: Identifier) -> None:
        self.id = identifier.new_id()

