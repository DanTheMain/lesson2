import ephem

mars = ephem.Mars('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)

# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
# В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.