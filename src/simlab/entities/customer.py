# src/simlab/entities/customer.py

class Customer:
    def __init__(self, customer_id: str, product_fit: float, usage_score: float, satisfaction_score: float) -> None:
        self.customer_id = customer_id
        self.product_fit = product_fit
        self.usage_score = usage_score
        self.satisfaction_score = satisfaction_score


