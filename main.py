from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.middleware("http")(timing_middleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(issues_router)



# items = [
#   {"id": 1, "name": "Item 1"},
#   {"id": 2, "name": "Item 2"},
#   {"id": 3, "name": "Item 3"},
# ]

# @app.get("/health")
# def health_check():
#   return {"status": "ok"}

# @app.get("/items/")
# def get_items():
#   return items

# @app.get("/query/")
# def get_query(skip: int = 0, limit : int = 0):
#   return f"skip is {skip} and limit is {limit}"

# @app.get("/items/{item_id}/")
# def get_item(item_id: int):
#   for item in items:
#     if item["id"] == item_id:
#       return item
#   return {"error": "Item not found"}

# @app.post("/items/")
# def add_item(item: dict):
#   items.append(item)
#   return item

# @app.put("/items/{item_id}/")
# def update_item(item_id: int, item: dict):
#   for i in range(len(items)):
#     if items[i]["id"] == item_id:
#       items[i] = item
#       return item
#   return {"error": "Item not found"}

