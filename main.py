import pandas as pd
import random

# Генерация данных
lst = ['robot']  *  10
lst += ['human']  *  10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание пустого DataFrame для one-hot кодирования
one_hot = pd.DataFrame()

# Получение уникальных значений
unique_values = data['whoAmI'].unique()

# Заполнение DataFrame значениями 0 и 1
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

# Вывод первых строк
print(one_hot.head())

