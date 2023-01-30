import pyautogui
from time import sleep

# 1- Clicar e digitar usuario
pyautogui.click(688,382, duration=0.5)
pyautogui.write('google')
# 2- Clicar e digitar senha
pyautogui.click(685,409, duration=0.5)
pyautogui.write('123')
# 3- clicar em "Entrar"
pyautogui.click(588,441, duration=0.5)
# 4- extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 	- Clicar e digitar produto
        pyautogui.click(420,373, duration=0.5)
        pyautogui.write(produto)
        # 	- Clicar e digitar quantidade
        pyautogui.click(435,399, duration=0.5)
        pyautogui.write(quantidade)
        # 	- Clicar e digitar preço
        pyautogui.click(436,423, duration=0.5)
        pyautogui.write(preco)
        # 	- Clicar em registrar
        pyautogui.click(312,587, duration=0.5)
        sleep(1)

