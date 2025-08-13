from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

# Load CSV once at startup
CSV_FILE = "njl_sales_report_sample_1000.csv"
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"{CSV_FILE} not found in project root")

df = pd.read_csv(CSV_FILE)

app = FastAPI(title="Gold Data API", description="Public JSON API for gold sales", version="1.0")

@app.get("/")
def root():
    return {"message": "Gold Data API - use /data to get the CSV contents as JSON."}

@app.get("/data")
def get_data():
    return JSONResponse(content=df.to_dict(orient="records"))

@app.get("/filter")
def filter_data(city: str = None, category: str = None):
    filtered_df = df.copy()
    if city:
        filtered_df = filtered_df[filtered_df['City'].str.lower() == city.lower()]
    if category:
        filtered_df = filtered_df[filtered_df['Master Category'].str.lower() == category.lower()]
    return JSONResponse(content=filtered_df.to_dict(orient="records"))

@app.get("/summary")
def summary():
    total_sales = df["Net Sales Value [INR]"].sum()
    avg_price = df["Cost Price [INR]"].mean()
    return {
        "total_sales_inr": total_sales,
        "average_cost_price_inr": avg_price
    }

