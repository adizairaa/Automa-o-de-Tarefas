import pyautogui
import time
import pandas as pd

# Configuração do tempo de pausa entre os comandos do PyAutoGUI
pyautogui.PAUSE = 1

# Abrir o navegador Chrome e acessar a página de login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(10)

# Fazer login na página
pyautogui.click(x=592, y=509)  # Selecionar o campo de email
pyautogui.write("adila.zaira@gmail.com")
time.sleep(2)

pyautogui.press("tab")  # Passar para o campo de senha
pyautogui.write("123456")
time.sleep(2)

pyautogui.press("tab")  # Passar para o botão de login
pyautogui.press("enter")
time.sleep(5)

# Importar a base de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastrar os produtos
for linha in tabela.index:
    try:
        # Clicar no campo inicial para cadastro
        pyautogui.click(x=587, y=361)  
        time.sleep(1)

        # Preencher os campos do formulário
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

        marca = tabela.loc[linha, "marca"]
        pyautogui.write(str(marca))
        pyautogui.press("tab")

        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(str(tipo))  # Corrigido o erro de "mause"
        pyautogui.press("tab")

        categoria = tabela.loc[linha, "categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

        preco_unitario = tabela.loc[linha, "preco_unitario"]
        pyautogui.write(str(preco_unitario))
        pyautogui.press("tab")

        custo = tabela.loc[linha, "custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if pd.notna(obs):  # Verifica se o valor não é NaN
            pyautogui.write(str(obs))
        pyautogui.press("tab")

        # Enviar o formulário
        pyautogui.press("enter")
        time.sleep(2)

        # Scroll para garantir visibilidade do próximo formulário (ajuste se necessário)
        pyautogui.scroll(1000)

    except Exception as e:
        print(f"Erro ao processar a linha {linha}: {e}")

print("Cadastro de produtos finalizado.")
