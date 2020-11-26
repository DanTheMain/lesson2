# ДЗ - FOR cycle

# cоздать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1

print("incremeneted numbers")

num_list = [1, 3, 5, 0, -1, 1000, 8, 0, 5, 777, -10]

for num in num_list:
    print(num + 1)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

print('vertical string:')

for chr in list(input("Enter a string: ")):
    print(chr)

# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

print("grade stats:")

classes_score_data = [
    {'school_class': '4a', 'scores': [3,4,4,5,2,2,5,3]},
    {'school_class': '4b', 'scores': [5,4,3,2,1,4,4,5,3]},
    {'school_class': '5a', 'scores': [3,4,4,5,2,3,3,4]},
    {'school_class': '5b', 'scores': [3,4,4,5,2,5,3,4,4,5,2]},
    {'school_class': '5c', 'scores': [5]},
    {'school_class': '2a', 'scores': [3,4,4,5,2,2,5,3]},
    {'school_class': '2b', 'scores': [5,4,3,2,1,4,4,5,3]},
    {'school_class': '2c', 'scores': [3,4,4,5,2,3,3,4]},
    {'school_class': '2z', 'scores': []},
    {'school_class': '3a', 'scores': [3,4,4,5,2]},
    {'school_class': '3b', 'scores': [4,5,2,2,5,3]},
    {'school_class': '3c', 'scores': [5,4,3,2,1,4,4,3,5,5]},
    {'school_class': '3d', 'scores': [3,4,4,5,2,3,4,2,2,5]},
    {'school_class': '1a', 'scores': [3,4,4,5,2,5,3,2]}]

all_scores = 0
all_scores_num = 0

for class_data in classes_score_data:
    class_scores = 0
    for score in class_data['scores']:
        class_scores += score
        class_scores_num = len(class_data['scores'])
    all_scores += class_scores
    all_scores_num += class_scores_num

    print(f"Cредний балл по классу {class_data['school_class']}: {round(class_scores/class_scores_num, 2) if class_scores_num else 0}")

print(f"средний балл по всей школе: {all_scores/all_scores_num if all_scores_num else 0}")
