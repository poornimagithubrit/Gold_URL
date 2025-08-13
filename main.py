from fastapi import FastAPI
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Gold Data API")

# Enable CORS for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Gold Data API is running"}

@app.get("/gold-data")
def get_gold_data():
    df = pd.read_csv("njl_sales_report_sample_1000.csv")
    return df.to_dict(orient="records")
