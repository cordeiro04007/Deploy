#IMPORTS 
import requests
import json
from pprint import pprint

AGENT_ID = 'Agente_PDF'
ENDPOINT = f'http://localhost:7777/agents/{AGENT_ID}/runs'

#CONEXÃO COM AGNO
def get_response_stream(message: str):
    response = requests.post(
        url= ENDPOINT,
        data= {
            'message': message,
            'stream': 'true',
        },
        stream= True
    )

    #STREAMING (PROCESSAMENTO)
    for line in response.iter_lines():
        if line:
            #Pase Server-Sent Events
            if line.startswith(b'data: '):
                data = line[6:]
            yield json.loads()




#PRINTA A RESPOSTA

#RUN (LOOP)
if __name__=='__main__':
    message = input('Digite uma mensagem: ')
    response = get_response_stream(message)
    print(response)
