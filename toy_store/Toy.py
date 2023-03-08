import random

class Toy:
    def __init__(self, toy_id, name, count, probability):
        self.toy_id = toy_id
        self.name = name
        self.count = count
        self.probability = probability
    
    def __str__(self):
        return f"{self.toy_id}: {self.name} (count: {self.count}, probability: {self.probability}%)"
    
    def reduce_count(self):
        self.count -= 1
    
