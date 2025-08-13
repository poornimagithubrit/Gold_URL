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

# Path to your CSV file
CSV_FILE = "gold_prices.csv"

@app.get("/")
def home():
    return {"message": "Gold Data API is running"}

@app.get("/gold-data")
def get_gold_data():
    """
    Returns the CSV data as JSON so Copilot Studio can consume it.
    """
    try:
        df = pd.read_csv(CSV_FILE)
        return JSONResponse(content=df.to_dict(orient="records"))
    except Exception as e:
        return {"error": str(e)}
