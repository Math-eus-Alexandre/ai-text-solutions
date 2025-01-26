from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel
import torch
import logging
import documento


analisde_sentimento = pipeline("sentiment-analysis")
paragrafo = "Eu gostaria de trabalhar na Microsoft, pois acredito que é uma empresa inovadora e que valoriza seus funcionários."

result = analisde_sentimento(paragrafo)

for idx, sentimento in enumerate(result):
    print(f'Frase {idx + 1}: {sentimento}\n')