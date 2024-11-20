from pydantic import BaseModel, Field
from datetime import date
from typing_extensions import Self

class BookAdd (BaseModel):
 'Schema para ingresar un nuevo libro con la informacion de una obra literaria.'
 # id_book: int --> El id se ingresa de forma autoincremental.
 title: str
 release_year: date
 favorites_amount: int = Field(default=0)
 available_units: int
 image_url: str

class BookInfo (BaseModel):
 
 'Informacion que retorna para mostrar en la pagina de la obra en cuestion'

 id_book: int 
 title: str
 release_year: date
 favorites_amount: int
 available_units: int
 image_url: str

 class config:
        orm_mode: True






