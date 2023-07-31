

import asyncio
from datetime import datetime
from pathlib import Path
import os
from random import randint

import pandas as pd
import yfinance as yf
from collections import deque
from dotenv import load_dotenv


from fetch import fetch_from_url
from util_logger import setup_logger


logger, log_filename = setup_logger(__file__)


def get_API_key():
    load_dotenv()
    key = os.getenv("OPEN_STOCK_API_KEY")
    return key


def lookup_ticker(company):
    stocks_dictionary = {
        "Tesla Inc": "TSLA",
        "General Motors Company": "GM",
        "Toyota Motor Corporation": "TM",
        "Ford Motor Company": "F",
        "Honda Motor Co": "HMC",
    },
    company = stocks_dictionary[company],
    return company




async def get_stock_price(ticker):
    logger.info("Calling get_stock_price for {ticker}")
   # api_key = get_API_key()
    #open_stock_url = f"https://query1.finance.yahoo.com/v7/finance/options/MSTR"
    #logger.info(f"Calling fetch_from_url for {open_stock_url}")
    # result = await fetch_from_url(open_stock_url, "json")
    # logger.info(f"Data from yahoo finance: {result}")
    # price = data["main"]["price"]
    price = randint(132, 148)
    return price 

def init_csv_file(file_path):
    df_empty = pd.DataFrame(
        columns=["Company", "Ticker", "Time", "Price"]
    )
    df_empty.to_csv(file_path, index=False)


async def update_csv_stock():
    logger.info("Calling update_csv_stock")
    try:
        file_path = Path(__file__).parent.joinpath("data").joinpath("mtcars_stok.csv")
       
        if not os.path.exists(file_path):
            df_empty = pd.DataFrame(
                columns=["Company", "Ticker", "Time", "Price"]
        ).copy()
            df_empty.to_csv(file_path, index=False)

        df_data = pd.DataFrame({
            "Company": ["Tesla Inc", "General Motors Company"],
            "Ticker": ["TSLA", "GM"],
            "Time": ["2023-07-25 12:00:00", "2023-07-25 12:01:00"],
            "Price": [700.0, 60.0]
        })

        logger.info(f"Saving stock prices to {file_path}")
        df_data.to_csv(file_path, index=False)
    except Exception as e:
        logger.error(f"An error occurred in update_csv_stock: {e}")
        
        
