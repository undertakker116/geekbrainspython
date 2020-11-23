#"Программа №1"
#name = input("Назовите ваше имя: ")
#surname = input("Напишите вашу фамилию: ")
#age = int(input("Напишите свой возраст: "))
#print(name, surname, age)


#"Программа №2"
#print("введите время в секундах и я вам переведу время в формат чч:мм:сс")
#time =int(input("Напишите время в секундах: "))
#hours = time // 3600
#minutes = (time - hours * 3600) // 60
#seconds = time - (hours * 3600 + minutes * 60)
#print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

#"Программа №3"
#n = int(input("Введите число n: "))
#total = (n + int(str(n)+ str(n)) + int(str(n) + str(n) + str(n)))
#print(f"Сумма чисел {n} + {int(str(n)+ str(n))} + {int(str(n) + str(n) + str(n))} = % d " % total)






#"Программа №4"
#n = abs(int(input("Введите целое положительное число ")))
#max = n % 10
#while n >= 1:
#    n = n // 10
#    if n % 10 > max:
#       max = n % 10
#   if n > 9:
#        continue
#    else:
#       print("Максимальное цифра в числе ", max)
#       break

# #"Программа №5"
# #profit = float(input("Введите выручку фирмы "))
# #costs = float(input("Введите издержки фирмы "))
# #if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f'прибыль в расчете на одного сторудника сотавила {profit / workers:.2f})
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")

"Программа №6"
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    print(f' в {result_days} - ый день вы пробежите: {result_km}')
    result_km = result_km + a
    round(result_km)
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)







