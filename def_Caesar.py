Шифр цезаря
На основании функции rotate_letter из предыдущего задания мы с вами можем реализовать знаменитый шифр Цезаря.
Этот шифр берет каждую букву исходной фразы и смещает ее на значение ключа. Под ключом здесь подразумевается значение
сдвига shift. В пределах кодирования одной фразы значение сдвига всегда постоянно.
И так, ваша задача создать функцию caesar_cipher, которая имеет два обязательных параметра:
phrase входной текст для шифрования
key значение ключа шифра, он же сдвиг
Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его
по следующим правилам:
1. если символ является знаком пунктуации, оставляем его как есть
2. если это буква, то сместить ее при помощи ранее написанной функции rotate_letter  на значение ключа
Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы
caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
caesar_cipher('one more light', 3) => 'rqh pruh oljkw'

# Для успешного решения напишите реализацию функции caesar_cipher, которая использует функцию rotate_letter.
# (нужно продублировать определение функции rotate_letter из предыдущего урока).
# Дополнительно нужно :
# сделать аннотацию параметров и возвращаемого значения всех функций
# сделать док-строку для функции caesar_cipher со значением «Шифр Цезаря»

def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    if shift > 0:
        rez = ord(letter) + shift % 26
        if rez > ord('z'):
            rez_1 = rez - ord('z')
            return chr(ord('a') + rez_1 - 1)
        else:
            return chr(rez)

    if shift < 0:
        rez_a = ord(letter) - ord('a')  # ord(a) = 97 ск букв до первой буквы алфавита, разница
        rez_shift = (shift + rez_a) % 26  # опред остаток шагов, т.к. число < 0, поэтому +rez_a
        rez = rez_shift + ord('a')
        if rez > ord('z'):
            rez_1 = rez - ord('z')
            return chr(ord('a') + rez_1)
        else:
            return chr(rez)


def caesar_cipher(phrase: str, key: int) -> str:
    """Шифр Цезаря"""
    fin_phrase = ''  # переменная для измененной строки
    for i in range(len(phrase)):
        if not phrase[i].isalpha():
            fin_phrase += phrase[i]
        if phrase[i].isalpha():
            fin_phrase += rotate_letter(phrase[i], key)  # добавляем изменен букву
    return fin_phrase

print(caesar_cipher.__annotations__)
print(caesar_cipher.__doc__)
print(caesar_cipher('lost in the echo', 1))



