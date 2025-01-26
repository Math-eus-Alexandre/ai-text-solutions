from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel
import torch
import logging
import documento



resumo = pipeline("summarization")

result = resumo(documento.documento,
                max_length=150,
                min_length=50,
                do_sample=True)
print(f"Resumo: {result[0]['summary_text']}\n")