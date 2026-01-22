from fastapi import FastAPI, UploadFile, Depends
import pandas as pd
from db import get_conn, init_db


app = FastAPI()

@app.on_event("startup")
def startup_event(conn=Depends(get_conn)):
    init_db(conn)

@app.post('/upload')
def upload_csv(file: UploadFile, conn=Depends(get_conn)):
    df = pd.read_csv(file.file)
    
    df['risk_level'] = pd.cut(
        df['range_km'], 
        bins=[0, 20, 100, 300, 600], 
        labels=['low', 'medium', 'high', 'extreme'],
        right=True,
        include_lowest=True)
    
    df['manufacturer'] = df['manufacturer'].fillna("Unknown")

    return {
        'mess': 'ok'
    }
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)