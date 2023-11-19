# -*- coding: utf-8 -*-
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from tokenizers import SentencePieceBPETokenizer


def question_generator(context):
    # 토크나이저 불러오기
    tokenizer = SentencePieceBPETokenizer.from_file(vocab_filename="tokenizer/vocab.json", merges_filename="tokenizer/merges.txt", add_prefix_space=False)
    # 모델 불러오기
    model = GPT2LMHeadModel.from_pretrained("taeminlee/kogpt2")

    # 가중치 불러오기
    weights = torch.load('QG_kogpt2.pth', map_location=torch.device('cpu'))

    # 불러온 가중치 중 모델의 키와 일치하는 가중치만 선택
    weights = {k: v for k, v in weights.items() if k in model.state_dict()}

    # 모델에 가중치 적용
    model.load_state_dict(weights, strict=False)

    encoded_context = tokenizer.encode(context)
    inputs = torch.tensor([encoded_context.ids])
    attention_mask = torch.tensor([[1] * len(inputs[0])])
    eos_token_id = tokenizer.token_to_id("</s>")
    max_length = len(inputs[0]) + 200  # 인풋 길이 설정
    outputs = model.generate(inputs, attention_mask=attention_mask, pad_token_id=eos_token_id, max_length=max_length, num_return_sequences=1, num_beams=1)

    output_str  = tokenizer.decode(outputs[-1].tolist(), skip_special_tokens=True)

    # 정답 추출
    answer = output_str.split("정답:")[1].split("질문:")[0].strip()

    # 질문 추출
    question = output_str.split("질문:")[1].split("</s>")[0].strip()

    return answer, question
