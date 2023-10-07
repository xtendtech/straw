from fastapi.params import Body
from fastapi import FastAPI

app=FastAPI()
@app.get('/')
async def main():
    return{"hello":"World"}

@app.get("/post")
def get_post():
    return{"post":"this is my post"}
@app.post("/createpost")
def create_post(payload : dict = Body(...)):
 
    # print(payload)
    return{"new_post": f"{payload['title']  ,payload['content']}"}
    #  return{"post":"this is my post"}
 
 

# if (__name__ = '__main__'):
