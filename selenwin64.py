from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_wikipedia():
    driver = webdriver.Chrome()

    try:
        driver.get('https://ru.wikipedia.org')

        query = input("Введите запрос для поиска на Википедии: ")
        search_box = driver.find_element(By.NAME, 'search')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        search_results = driver.find_elements(By.CSS_SELECTOR, '.mw-search-result-heading a')
        if not search_results:
            print("По вашему запросу ничего не найдено.")
            return

        print("\nНайденные статьи:")
        for i, result in enumerate(search_results):
            print(f"{i + 1}. {result.text}")

        choice = input("Введите номер статьи для перехода или '0' для выхода: ")
        if choice.isdigit() and 0 < int(choice) <= len(search_results):
            article_link = search_results[int(choice) - 1].get_attribute('href')
            driver.get(article_link)
            time.sleep(2)
        else:
            print("Неверный выбор или выход.")
            return

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Введите номер действия: ")

            if choice == '1':
                paragraphs = driver.find_elements(By.TAG_NAME, 'p')
                for p in paragraphs:
                    print(p.text)
                    if input("Нажмите Enter для продолжения или введите '0' для выхода из параграфов: ") == '0':
                        break

            elif choice == '2':
                links = driver.find_elements(By.CSS_SELECTOR, '.mw-body a')
                index = 0
                while index < len(links):
                    print("\nСвязанные страницы:")
                    for i in range(index, min(index + 7, len(links))):
                        print(f"{i + 1}. {links[i].text}")
                    link_choice = input("Введите номер страницы, чтобы перейти, 'n' для следующих семи, 'p' для предыдущих семи или '0' для выхода: ")
                    if link_choice.isdigit() and index < int(link_choice) <= index + 7:
                        next_link = links[int(link_choice) - 1].get_attribute('href')
                        driver.get(next_link)
                        time.sleep(2)
                        break
                    elif link_choice == 'n':
                        index += 7
                    elif link_choice == 'p' and index - 7 >= 0:
                        index -= 7
                    elif link_choice == '0':
                        break
                    else:
                        print("Неверный выбор, попробуйте снова.")

            elif choice == '3':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор, попробуйте снова.")

    finally:
        driver.quit()

if __name__ == "__main__":
    search_wikipedia()