import pyautogui
import pyperclip
import time
import random
import traceback
import os
import shutil
from pathlib import Path

pyautogui.FAILSAFE = True


def delay(a=0.5, b=1.5):
    time.sleep(random.uniform(a, b))


def mover_e_clicar(x, y):
    pyautogui.moveTo(
        x + random.randint(-3, 3),
        y + random.randint(-3, 3),
        duration=random.uniform(0.2, 0.6)
    )
    pyautogui.click()
    delay()


def abrir_nova_aba():
    pyautogui.hotkey("ctrl", "t")
    delay()

def fechar_aba():
    pyautogui.hotkey("ctrl", "w")
    delay()


def acessar_site():
    pyperclip.copy("https://www.meudanfe.com.br")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(2.5)


def digitar_chave(chave):
    pyperclip.copy(chave)
    pyautogui.hotkey("ctrl", "v")
    delay()


def criar_pasta_downloads(nome_pasta):
    downloads = str(Path.home() / "Downloads")
    caminho = os.path.join(downloads, nome_pasta)
    os.makedirs(caminho, exist_ok=True)
    return caminho


# 🔥 NOVA FUNÇÃO (corrigida de verdade)
def esperar_e_mover_xml(destino, timeout=30):
    downloads = str(Path.home() / "Downloads")
    inicio = time.time()

    arquivos_antes = set(os.listdir(downloads))

    while True:
        arquivos_agora = set(os.listdir(downloads))
        novos = arquivos_agora - arquivos_antes

        # pega apenas XML novo
        xmls = [f for f in novos if f.endswith(".xml")]

        if xmls:
            for arquivo in xmls:
                origem = os.path.join(downloads, arquivo)
                destino_final = os.path.join(destino, arquivo)

                # espera terminar download real
                while True:
                    try:
                        with open(origem, "rb"):
                            break
                    except:
                        time.sleep(0.5)

                try:
                    shutil.move(origem, destino_final)
                    print(f"📁 Movido: {arquivo}")
                except Exception as e:
                    print(f"Erro ao mover: {e}")

            return True

        if time.time() - inicio > timeout:
            print("⚠️ Timeout esperando XML")
            return False

        time.sleep(1)


def rodar_bot(chaves, pasta_destino):
    print("🚀 Iniciando (modo coordenadas)")

    INPUT_X, INPUT_Y = -1446, 398
    BUSCAR_X, BUSCAR_Y = -1063, 408
    XML_X, XML_Y = -1184, 380
    qtd_sucesso = 0
    qtd_erro = 0
    chaves_erro = []

    for i, chave in enumerate(chaves, 1):
        try:
            print(f"\n🔎 [{i}/{len(chaves)}] {chave}")

            abrir_nova_aba()
            acessar_site()

            mover_e_clicar(INPUT_X, INPUT_Y)

            pyautogui.hotkey("ctrl", "a")
            pyautogui.press("backspace")

            digitar_chave(chave)

            mover_e_clicar(BUSCAR_X, BUSCAR_Y)

            time.sleep(2)

            mover_e_clicar(XML_X, XML_Y)
            pyautogui.press("enter")

            print("⏳ Aguardando download...")

            sucesso = esperar_e_mover_xml(pasta_destino)
            fechar_aba()

            if not sucesso:
                qtd_erro += 1
                chaves_erro.append(chave)
                print("❌ Não encontrou XML (pode ser bloqueio ou clique errado)")
            else:
                qtd_sucesso +=1

            delay(0.5, 1.2)

        except Exception:
            print("❌ Erro completo:")
            traceback.print_exc()

    print("\n🎯 Finalizado")

    return {
        "total": len(chaves),
        "sucessos": qtd_sucesso,
        "erros": qtd_erro,
        "chaves_erro": chaves_erro
    }