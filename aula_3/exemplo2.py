#Conta Corrente Bancária - FastAPI
#Gerenciar saques e depósitos de clientes

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title='Conta Banária - Conta Corrente')

#Adicionar clientes
db_clientes = {
    'Joao':0,
    'Pedro':0,
    'Maria':0,
}

#Criar uma classe para as movimentações. OBS: usar pydantic para não acontecer erros
class Movimentacao(BaseModel):
    cliente:str = Field(..., description='Nome do cliente')
    valor:float = Field(...,gt=0, description='Valor da movimentação') # gt --> limitando o valor da entrada 

#Criando endpoint home
@app.get('/') #método para chamar os endpoints
def read_root():
    return{'message':'Conta Bancária - Conta Corrente'}

#Criar endpoint para consultar saldos
@app.post('/saldo') #método para chamar os endpoints
def saldo_cliente(cliente:str):
    return{'message':f'Saldo do cliente {cliente} é: {db_clientes[cliente]}'}

# Criar endpoint para realizar saques
@app.post('/saques') #método para chamar os endpoints
def saque_cliente(movimentacao: Movimentacao):
    db_clientes[movimentacao.cliente] -=movimentacao.valor
    return{'message':{'cliente':movimentacao.cliente, "valor": movimentacao.valor, 'saldo': db_clientes[movimentacao.cliente]}}

#Criar endpoint para realizar depósitos
@app.post('/deposito') #método para chamar os endpoints
def deposito_cliente(movimentacao: Movimentacao):
    db_clientes[movimentacao.cliente] += movimentacao.valor
    return{'message':{'cliente':movimentacao.cliente, "valor": movimentacao.valor, 'saldo': db_clientes[movimentacao.cliente]}}

#run
if __name__=='__main__':
    uvicorn.run('exemplo2:app', host='localhost', port=8000, reload=True) #host = próprio endereço / porta = 8000