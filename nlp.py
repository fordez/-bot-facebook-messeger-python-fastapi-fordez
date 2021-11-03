from transformers import AutoTokenizer
from transformers import AutoModelForQuestionAnswering
from transformers import pipeline

the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)

contexto = 'catalogo = 2, carrito = 3'
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)


def pregunta_respuesta(model, contexto, nlp):
    print('Contexto:')
    print('-------------------------')
    print(contexto)

    continuar = True
    while continuar:
        print('\nPregunta:')
        print('-------------------------')
        pregunta = str(input())

        continuar = pregunta != ''

        if continuar:
            salida = nlp({'question': pregunta, 'context': contexto})
            print('\nRespuesta:')
            print('-------------------------')
            print(salida['answer'])


pregunta_respuesta(model, contexto, nlp)
