import tkinter as tk
from tkinter import PhotoImage, messagebox
import pandas as pd
import os

# Caminho do arquivo Excel
caminho_do_arquivo = "kaplanilha.xlsx"  # Substitua pelo caminho real do seu arquivo

# Use pd.ExcelFile com a engine openpyxl
xls = pd.ExcelFile(caminho_do_arquivo, engine="openpyxl")

# Adicione essas linhas para imprimir o conteúdo do DataFrame:
print("Conteúdo do DataFrame:")
df = pd.read_excel(xls, sheet_name="Sheet1")  # Substitua "Planilha1" pelo nome da sua planilha
print(df)

# Variáveis globais
score = 0
current_question = 0

# Função para verificar a resposta
def check_answer(answer):
    global score, current_question

    correct_answer = df.iloc[current_question]["Resposta"]

    if int(answer) == int(correct_answer):
        score += 1
        # Chama a função para aplicar o efeito visual de confetes
        apply_correct_answer_effect()

    print(f"Resposta correta: {correct_answer}")
    print(f"Resposta dada: {answer}")
    print(f"Score: {score}")
    print(f"Pergunta Atual: {current_question + 1}/{len(df)}")

    current_question += 1

    if current_question < len(df):
        display_question()
    else:
        show_result()

# Função para exibir a próxima pergunta
def display_question():
    global current_question

    # Obtém os dados da linha correspondente à pergunta atual
    question_data = df.iloc[current_question]

    # Descompacta os dados
    question, option1, option2, option3, option4, answer = question_data

    question_label.config(text=question)

    # Configurações adicionais para redefinir o estado do botão
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda a=1: check_answer(a))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda a=2: check_answer(a))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda a=3: check_answer(a))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda a=4: check_answer(a))

# Função para exibir o resultado final
def show_result():
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)

    # Verifica a porcentagem de acertos
    percentual_acertos = (score / len(df)) * 100

    if percentual_acertos == 100:
        mensagem = "Parabéns, você é um ótimo namorado, merece uma massagem."
    else:
        mensagem = "Você precisa melhorar, ou será castigado."

    # Move a impressão da pontuação final aqui
    print(f"Score final: {score}")

    # Adiciona a mensagem personalizada
    messagebox.showinfo("Quiz Finalizado", f"{mensagem}\n\nPontuação final: {score}/{len(df)}")

    # Adiciona o botão "Jogar Novamente"
    play_again_btn.pack(pady=10)

# Função para aplicar o efeito visual de confetes
def apply_correct_answer_effect():
    # Altera a cor de fundo da janela para verde por 1 segundo (pode ajustar conforme necessário)
    janela.config(bg="#00FF00")
    janela.update_idletasks()

    # Agendamento para restaurar a cor original após 1 segundo
    janela.after(1000, restore_background_color)

def restore_background_color():
    janela.config(bg=background_color)
    janela.update_idletasks()

# Função para reiniciar o jogo
def restart_game():
    global score, current_question

    # Reinicializa as variáveis globais
    score = 0
    current_question = 0

    # Redefine o estado dos botões
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    # Esconde o botão "Jogar Novamente"
    play_again_btn.pack_forget()

    # Exibe a primeira pergunta
    display_question()

# Criação da janela
janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x500")

# Definindo as cores
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#001F3F"

janela.config(bg=background_color)
janela.option_add("*font", "Arial")

# Obtém o caminho do diretório atual do script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Concatena o caminho do diretório com o nome do arquivo
logo_path = os.path.join(script_directory, "logo.png")

# Ícone na tela
app_icon = PhotoImage(file=logo_path)
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Adicionando a variável correta à instância da janela
janela.correct_answer = tk.StringVar()

# Componentes da interface
question_label = tk.Label(text="", wraplength=300, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"), command=restart_game)

# Exibindo a primeira pergunta
display_question()

# Loop principal
janela.mainloop()

