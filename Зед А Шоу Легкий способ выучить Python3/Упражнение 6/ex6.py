types_of_people = 10
x = f"Существуют {types_of_people} типов людей."

binary = "Python"
do_not = "нет"
y = f"Те, кто понимает {binary}, и те, кто - {do_not}."

print(x)
print(y)

print(f"Я сказал: {x}")
print(f"А еще я сказал: '{y}'")

hilarious = False
joke_evaluation = "Развитие это не смешно?! {}"

print(joke_evaluation.format(hilarious))

w = "Это часть строки слева..."
e = "А это справа."

print(w + e)