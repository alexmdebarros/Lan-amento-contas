import pyautogui
import time
import pandas as pd
import keyboard  # Para detectar a tecla de interrupção
import threading  # Para rodar a detecção de ESC em paralelo

# Variável global para interrupção
interromper = False

# Função para monitorar a tecla ESC
def monitorar_tecla():
    global interromper
    keyboard.wait("esc")  # Espera até que ESC seja pressionado
    interromper = True
    print("\n🛑 Interrompido pelo usuário!")

# Iniciar monitoramento de ESC em uma thread separada
threading.Thread(target=monitorar_tecla, daemon=True).start()

# Carregar a planilha CSV (ajuste o nome do arquivo)
df = pd.read_csv("./lancamentos.csv", sep=";", dtype={"Cta": str, "Vl_lancamento": str})  

# 🕒 Contagem regressiva antes de iniciar
print("⚠️ Prepare a tela do TOTVS! O sistema iniciará em:")
for i in range(5, 0, -1):
    if interromper:
        print("🛑 Execução cancelada antes de iniciar.")
        exit()
    print(f"⏳ {i} segundos...")
    time.sleep(1)

print("🚀 Iniciando lançamentos...")
time.sleep(2)  # Pequena pausa para transição

# ⏳ Capturar o tempo de início
tempo_inicio = time.time()

for index, row in df.iterrows():
    if interromper:
        break  # Se ESC for pressionado, sai do loop

    cta = row["Cta"]
    valor = row["Vl_lancamento"]
    data = "31/12/2024"  # Data fixa para todos os lançamentos

    print(f"📌 Lançando {index + 1}/{len(df)} | Conta: {cta} | Valor: {valor}")

    # 1️⃣ Limpar a tela
    pyautogui.press("f2")
    time.sleep(0.5)

    # 2️⃣ Preencher Cta
    pyautogui.click(x=138, y=158)
    pyautogui.write(cta)
    time.sleep(0.5)

    # 3️⃣ Preencher Data
    pyautogui.click(x=147, y=254)
    pyautogui.write(data)
    time.sleep(0.5)
    pyautogui.press("tab")

    # 4️⃣ Preencher Espécie ("A" e tab)
    pyautogui.write("A")
    time.sleep(0.5)
    pyautogui.press("tab")

    # 5️⃣ Preencher Valor do Lançamento
    pyautogui.write(valor)
    time.sleep(0.5)
    pyautogui.press("tab")

    # 6️⃣ Preencher Documento ("LUCRO" e tab)
    pyautogui.write("LUCRO")
    time.sleep(0.5)
    pyautogui.press("tab")

    # 7️⃣ Preencher Histórico Auxiliar ("LUCRO" e tab)
    pyautogui.write("LUCRO")
    time.sleep(0.5)
    pyautogui.press("tab")

    # 8️⃣ Preencher Código Histórico ("76" e tab)
    pyautogui.write("76")
    time.sleep(0.5)
    pyautogui.press("tab")

    # 9️⃣ Clicar em Confirmar
    pyautogui.click(x=935, y=663)
    time.sleep(0.8)  # Aguardar processamento

    # 🔟 Apertar Enter para fechar mensagem
    pyautogui.press("enter")
    time.sleep(0.8)

    # 1️⃣1️⃣ Repetir o ciclo limpando a tela
    pyautogui.press("f2")
    time.sleep(0.8)

# ⏳ Capturar o tempo final
tempo_fim = time.time()

# 🕒 Calcular o tempo total
tempo_total = tempo_fim - tempo_inicio

# 📌 Exibir tempo total formatado
minutos, segundos = divmod(tempo_total, 60)
print(f"✅ Lançamentos finalizados em {int(minutos)} min e {segundos:.2f} segundos!")
