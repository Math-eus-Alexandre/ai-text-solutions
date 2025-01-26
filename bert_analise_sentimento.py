from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel



analise_sentimento = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

documento="Eu gostaria que parasse a tempestade! pois nao aguento mais"

resultados=analise_sentimento(documento)

def mapear_sentimento(label):
    estrelas = int(label.split()[0])
    if estrelas in [1, 2]:
        return "Negativo"
    elif estrelas == 3:
        return "Neutro"
    else:
        return "Positivo"
    
for idx, resultado in enumerate(resultados):
    sentimento = mapear_sentimento(resultado['label'])
    print(f'Texto {idx + 1}: {documento}')
    print(f'Classificacao: {sentimento} (Confianca: {resultado['score']:.2f})\n')