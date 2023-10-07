import json
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
class Person(BaseModel):
    pid:Optional[int]=None,
    name:str
    age:int
    gender:Optional[str]
with open('people.json','r' )as f:
    people= json.load(f)['people']
# print(people)     

@app.get('/person/{p_id}',status_code=200)
async def get_person (p_id:int):
    # print(p_id)
    person= [ p for p in people if p['pid'] == p_id]
    print(len(person))
    return person[0] if len(person) > 0 else {}
@app.get('/search')
def search_person(age:Optional[int]=Query(None,title='Age',description="age of person"),
                  name:Optional[str]=Query(None,title="name",description="nameof person")):
    people1= [ p for p in people if p['age'] == age]
    # print(name,age,people1)
    if name is None:
        if age is None:
            return people
        else:
            print(people1,age)
            return people1
    else:
        people2= [p for p in people if name.lower() in p['name'].lower() ]  
        # print(people1,people2,age)
        if age is None:
            print(people1,people2,age)
            return people2
        else:
            print(people1,people2,age)
            combined=[p for p in people1 if p in people2]
            return combined

        
    return people[0]
@app.post('/addPerson', status_code=201)
def add_persons(person:Person):
    print("start")
    p_id= max([p['id'] for p in people ]) +1
    print(p_id)
    # new_person={
    #     "id":p_id,
    #     "name":person.name,
    #     "age":person.age
    # }

    # people.append(new_person)
    # print(new_person)
    # # with open('people.json','w') as f:
    # #     json.dumps(people,f)
    return new_person