# FAST API exercise

This is a simple exercise to learn how to use Fast API. It is a simple API that handles CRUD of a list of issues. It also has a middleware that adds a header with the processing time of the request.

## How to run locally
1. Clone the repository
```bash
$ git clone https://github.com/thedivloop/fastapi.git
```   
2. Install the dependencies
```bash
$ cd fastapi
$ pip install -r requirements.txt
```
3. Run the application
```bash
$ fastapi dev main.py 
```

## Swagger UI
You can access the Swagger UI at `http://localhost:8000/docs` to interact with the API endpoints.

## Credits
This is based on a youtube [video](https://youtu.be/8TMQcRcBnW8?is=LCsSTVW8rod8bmD8) by Brad Traversy, Traversy Media®.