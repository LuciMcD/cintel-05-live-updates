

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
    company_dictionary = {
        "Tesla Inc": {"TSLA"},
        "General Motors Company": {"GM"},
        "Toyota Motor Corporation": {"TM"},
        "Ford Motor Company": {"F"},
        "Honda Motor Co": {"HMC"},
    },
    ticker = company_dictionary[company]
    return ticker




async def get_stock_price(ticker):
    logger.info("Calling get_stock_price for {ticker}")
    api_key = get_API_key()
    stock_api_url = f"https://query1.finance.yahoo.com/v7/finance/options/{ticker}"
    logger.info(f"Calling fetch_from_url for {stock_api_url}")
    result = await fetch_from_url(stock_api_url, "json")
    #result = pd.read_csv("mtcars_stock_csv : {Price}") #Adding this to bypass API and URL
    logger.info(f"Data for {ticker}: {result}")
    price = result.data['optionChain']['result'][0]['quote']['regularMarketPrice']
    #price = randint(132, 148)
    return price 

def init_csv_file(file_path):
    df_empty = pd.DataFrame(columns=["Company", "Ticker", "Time", "Price"])
    df_empty.to_csv(file_path, index=False)


async def update_csv_stock():
    logger.info("Calling update_csv_stock")
    try:
        companies = [
            "Tesla Inc",
            "General Motors Company",
            "Toyota Motor Corporation",
            "Ford Motor Company",
            "Honda Motor Co"
        ]
        update_interval =60
        total_runtime = 15 * 60
        num_updates = 50
        logger.info(f"update_interval: {update_interval}")
        logger.info(f"total_runtime: {total_runtime}")
        logger.info(f"num_updates: {num_updates}")

        records_deque = deque(maxlen=num_updates)

        fp = Path(__file__).parent.joinpath("data").joinpath("mtcars_stock.csv")
       
        if not os.path.exists(fp):
            init_csv_file(fp)

        logger.info(f"Initialized csv file at {fp}")

        for _ in range(num_updates):
            for company in companies:
                ticker = lookup_ticker(company)
                new_price = await get_stock_price(ticker)
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_record = {
                    "Company": company,
                    "Ticker": ticker,
                    "Time": time_now,
                    "Price": new_price,
                }
                records_deque.append(new_record)

            df = pd.DataFrame(records_deque)
            
            df.to_csv(fp, index=False, mode="w")
            logger.info(f"Saving stock prices to {fp}")
             
        await asyncio.sleep(update_interval)
        
    except Exception as e:
        logger.error(f"An error occurred in update_csv_stock: {e}")

        