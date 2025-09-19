from typing import List #to define option in list
from pydantic import BaseModel,Field,validator # to define and validate our models

class MCQQuestion(BaseModel):
    question: str = Field(description="The question text")
    options: List[str] =Field(description="List of 4 options")
    correct_answer: str = Field(description="The correct answer from the options")

    @validator('question',pre=True) #used to clean or fix the input before assigning it. #llm gives response in strings or dictionary
    def clean_question(cls,v): #if llm response of question is dictionary,how we will extract those questions(that is the use of validator) ,like 1
        if isinstance(v,dict):
            return v.get('description',str(v)) # get only string
        return str(v)


class FillBlankQuestion(BaseModel):
    question: str = Field(description="The question text with '___' for the blank")
    answer: str=Field(description="The correct word or phrase for the blank")

    @validator('question',pre=True) #used to clean or fix the input before assigning it. #llm gives response in strings or dictionary
    def clean_question(cls,v): #if llm response of question is dictionary,how we will extract those questions(that is the use of validator) ,like 1
        if isinstance(v,dict):
            return v.get('description',str(v)) # get only string
        return str(v)
    
'''
Schemas means data structure how your question should be passed by the llm,so that you can see the results in a more proper way'''
'''
  #1
  "question" : "What is your name?"

  "options"
'''

'''
@validator('question', pre=True)

Pydantic will call this method before normal parsing happens for the question field.

This is useful when the raw input might not be in the right format.

Function signature:

cls is the model class (MCQQuestion).

v is the value passed for question when constructing the model.

Logic:

If v is a dictionary → try to extract the "description" key.

Example: {"description": "What is 2+2?"} → becomes "What is 2+2?".

If "description" doesn’t exist, fall back to str(v) (convert dict to string).

Otherwise → force v into a string.

pre=True

Your validator runs first, before Pydantic does any conversions.
'''

'''
q = MCQQuestion(
    question={"description": "Capital of France"},
    options=["Berlin", "London", "Paris", "Rome"],
    correct_answer="Paris"
)
question is a dict.

Validator sees that → returns "Capital of France".

✅ Model is created successfully.
'''