import random

class controller:
    def __init__(self):
        self.toys = []
    
    def add_toy(self, toy):
        self.toys.append(toy)
        with open("toy_text.txt", "a") as f:
            f.write(f"{toy.toy_id},{toy.name},{toy.count},{toy.probability}\n")
    
    
    
    def save_toys(self):
        with open("toy_text.txt", "w") as f:
            for toy in self.toys:
                f.write(f"{toy.toy_id},{toy.name},{toy.count},{toy.probability}\n")
                
                
                
                
    def change_probability(cls, toy_id, new_probability):
        toys = []
        with open('toy_text.txt', 'r') as f:
            for line in f.readlines():
                toy = line.strip().split(',')
                if toy[0] == toy_id:
                    toy[3] = new_probability
                toys.append(toy)

        with open('toy_text.txt', 'w') as f:
            for toy in toys:
                f.write(','.join(toy) + '\n')          
    
    def select_toy(self):
        total_prob = sum(toy.probability for toy in self.toys)
        r = random.uniform(0, total_prob)
        cum_prob = 0
        for toy in self.toys:
            cum_prob += toy.probability
            if r <= cum_prob:
                if toy.count > 0:
                    toy.reduce_count()
                    with open("text_win.txt", "a") as f:
                        f.write(f"{toy.toy_id},{toy.name}\n")
                    if toy.count == 0:
                        self.toys.remove(toy)
                    return toy
                else:
                    self.toys.remove(toy)
                    return None
    
    def run_lottery(self):
        toy = self.select_toy()
        if toy:
            print(f"Ты получил: {toy}")
        else:
            print("Не осталось.")
    
    def print_all_toys(self):
        for toy in self.toys:
            print(toy)
            
           
    def print_toys(self):
        with open('text_win.txt', 'r') as file:
            f = file.read()
        print(f)
        
        
        
    def deli(self):
        with open('text_win.txt', "r") as f:
            toys = f.readlines()
        if not toys:
            print("Пусто")
            return
        first_toy = toys[0]
        with open('text_deli.txt', "a") as f:
            f.write(first_toy)
        with open('text_win.txt', "w") as f:
            f.writelines(toys[1:])
        print(f"Товары из корзины уже собираются {first_toy.split(',')[1]}!")

# Example usage:
lottery = controller()
lottery.print_all_toys()