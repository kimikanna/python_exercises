# Дана масса M в килограммах. Используя операцию деления нацело,
# найти количество полных тонн в ней (1 тонна = 1000 кг).

def get_tons(kilograms):
    tons = kilograms // 1000
    return tons


kilograms = int(input("Введите массу (кг): "))
print("Масса в тоннах:", get_tons(kilograms))
