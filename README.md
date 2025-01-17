# 🐍 Desafio #1: Automação de Cadastro com PyAutoGUI

Este repositório contém a solução para o desafio número 1 da Jornada Python da Hashtag Treinamentos. O objetivo do programa é automatizar o processo de login em um sistema e o cadastro de produtos com base em uma planilha de dados utilizando a biblioteca *PyAutoGUI*.

---

## 🧠 Descrição do Problema

O desafio consiste em criar um script que:

1. *Realize login automático* em uma plataforma de treinamento.  
2. *Importe uma planilha* com informações de produtos.  
3. *Preencha automaticamente um formulário* na página web para cadastrar os produtos da planilha.  

### Requisitos Específicos:
- O programa deve abrir o navegador, acessar a página de login e autenticar o usuário.
- Após o login, deve navegar até a área de cadastro e preencher o formulário com os dados de cada produto.
- O formulário inclui campos como código, marca, tipo, categoria, preço unitário, custo e observações.

---

## ⚙️ Como Funciona o Programa

1. *Abrir o Navegador e Fazer Login:*
   - O programa utiliza coordenadas para clicar nos campos de email e senha.
   - Preenche o formulário de login e autentica o usuário.

2. *Importar a Planilha de Produtos:*
   - O script lê um arquivo CSV chamado produtos.csv, que deve estar no mesmo diretório do código.

3. *Cadastrar Produtos:*
   - Para cada linha da planilha:
     - Preenche os campos do formulário na página web usando o *PyAutoGUI*.
     - Envia o formulário e passa para o próximo produto.

4. *Scroll para Visibilidade:*
   - A página é rolada para garantir que o próximo formulário esteja visível.

---

## 🚀 Como Rodar o Programa

### Pré-requisitos:
- Python 3.x instalado.
- Bibliotecas necessárias:  
  bash
  pip install pyautogui pandas
  
- Arquivo produtos.csv no diretório do projeto contendo os campos:
  - codigo, marca, tipo, categoria, preco_unitario, custo, obs.

### Passos para Execução:
1. Clone este repositório:
   bash
   git clone https://github.com/seuusuario/desafio1-python.git
   cd desafio1-python
   

2. Execute o programa:
   bash
   python automacao_cadastro.py
   

3. Siga as instruções no terminal e verifique o cadastro na página web.

---

## ✅ Exemplos de Entrada e Saída

### *Entrada:*
Arquivo produtos.csv:
csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
12345,MarcaA,Mouse,Periféricos,50.00,30.00,Produto em promoção
67890,MarcaB,Teclado,Periféricos,100.00,70.00,Produto novo


### *Saída:*
- Produtos cadastrados automaticamente no sistema da plataforma.
- Mensagem no terminal indicando o status do cadastro:
  
  Cadastro de produtos finalizado.
  

---

## 🛠️ Ferramentas e Testes

### *Bibliotecas Utilizadas:*
- *PyAutoGUI:* Para automação do teclado e mouse.
- *Pandas:* Para manipulação da planilha de dados.

### *Testes Manuais:*
1. Certifique-se de que as coordenadas dos cliques (x, y) estão corretas para sua tela.
2. Use valores variados na planilha para testar diferentes cenários, incluindo campos vazios ou inválidos.

### *Validação de Estilo:*
- Verifique a formatação e estilo do código:
  bash
  flake8 automacao_cadastro.py
  

---

## 🌟 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou sugestões.
