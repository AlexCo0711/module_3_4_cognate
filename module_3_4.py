# Самостоятельная работа по уроку "Произвольное число параметров".

# Объявление функции single_root_words
def single_root_words(root_word, *other_words):
# создание пустого списка
    same_words = []
# цикл поиска *other_words в root_word или root_word в *other_words
    for i in (other_words):
# Условие для поиска и приведения символов к одному регистру
         if i.lower().count(root_word) == True or root_word.count(i.lower()) == True:
# Добавление найденных элементов в конец списка same_word
            same_words.append(i)
# вывод результата работы функции
    return same_words

# Исходный код
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод на консоль результата работы функции single_root_words для каждого вхождения
print(result1)
print(result2)
