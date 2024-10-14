from pydantic import BaseModel
from datetime import date
from typing_extensions import Self

class BookAdd (BaseModel):
 'Schema para ingresar un nuevo libro con la informacion de una obra literaria.'
 # id_book: int --> El id se ingresa de forma autoincremental.
 title: str
 release_year: date
 favorites_amount: int | 0
 available_units: int

class BookInfo (BaseModel):
 
 'Informacion que retorna para mostrar en la pagina de la obra en cuestion'

 id_book: int 
 title: str
 release_year: date
 favorites_amount: int
 available_units: int





