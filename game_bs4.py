from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    translator = GoogleTranslator(source='en', target='ru')  # Создаем экземпляр переводчика вне цикла
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        
        word_rus = translator.translate(word)  # Переводим слово
        word_rus_definition = translator.translate(word_definition)  # Переводим определение
        # Начинаем игру
        print(f"Значение слова - {word_rus_definition}")
        user = input("Что это за слово? ")
        if user.strip().lower() == word_rus.strip().lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_rus}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

word_game()