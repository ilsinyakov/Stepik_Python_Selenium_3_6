from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_basket_button_exist(browser):
    try:
        # ссылка на страницу товара
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        # открываем ссылку
        browser.get(link)
        # это нужно раскомментировать для проверки французской корзины по условию задачи
        # time.sleep(10)
        # ждем, когда загрузится страница (проверяем по наличию кнопки "Добавить в корзину")
        WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
        )
        # 3 секунды, чтобы увидеть, что есть на сайте
        time.sleep(3)
        
        # хрен его знает, зачем здесь assert, но т.к. по условию задачи он нужен ОБЯЗАТЕЛЬНО, пришлось добавить )))        
    except:
        assert False, 'Кнопка "Добавить в корзину" не найдена'
    