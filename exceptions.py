# Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу при помощи оператора break

print("hello user with interrupt!")

def hello_user_interruptable():
    while True:
        try:
            if input('Как дела? ') == 'Хорошо':
                break
        except KeyboardInterrupt:
            print("Пока!")
            break

hello_user_interruptable()


# Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
# чтобы она перехватывала исключения, когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, 
# если приведение типов не сработало.

def discounted_with_exception_handling(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError):
        print("Неправильный тип аргумента!")
        return -1
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

print(discounted_with_exception_handling(100, 10, 10))
print(discounted_with_exception_handling(-100, -10, -10.5))
print(discounted_with_exception_handling('lOO', 0, '*'))
