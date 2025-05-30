import pyautogui
import time
import pandas as pd
import keyboard
import threading

interromper = False

# Tempo médio gasto manualmente por lançamento (em segundos)
tempo_por_lancamento_manual = 25.61

# Função para monitorar a tecla ESC
def monitorar_tecla():
    global interromper
    keyboard.wait("esc")
    interromper = True
    print("\n🛑 Interrompido pelo usuário!")


threading.Thread(target=monitorar_tecla, daemon=True).start()


df = pd.read_csv("./lancamentos.csv", sep=";", dtype={"Cta": str, "Vl_lancamento": str})  
total_lancamentos = len(df)


print("⚠️ Prepare a tela do TOTVS! O sistema iniciará em:")
for i in range(5, 0, -1):
    if interromper:
        print("🛑 Execução cancelada antes de iniciar.")
        exit()
    print(f"⏳ {i} segundos...")
    time.sleep(1)

print("🚀 Iniciando lançamentos...")
time.sleep(2)

tempo_inicio = time.time()

for index, row in df.iterrows():
    if interromper:
        break

    cta = row["Cta"]
    valor = row["Vl_lancamento"]
    data = "01/01/2024"

    print(f"📌 Lançando {index + 1}/{total_lancamentos} | Conta: {cta} | Valor: {valor}")

    #Limpa a tela
    pyautogui.press("f2")
    time.sleep(0.5)

    #Preenche Cta
    pyautogui.click(x=138, y=158)
    pyautogui.write(cta)
    time.sleep(0.5)

    #Preenche Data
    pyautogui.click(x=147, y=254)
    pyautogui.write(data)
    time.sleep(0.5)
    pyautogui.press("tab")

    #Preenche Espécie ("A" e tab)
    pyautogui.write("A")
    time.sleep(0.5)
    pyautogui.press("tab")

    #Preenche Valor do Lançamento
    pyautogui.write(valor)
    time.sleep(0.5)
    pyautogui.press("tab")

    #Preencher Documento ("LUCRO" e tab)
    pyautogui.write("ESTORNO")
    time.sleep(0.5)
    pyautogui.press("tab")

    #Preenche Histórico Auxiliar ("LUCRO" e tab)
    pyautogui.write("DUPLICIDADE")
    time.sleep(0.5)
    pyautogui.press("tab")

    #Preenche Código Histórico ("76" e tab)
    pyautogui.write("75")
    time.sleep(0.5)
    pyautogui.press("tab")

    #Clica em Confirmar
    pyautogui.click(x=935, y=663)
    time.sleep(0.8)  # Aguardar processamento

    #Aperta Enter para fechar mensagem
    pyautogui.press("enter")
    time.sleep(0.8)

    #Repete o ciclo limpando a tela
    pyautogui.press("f2")
    time.sleep(0.8)

#Captura o tempo final
tempo_fim = time.time()

#Calcula o tempo total gasto pelo script
tempo_total_script = tempo_fim - tempo_inicio

#Calcula o tempo que seria gasto manualmente
tempo_total_manual = total_lancamentos * tempo_por_lancamento_manual

#Calcula o tempo economizado
tempo_economizado = tempo_total_manual - tempo_total_script

#Exibir resultados formatados
minutos_script, segundos_script = divmod(tempo_total_script, 60)
minutos_economizados, segundos_economizados = divmod(tempo_economizado, 60)

print(f"\n✅ Lançamentos finalizados em {int(minutos_script)} min e {segundos_script:.2f} segundos!")
print(f"🕒 Se fosse manualmente, levaria {int(tempo_total_manual // 60)} min e {tempo_total_manual % 60:.2f} segundos.")
print(f"💰 Tempo economizado: {int(minutos_economizados)} min e {segundos_economizados:.2f} segundos! 🚀")