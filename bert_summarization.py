from transformers import pipeline, BertTokenizerFast, EncoderDecoderModel
import torch
from documento import documento

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization')
model = EncoderDecoderModel.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization').to(device)

def resumo(doc):
    inputs = tokenizer([doc], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    output = model.generate(input_ids, attention_mask=attention_mask)
    return f" Resumo: {tokenizer.decode(output[0], skip_special_tokens = True)}"

resumo_documento = resumo(documento)
print(resumo_documento)