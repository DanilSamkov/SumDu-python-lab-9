import re

# Функція для створення файлу TF7_1
def create_file_tf7_1():
    try:
        with open('TF7_1.txt', 'w', encoding='utf-8') as file:
            file.write("Це приклад рядка з текстом.\n")
            file.write("В цьому тексті є букви і слова з повтореннями, наприклад зілля або потяг.\n")
            file.write("Ще один рядок без подвоєнь букв.\n")
        print("Файл TF7_1 успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу TF7_1: {e}")


# Функція для пошуку слів із подвоєнням букв і запису їх у TF7_2
def find_and_write_double_letters():
    try:
        with open('TF7_1.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)  # Знаходження всіх слів
            double_letter_words = [word for word in words if
                                   re.search(r'(.)\1', word)]  # Пошук слів з подвоєними літерами

        if double_letter_words:
            with open('TF7_2.txt', 'w', encoding='utf-8') as file:
                for word in double_letter_words:
                    file.write(word + '\n')
            print("Слова з подвоєнням букв записані у файл TF7_2.")
        else:
            with open('TF7_2.txt', 'w', encoding='utf-8') as file:
                file.write("У файлі TF7_1 немає слів з подвоєнням букв.\n")
            print("У файлі TF7_1 немає слів з подвоєнням букв, відповідне повідомлення записане у файл TF7_2.")
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")


# Функція для читання і виведення вмісту файлу TF7_2
def print_file_tf7_2():
    try:
        with open('TF7_2.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Помилка при читанні файлу TF7_2: {e}")


if __name__ == "__main__":
    create_file_tf7_1()
    find_and_write_double_letters()
    print_file_tf7_2()