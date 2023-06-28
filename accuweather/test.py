from pprint import pprint
import logging
import sys
from get import AccuweatherGETAPIHandler

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

api_key = ""

get_class = AccuweatherGETAPIHandler(apikey=api_key)
city = "helsinki"
city_data = get_class.get_city(city=city)

city_key = city_data[0]["Key"]

weather = get_class.get_weather(key=city_key)
pprint(weather)


"""
CITY DATA
[{'AdministrativeArea': {'CountryID': 'FI',
                         'EnglishName': 'Uusimaa',
                         'EnglishType': 'Region',
                         'ID': '18',
                         'Level': 1,
                         'LocalizedName': 'Uusimaa',
                         'LocalizedType': 'Region'},
  'Country': {'EnglishName': 'Finland', 'ID': 'FI', 'LocalizedName': 'Finland'},
  'DataSets': ['AirQualityCurrentConditions',
               'AirQualityForecasts',
               'Alerts',
               'DailyPollenForecast',
               'ForecastConfidence',
               'FutureRadar',
               'MinuteCast',
               'Radar'],
  'EnglishName': 'Helsinki',
  'GeoPosition': {'Elevation': {'Imperial': {'Unit': 'ft',
                                             'UnitType': 0,
                                             'Value': 85.0},
                                'Metric': {'Unit': 'm',
                                           'UnitType': 5,
                                           'Value': 26.0}},
                  'Latitude': 60.17,
                  'Longitude': 24.939},
  'IsAlias': False,
  'Key': '133328',
  'LocalizedName': 'Helsinki',
  'PrimaryPostalCode': '',
  'Rank': 30,
  'Region': {'EnglishName': 'Europe', 'ID': 'EUR', 'LocalizedName': 'Europe'},
  'SupplementalAdminAreas': [{'EnglishName': 'Helsingin',
                              'Level': 2,
                              'LocalizedName': 'Helsingin'}],
  'TimeZone': {'Code': 'EEST',
               'GmtOffset': 3.0,
               'IsDaylightSaving': True,
               'Name': 'Europe/Helsinki',
               'NextOffsetChange': '2023-10-29T01:00:00Z'},
  'Type': 'City',
  'Version': 1},
 {'AdministrativeArea': {'CountryID': 'FI',
                         'EnglishName': 'Southwest Finland',
                         'ID': '19',
                         'Level': 1,
                         'LocalizedName': 'Southwest Finland',
                         'LocalizedType': 'Region'},
  'Country': {'EnglishName': 'Finland', 'ID': 'FI', 'LocalizedName': 'Finland'},
  'DataSets': ['AirQualityCurrentConditions',
               'AirQualityForecasts',
               'Alerts',
               'DailyPollenForecast',
               'ForecastConfidence',
               'MinuteCast',
               'Radar'],
  'EnglishName': 'Helsinki',
  'GeoPosition': {'Elevation': {'Imperial': {'Unit': 'ft',
                                             'UnitType': 0,
                                             'Value': 0.0},
                                'Metric': {'Unit': 'm',
                                           'UnitType': 5,
                                           'Value': 0.0}},
                  'Latitude': 60.6,
                  'Longitude': 21.433},
  'Key': '1121116',
  'LocalizedName': 'Helsinki',
  'PrimaryPostalCode': '',
  'Rank': 600,
  'Region': {'EnglishName': 'Europe', 'ID': 'EUR', 'LocalizedName': 'Europe'},
  'SupplementalAdminAreas': [{'EnglishName': 'Vakka-Suomen',
                              'Level': 2,
                              'LocalizedName': 'Vakka-Suomen'}],
  'TimeZone': {'Code': 'EEST',
               'GmtOffset': 3.0,
               'IsDaylightSaving': True,
               'Name': 'Europe/Helsinki',
               'NextOffsetChange': '2023-10-29T01:00:00Z'},
  'Type': 'City',
  'Version': 1}]



WEATHER DATA
{'DailyForecasts': [{'Date': '2023-06-28T07:00:00+03:00',
                     'Day': {'HasPrecipitation': True,
                             'Icon': 13,
                             'IconPhrase': 'Mostly cloudy w/ showers',
                             'PrecipitationIntensity': 'Moderate',
                             'PrecipitationType': 'Rain'},
                     'EpochDate': 1687924800,
                     'Link': 'http://www.accuweather.com/en/fi/helsinki/133328/daily-weather-forecast/133328?day=1&lang=en-us',
                     'MobileLink': 'http://www.accuweather.com/en/fi/helsinki/133328/daily-weather-forecast/133328?day=1&lang=en-us',
                     'Night': {'HasPrecipitation': True,
                               'Icon': 41,
                               'IconPhrase': 'Partly cloudy w/ t-storms',
                               'PrecipitationIntensity': 'Light',
                               'PrecipitationType': 'Rain'},
                     'Sources': ['AccuWeather'],
                     'Temperature': {'Maximum': {'Unit': 'F',
                                                 'UnitType': 18,
                                                 'Value': 79.0},
                                     'Minimum': {'Unit': 'F',
                                                 'UnitType': 18,
                                                 'Value': 61.0}}}],
 'Headline': {'Category': 'thunderstorm',
              'EffectiveDate': '2023-06-29T08:00:00+03:00',
              'EffectiveEpochDate': 1688014800,
              'EndDate': '2023-06-29T20:00:00+03:00',
              'EndEpochDate': 1688058000,
              'Link': 'http://www.accuweather.com/en/fi/helsinki/133328/daily-weather-forecast/133328?lang=en-us',
              'MobileLink': 'http://www.accuweather.com/en/fi/helsinki/133328/daily-weather-forecast/133328?lang=en-us',
              'Severity': 3,
              'Text': 'Thunderstorms Thursday'}}
"""