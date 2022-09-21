#!/usr/bin/env python
import os
import requests
api_key = os.environ[‘API_KEY’]response = requests.get("https://thedogapi.com/v1/breeds?api_key={}".format(api_key))
print(response)
