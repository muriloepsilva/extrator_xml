from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import uuid
from io import BytesIO
from datetime import datetime
from bot import rodar_bot, criar_pasta_downloads

app = FastAPI()


@app.post("/upload-xlsx/")
async def upload_xlsx(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())

    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents), header=None)

        df = df.dropna()
        chaves = df.iloc[:, 0].astype(str).tolist()

        if not chaves:
            raise HTTPException(status_code=400, detail="Arquivo vazio")

        print(f"[{file_id}] Total: {len(chaves)}")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pasta_execucao = criar_pasta_downloads(f"xmls_{timestamp}")

        resultado = rodar_bot(chaves, pasta_execucao)

        return resultado

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))