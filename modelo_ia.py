from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Cargar el modelo preentrenado y el tokenizador
modelo = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizador = GPT2Tokenizer.from_pretrained('gpt2')

def responder_pregunta(pregunta):
    entradas = tokenizador.encode(pregunta, return_tensors='pt')
    salida = modelo.generate(entradas, max_length=50, num_return_sequences=1)
    respuesta = tokenizador.decode(salida[0], skip_special_tokens=True)
    return respuesta