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

def esperar_e_mover_xml(destino, timeout=30):
    downloads = str(Path.home() / "Downloads")
    inicio = time.time()

    while True:
        for arquivo in os.listdir(downloads):
            if arquivo.endswith(".xml"):
                origem = os.path.join(downloads, arquivo)
                print(origem)
                destino_final = os.path.join(destino, arquivo)
                print(destino_final)

                try:
                    tamanho1 = os.path.getsize(origem)
                    time.sleep(0.5)
                    tamanho2 = os.path.getsize(origem)

                    if tamanho1 != tamanho2:
                        continue
                except:
                    continue

                try:
                    shutil.move(origem, destino_final)
                    print(f"📁 Movido: {arquivo}")
                    return True
                except Exception as e:
                    print(f"Erro ao mover: {e}")
                    return False

        if time.time() - inicio > timeout:
            print("⚠️ Timeout esperando XML")
            return False

        time.sleep(0.5)


def rodar_bot(chaves, pasta_destino):
    print("🚀 Iniciando (modo coordenadas)")

    INPUT_X, INPUT_Y = 501, 399
    BUSCAR_X, BUSCAR_Y = 896, 409
    XML_X, XML_Y = 630, 370
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

            time.sleep(5)

            mover_e_clicar(XML_X, XML_Y)

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