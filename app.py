# from flask import Flask, request
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import os
# import pickle
# import json
# from itertools import chain

# #Import Packages
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# app=Flask(__name__)

# def download_selenum():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     driver.get("https://www.google.com/")
#     return { 'Title': driver.title }

# @app.route("/", methods=['GET','POST'])
# def home():
#     if (request.method == "GET"):
#         return download_selenum()
    
# if __name__ == '__main__':
#   app.run()
# # dd=download_selenum()
# # print(dd)


from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/automate', methods=['POST'])
def automate():
    data = request.get_json()

    if not data or 'target_url' not in data:
        return jsonify({'error': 'Missing target URL'}), 400

    target_url = data['target_url']

    try:
        # Configure headless Chrome for Railway deployment (security-conscious)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Optional for headless mode

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(target_url)
        title = driver.title
        driver.quit()

        return jsonify({'title': title})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
