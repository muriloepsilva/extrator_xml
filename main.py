from fastapi import FastAPI, UploadFile, File, HTTPException, Body
import pandas as pd
import uuid
from io import BytesIO
from datetime import datetime
import json

from bot import rodar_bot, criar_pasta_downloads

app = FastAPI()


@app.post("/processar/")
async def processar(
    file: UploadFile = File(None),
    chaves: str = Body(default=None)
):
    file_id = str(uuid.uuid4())

    try:
        lista_chaves = []

        if file:
            contents = await file.read()
            df = pd.read_excel(BytesIO(contents), header=None)

            df = df.dropna()
            lista_chaves = df.iloc[:, 0].astype(str).tolist()

        elif chaves:
            chaves = chaves.strip()

            if chaves.startswith("["):
                try:
                    lista_chaves = json.loads(chaves)

                    if not isinstance(lista_chaves, list):
                        raise ValueError()

                except:
                    raise HTTPException(
                        status_code=400,
                        detail="JSON inválido"
                    )

            else:
                lista_chaves = [
                    c.strip() for c in chaves.split(",") if c.strip()
                ]

        else:
            raise HTTPException(
                status_code=400,
                detail="Envie um arquivo ou uma lista de chaves"
            )

        lista_chaves = [str(c) for c in lista_chaves]

        if not lista_chaves:
            raise HTTPException(
                status_code=400,
                detail="Nenhuma chave válida"
            )

        print(f"[{file_id}] Total: {len(lista_chaves)}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pasta_execucao = criar_pasta_downloads(f"xmls_{timestamp}")

        resultado = rodar_bot(lista_chaves, pasta_execucao)

        return resultado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))