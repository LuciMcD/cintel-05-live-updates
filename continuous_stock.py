

import asyncio
from datetime import datetime
from pathlib import Path
import os
from random import randint

import pandas as pd
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
    return F




async def get_stock_price(ticker):
    logger.info("Calling get_stock_price for {ticker}")
   # api_key = get_API_key()
    #open_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=imperial"
    #logger.info(f"Calling fetch_from_url for {open_weather_url}")
    # result = await fetch_from_url(open_weather_url, "json")
    # logger.info(f"Data from openweathermap: {result}")
    # temp_F = data["main"]["temp"]
    price = randint(132, 148)
    return price 

"""
# Function to create or overwrite the CSV file with column headings
def init_csv_file(file_path):
    df_empty = pd.DataFrame(
        columns=["Location", "Latitude", "Longitude", "Time", "Temp_F"]
    )
    df_empty.to_csv(file_path, index=False)


async def update_csv_location():
    ""Update the CSV file with the latest location information.""
    logger.info("Calling update_csv_location")
    try:
        locations = ["ELY MN", "Death Valley CA", "Maryville MO"]
        update_interval = 60  # Update every 1 minute (60 seconds)
        total_runtime = 15 * 60  # Total runtime maximum of 15 minutes
        num_updates = 10  # Keep the most recent 10 readings
        logger.info(f"update_interval: {update_interval}")
        logger.info(f"total_runtime: {total_runtime}")
        logger.info(f"num_updates: {num_updates}")

        # Use a deque to store just the last, most recent 10 readings in order
        records_deque = deque(maxlen=num_updates)

        fp = Path(__file__).parent.joinpath("data").joinpath("mtcars_location.csv")

        # Check if the file exists, if not, create it with only the column headings
        if not os.path.exists(fp):
            init_csv_file(fp)

        logger.info(f"Initialized csv file at {fp}")

        for _ in range(num_updates):  # To get num_updates readings
            for location in locations:
                lat, long = lookup_lat_long(location)
                new_temp = await get_temperature_from_openweathermap(lat, long)
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current time
                new_record = {
                    "Location": location,
                    "Latitude": lat,
                    "Longitude": long,
                    "Time": time_now,
                    "Temp_F": new_temp,
                }
                records_deque.append(new_record)

            # Use the deque to make a DataFrame
            df = pd.DataFrame(records_deque)

            # Save the DataFrame to the CSV file, deleting its contents before writing
            df.to_csv(fp, index=False, mode="w")
            logger.info(f"Saving temperatures to {fp}")

            # Wait for update_interval seconds before the next reading
            await asyncio.sleep(update_interval)

    except Exception as e:
        logger.error(f"ERROR in update_csv_location: {e}")
        """ 
        
