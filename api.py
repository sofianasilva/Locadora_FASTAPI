from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Locacao(BaseModel):
    data_inicial: datetime
    data_final: datetime
    carro: Carro 
    locador: Locador
    seguro: Seguro 

class Seguro(BaseModel):
    nome: str
    categoria: str
    cobertura: str
    valor: float

class Carro(BaseModel):
    modelo: str
    ano: int
    placa: str
    cor: str

class Pessoa(BaseModel):
    nome: str
    cpf: str       
    telefone: str
    endereco: Endereco

class Locador(Pessoa):
    salario: float

class Locatario(Pessoa):
    cnh: str    

class Endereco(BaseModel):
    logradouro: str
    numero: str
    cep: str
    bairro: str
    cidade: str
    estado: str
    complemento: str



