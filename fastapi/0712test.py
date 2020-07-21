from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id:int,q:str = None):
    return {"item_id":item_id , "q":q}

@app.get("/apps/haomacejixiong/ios")
def haomacejixiong_ios():
    return "https://apps.apple.com/us/app/id1206856799"


