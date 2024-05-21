
# Address Book API

## Description
A FastAPI application for managing addresses with SQLite. Supports creating, updating, deleting, and retrieving addresses based on distance and coordinates.

## Requirements
- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
- Geopy

## Installation
1. Clone the repository:
    ```sh
    git clone 
    cd address_book
    ```

2. Install dependencies:
   '''
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    uvicorn app:app --reload or python run app.py
    ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`



## RUNNING VIA DOCKER
1. clone the repo
2. cd addressbook
sudo docker build -t 'address_api' .
sudo docker run -dp 8000:8000 -t address_api
Access the API documentation at `http://0.0.0.0:8000/docs`
