import openai
import my_key from ".env"

openai.api_key = my_key

def send(message): 
    answer = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": message}
        ]
    )
    
    return answer['choices'][0]['message']

while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break

print(send("Em que ano Einstein morreu?"))