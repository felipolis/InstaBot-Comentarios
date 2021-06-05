from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:/WebDriver/bin/geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        # //input[@name="username"]
        # //input[@name="password"]

        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_hashtag("calistenia")

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        for i in range(1, 2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(pic_hrefs)
        # [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios = ["Muito legal!!!", "Mandou bem!!!", "Só admiração!!!"]
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(30, 40))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)


user = str(input("Digite o nome de usuario: "))
passw = str(input("Digite a sua senha: "))
archanjoBot = InstagramBot(user, passw)
archanjoBot.login()
