# -*- coding: utf-8 -*-
"""
Created on Sun May  8 14:48:07 2022

@author: ObiraDaniel
"""

def main(dict):
    true = True
    if ('docs' in dict['body']['data']):
          return {'reviews':dict['body']['data']['docs'] }
true = True
test = {
  "body": {
    "data": {
      "bookmark": "g1AAAABweJzLYWBgYMpgSmHgKy5JLCrJTq2MT8lPzkzJBYorpKalmJoZpZmYG6aamKSamyWmGRgZWSYbGBsaW1iaW1iA9HHA9BGlIwsAjhUdew",
      "docs": [
        {
          "_id": "efd562f471e44e76af0229c0313738d2",
          "_rev": "1-6d3a316e140863cdb147048888d26051",
          "car_make": "Audi",
          "car_model": "A6",
          "car_year": 2010,
          "dealership": 15,
          "id": 1,
          "name": "Berkly Shepley",
          "purchase": true,
          "purchase_date": "07/11/2020",
          "review": "Total grid-enabled service-desk"
        },
        {
          "_id": "efd562f471e44e76af0229c031388dc7",
          "_rev": "1-38232a94989cf86c63135d7e85912a36",
          "car_make": "Lexus",
          "car_model": "IS F",
          "car_year": 2009,
          "dealership": 15,
          "id": 37,
          "name": "Albrecht Collen",
          "purchase": true,
          "purchase_date": "10/10/2020",
          "review": "Pre-emptive heuristic solution"
        }]}}}

print(main(test))