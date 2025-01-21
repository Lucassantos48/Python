from selenium import webdriver
import time

#Abrir navegador
navegador = webdriver.Chrome()

#acessar site
navegador.get('https://www.hashtagtreinamentos.com/')
 
#colocar o navegador em tela cheia
navegador.maximize_window()

#selecionar um elemento na tela
botao_verde = navegador.find_element('class name', 'botao-verde')

#clicar no elemento
botao_verde.click()

#encontrar varios elementos
lista_botoes = navegador.find_elements('class name','header_titulo')

for botao in lista_botoes:
    if 'Assinatura' in botao.text:
        botao.click()
        break

#selecionar abas
abas = navegador.window_handles
navegador.switch_to.window(abas[1])

#site diferente
navegador.get('https://www.hashtagtreinamentos.com/curso-python?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=programacao')

#escrevendo em um campo/formulario
nome = navegador.find_element('id', 'firstname')
nome.send_keys('Lucas')
email = navegador.find_element('id', 'email')
email.send_keys('Lucas@gmail.com')
telefone = navegador.find_element('id', 'phone')
telefone.send_keys('912345678')

#Scroll (colocar um elemento na tela)


botao_cadastro = navegador.find_element('id','_form_2475_submit')
botao_cadastro.click()




time.sleep(10)


