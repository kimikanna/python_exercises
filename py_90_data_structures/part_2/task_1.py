# Дано расстояние L в сантиметрах. Используя операцию деления нацело,
# найти количество полных метров в нем (1 метр = 100 см).

def get_metres(centimetres):
    metres = centimetres // 100
    return metres


centimetres = int(input("Введите расстояние в сантиметрах: "))
print("Расстояние в метрах:", get_metres(centimetres))
