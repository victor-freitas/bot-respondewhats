from selenium import webdriver
import time

class WhatsappBot():

    def __init__ (self):
        self.mensagem = 'Obrigado por entrar em contato conosco, o  não se  encontra online. Para maiores informações acesse nosso site www.botparawhatsapp.com.br lá informaremos sobre o status da pessoa na qual você quer se comunicar. Obrigado.'
        self.contatos = ["Meu Amor 💙😍"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


    def EnviarMensagem(self):
       self.driver.get('https://web.whatsapp.com')
       time.sleep(30) 
       for contato in self.contatos:
            contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
            time.sleep(3)
            contato.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagem()

