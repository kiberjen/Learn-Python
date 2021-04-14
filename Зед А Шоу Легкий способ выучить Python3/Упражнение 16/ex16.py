from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("если вы не хотите стирать его, нажмите сочетание клавиш ctrl-C (^C).")
print("если хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("открытие файля...")
target = open(filename, 'w')

print("Очистка файла. До свидание!")
target.truncate()

print("Теперь я запрашиваю у вас три строки.")

line1 = input("строка 1:")
line2 = input("строка 2:")
line3 = input("строка 3:")

print("Это я запишу в файл.")

line = '{}\n{}\n{}\n'.format(line1, line2, line3)
target.write(line)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("И наконец я закрою файл.")
target.close()