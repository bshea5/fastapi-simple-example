Re-work of previous simple fastapi app using sqlmodel.

Requirments:
* Python 3.7+
* Pip


Create python virtual enviroment
> py -m venv env


If using VSCode, set Python interpreter path if it doesn't already pickup the virtual env.


Activate enviroment
> .\env\Scripts\activate (Windows)

> pip install -r requirements.txt

Start server
> uvicorn main:app --reload

For VSCode, I've set it up to start on 'F5' command.

OpenAPI(Swagger): http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

