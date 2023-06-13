# Kiana's Cookbook

This project is a proof of concept for a recipe repository app. It allows you to input any recipe URL from the internet and organize it within your own cookbook. The site will extract the recipe from the web page and discard any non-recipe related content.

## How to run the backend
To run the backend, cd into KCB-be and install the dependencies. You can use a virtual environment if you desire.
```
cd KCB-be
python3 -m pip install -r requirements.txt
```
The api uses fastapi which requires an ASGI server. I use uvicorn for this project, which should be included in the dependencies. To run the api:
```
python -m uvicorn main:app
```
This will run the app using 127.0.0.1:8000 by default.

## How to host the frontend
You can build and host the frontend locally using npm.
```
cd KCB-fe
npm install
npm run dev
```

You can also run the unit tests.
```
npm run test:unit
```
