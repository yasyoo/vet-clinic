from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import Optional, List, Dict
from enum import Enum

app = FastAPI()


# Перечисление типов собак
class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


# Модель собаки
class Dog(BaseModel):
    pk: Optional[int] = None
    name: str
    kind: DogType


# Модель временной метки
class Timestamp(BaseModel):
    id: int
    timestamp: int


# Исходные данные (предзаполнены)
dogs_db: Dict[int, Dog] = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}
next_pk = max(dogs_db.keys()) + 1

post_db: List[Timestamp] = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get("/")
def root():
    return {"message": "Hello, this is the root endpoint"}


@app.post("/post", response_model=Timestamp)
def get_post():
    return post_db[-1]  # возвращаем последний элемент


@app.get("/dog", response_model=List[Dog])
def get_dogs(kind: Optional[DogType] = Query(None)):
    if kind:
        return [dog for dog in dogs_db.values() if dog.kind == kind]
    return list(dogs_db.values())


@app.post("/dog", response_model=Dog)
def create_dog(dog: Dog):
    global next_pk
    dog.pk = next_pk
    dogs_db[next_pk] = dog
    next_pk += 1
    return dog


@app.get("/dog/{pk}", response_model=Dog)
def get_dog_by_pk(pk: int = Path(...)):
    if pk in dogs_db:
        return dogs_db[pk]
    raise HTTPException(status_code=404, detail="Dog not found")


@app.patch("/dog/{pk}", response_model=Dog)
def update_dog(pk: int, updated_dog: Dog):
    if pk not in dogs_db:
        raise HTTPException(status_code=404, detail="Dog not found")
    updated_dog.pk = pk
    dogs_db[pk] = updated_dog
    return updated_dog