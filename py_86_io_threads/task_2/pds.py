# подключаем модуль pathlib и библиотеку Path модуля pathlib
import pathlib
from pathlib import Path

# Импортируем Pandas
import pandas as pd

# Получаем строку, содержащую путь к рабочей директории:
work_path = pathlib.Path.cwd()

# сохраним путь к csv файлу в переменной data_path
data_path = Path(work_path, 'task_2', 'bikes.csv')

# Считываем содержимое файла в переменную data:
data = pd.read_csv(data_path)

# Выведем первые 5 строк:
print(data.head(5))
print()

# Посчитаем сумму столбца Rachel1 из файла:
print('Сумма столбца Rachel1:', data.sum()['Rachel1'])
