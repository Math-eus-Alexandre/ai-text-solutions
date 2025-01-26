from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel
import documento

qa = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
pergunta = "Qual a ultima versao do Office?"
result = qa(question=pergunta,
            context=documento.documento,
            max_lengh=100)

print(f'Resposta: {result['answer']}\n')