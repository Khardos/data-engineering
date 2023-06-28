import requests
import json
import logging


class AccuweatherGETAPIHandler:
    def __init__(self, apikey):
        self.apikey = apikey
        self.base_url = "http://dataservice.accuweather.com"
        
    def get_data(self, endpoint, params):
        params["apikey"] = self.apikey
        url = self.base_url + endpoint
        data = requests.get(url=url, params=params)
        if data.status_code != 200:
            logging.error(data.status_code)
            logging.error(data.text)
        else:
            logging.info("Request succesful.")
        data = json.loads(data.text)
        return data
        
    def get_city(self, city: str):
        logging.info(f"Searching for city: {city}")
        endpoint = "/locations/v1/cities/search"
        params = {
            "q": city
        }
        data = self.get_data(endpoint=endpoint, params=params)
        return data
        
    def get_weather(self, key):
        logging.info(f"Getting daily weather summary for key: {key}")
        endpoint = f"/forecasts/v1/daily/1day/{key}"
        params = {}
        data = self.get_data(endpoint=endpoint, params=params)
        return data