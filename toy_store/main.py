

from controller1 import controller
from toys import Toy


lottery = controller()
lottery.print_all_toys()

while True:
    
    print('\nВыберите команду')
    print('1. Добавить игрушку в автомат')
    print('2. Изменить шанс')
    print('3. Сыграть в розыгрыш')
    print('4. Посмотреть корзину')
    print('5. Доставить игрушки в пункт выдачи')
    print('6. Выход')
    option = input()
        
    if option == '1': 
        toy_id = int(input("Введите ID: "))
        name = input("Введите название игрушки: ")
        count = int(input("Количество: "))
        probability = float(input("Шанс: "))
        toy = Toy(toy_id, name, count, probability)
        lottery.add_toy(toy)
        
    elif option == '2': 
        toy_id = input("Введите ID: ")
        new_probability = input("Какой шанс хотите: ")
        lottery.change_probability(toy_id, new_probability) 
    
    
    elif option == '3':
        lottery.run_lottery()
        
        
    elif option == '5': 
        lottery.deli()
    
    elif option == '4': 
        lottery.print_toys()
    
    elif option == '6': 
        lottery.save_toys()
        break
    else:
        print("ERROR")
