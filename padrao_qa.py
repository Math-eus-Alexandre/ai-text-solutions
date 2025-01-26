"""
modelo Q & A utilizando question-answering
"""

from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel
import torch
import logging
import documento



qa = pipeline("question-answering")

pergunta = "Qual a versao atual do Office?"
result = qa(question=pergunta,
            context=documento.documento,
            max_length=100)
print(f"Resposta: {result['answer']}\n")

