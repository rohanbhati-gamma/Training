# use for validations at run time
from typing import List
from pydantic import BaseModel, Field
#field for metadata and validation

class Student(BaseModel):
    id : int
    name : str = Field(None, title="Descritpion", max_length=10)
    subjects : List[str]

data = {
   'id': 1,
   'name': 'Ravikumar',
   'subjects': ["Eng", "Maths", "Sci"],
}

s1 = Student(**data)
print(s1)