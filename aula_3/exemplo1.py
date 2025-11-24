from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title='FastAPI ASIMOV',
    description= 'Este é o exemplo 1 da aula 3 da ASIMOV',
    version= '0.1.0',
    contact={
        'name': 'Asimov',
        'email': 'asimov@example.com',
    },
)


@app.get('/') #método para chamar os endpoints
def read_root():
    return{'message':'Hello world'}

@app.get('/hello/{name}') #método para chamar os endpoints
def read_hello_name(name:str):
    return{'message':f'Hello {name}'}

if __name__=='__main__':
    uvicorn.run('exemplo1:app', host='localhost', port=8000, reload=True) #host = próprio endereço / porta = 8000