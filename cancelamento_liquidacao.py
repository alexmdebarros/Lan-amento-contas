import pyautogui
import time
import pandas as pd
import keyboard
import threading

interromper = False

# Tempo médio gasto manualmente por lançamento (em segundos)
tempo_por_lancamento_manual = 38.86

# Função para monitorar a tecla ESC
def monitorar_tecla():
    global interromper
    keyboard.wait("f8")
    interromper = True
    print("\n🛑 Interrompido pelo usuário!")


threading.Thread(target=monitorar_tecla, daemon=True).start()


df = pd.read_csv("./liquidacao.csv", sep=";", dtype={"liquidacao": str})  
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

    liquidacao = row["liquidacao"]
    observacao = "DUPLICIDADE"
    
    print(f"📌 Lançando {index + 1}/{total_lancamentos} | Liquidação: {liquidacao}")

    #Limpa a tela
    pyautogui.press("f2")
    time.sleep(0.5)

    #Preenche liquidação
    pyautogui.click(x=406, y=205)
    pyautogui.write(liquidacao)
    time.sleep(0.5)

    #Preenche observação
    pyautogui.click(x=102, y=452)
    pyautogui.write(observacao)
    time.sleep(0.5)
    pyautogui.click(x=40, y=103)
    time.sleep(0.8)
    
    #pega lançamento contabil
    pyautogui.click(x=604, y=518)
    time.sleep(1.0)
    pyautogui.click(x=901, y=583)
    time.sleep(1.5)
    pyautogui.click(x=1300, y=395)
    time.sleep(0.9)
    pyautogui.doubleClick(x=1320, y=543)
    time.sleep(0.9)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.6)
    pyautogui.press("esc")
    time.sleep(0.5)
    pyautogui.press("esc")
    time.sleep(0.5)
    
    #cancelando lançamento contabil
    pyautogui.click(x=125, y=33)
    time.sleep(0.6)
    pyautogui.click(x=112, y=121)
    time.sleep(0.6)
    pyautogui.click(x=112, y=140)
    time.sleep(0.9)
    pyautogui.click(x=134, y=141)
    time.sleep(0.6)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.6)
    pyautogui.press("tab")
    time.sleep(0.6)
    pyautogui.click(x=470, y=695)
    time.sleep(0.9)
    pyautogui.click(x=899, y=582)
    time.sleep(0.7)
    pyautogui.press("esc")
    time.sleep(0.6)
    pyautogui.click(x=603, y=694)
    time.sleep(0.9)
    pyautogui.click(x=899, y=582)
    time.sleep(0.7)
    pyautogui.press("esc")
    time.sleep(0.6)
    pyautogui.press("esc")
    time.sleep(0.6)
    pyautogui.press("esc")
    time.sleep(0.6)
    
    #cancelando liquidação
    pyautogui.click(x=602, y=515)
    time.sleep(0.9)
    pyautogui.click(x=899, y=582)
    time.sleep(1.0)
    pyautogui.press("esc")
    time.sleep(0.6)
    
    #Repete o ciclo limpando a tela
    pyautogui.press("f2")
    time.sleep(0.9)

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