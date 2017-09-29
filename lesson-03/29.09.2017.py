# Ветвление

a = 1
b = 2
if a > b:
    # pass  # показывает, что тут должен быть блок  кода, но он пустой
    print('a > b')
elif a == b:
    print('a = b')
else:
    print('a <= b')

# Тернарный оператор

# это обычная запись иф элсе
flag = True

if flag:
    v = 5
else:
    v = 'hello'

# Это уже тернарный оператор
v = 5 if flag else 'hello'

# Циклы


# WHILE DO
i = 1
summa = 0
while i < 10:
    summa += i
    i += 1
print(summa)

i = 1
while i:
    if i == 10:
        break  # прерывает цикл
    elif i == 8:
        continue  # пропустить итерацию
    i += 1
# continue - пропустить итерацию

# FOR EACH

for i in range(10, 20, 2):  # от 10 до 19, с шагом 2
    print(i, end=',')


# можно также выводить кучу данных из кортежей, наборов и т.д

# Срезы
lst = list(range(1, 20))
# lst[4] = 5
# lst[4:7] = 5,6,7  выбирает элементы с 4 индекса до 7 не включительно
# lst[-5:] = пять последних элементов, отсчёт ведётся от -1
# lst[x::-y] перевернуть список

s = 'hello, python'
# s[1] => e
# s[1:5] => ello

result = []
for i in range(10):
    result.append(str(i)) # добавить элемент в конец списока результ

result = ''.join(result) # список в строку
print(result)

########################################
# домашнее задание:
#