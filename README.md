# 🤖 Bot de Download de XML (NFe) + API com FastAPI

Este projeto automatiza o download de arquivos XML de notas fiscais (NFe) a partir de uma lista de chaves em um arquivo Excel (.xlsx), utilizando automação com `pyautogui` e disponibilizando uma API com `FastAPI`.

---

## 🚀 Funcionalidades

* Upload de arquivo `.xlsx` com chaves de NFe
* Automação de navegação no site https://www.meudanfe.com.br
* Download automático dos XMLs
* Organização dos arquivos em pasta dentro de `Downloads`
* Retorno via API com:

  * Total processado
  * Sucessos
  * Erros
  * Lista de chaves com erro

---

## 🧰 Requisitos

* Python 3.10 ou superior
* Navegador aberto (Chrome ou Edge)
* Sistema operacional: Windows (recomendado)

---

## 📥 1. Instalação do Python

1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente
3. Durante a instalação:

   * ✅ Marque **"Add Python to PATH"**
   * Clique em **Install Now**

Para verificar:

```bash
python --version
```

---

## 📦 2. Clonar ou baixar o projeto

```bash
git clone <seu-repositorio>
cd <seu-repositorio>
```

Ou apenas extraia o `.zip` do projeto.

---

## 🧪 3. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
```

Ativar:

### Windows:

```bash
venv\Scripts\activate
```

---

## 📚 4. Instalar dependências

```bash
pip install fastapi uvicorn pandas pyautogui pyperclip openpyxl
```

---

## 🖥️ 5. Preparação do ambiente (IMPORTANTE)

### ⚠️ Antes de rodar:

* Abra o navegador manualmente
* Não minimize a janela
* Mantenha o navegador visível
* Não mexa no mouse/teclado durante execução

---

### 🖱️ Ajustar coordenadas

No arquivo `bot.py`, ajuste conforme sua tela:

```python
INPUT_X, INPUT_Y = -1446, 398
BUSCAR_X, BUSCAR_Y = -1063, 408
XML_X, XML_Y = -1184, 380
```

📌 Dica:
Use este script para descobrir coordenadas:

```python
import pyautogui
print(pyautogui.position())
```

---

## ▶️ 6. Executar a API

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 7. Acessar Swagger

Abra no navegador:

```
http://127.0.0.1:8000/docs
```

---

## 📤 8. Como usar

1. Clique em **POST /upload-xlsx/**
2. Clique em **Try it out**
3. Envie um arquivo `.xlsx` com as chaves na primeira coluna
4. Execute

---

## 📄 Formato do Excel

| Coluna A |
| -------- |
| 3519...  |
| 3520...  |

* Sem cabeçalho
* Apenas as chaves

---

## 📊 Resposta da API

```json
{
  "total": 10,
  "sucessos": 8,
  "erros": 2,
  "chaves_erro": ["3519...", "3520..."]
}
```

---

## 📁 Onde os arquivos são salvos

Os XMLs são armazenados em:

```
C:\Users\SEU_USUARIO\Downloads\xmls_<DATA_HORA>
```

---

## 🧠 Dicas importantes

* Não use o computador durante a execução
* Evite múltiplos monitores (ou ajuste coordenadas)
* Caso pare de funcionar, revise os cliques

---

## 👨‍💻 Autor

Projeto desenvolvido para automação de coleta de XMLs de NFe por Murilo Eduardo Penha Silva.

---