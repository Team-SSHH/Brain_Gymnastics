# -*- coding: utf-8 -*-

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from tokenizers import SentencePieceBPETokenizer


# 토크나이저를 불러옵니다.
tokenizer = SentencePieceBPETokenizer.from_file(vocab_filename="tokenizer/vocab.json", merges_filename="tokenizer/merges.txt", add_prefix_space=False)
# tokenizer = GPT2Tokenizer.from_pretrained("taeminlee/kogpt2")

# 모델을 불러옵니다.
# model = GPT2LMHeadModel.from_pretrained("csi9876/brain", use_auth_token="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")
model = GPT2LMHeadModel.from_pretrained("taeminlee/kogpt2")
# 미리 학습된 가중치를 불러옵니다.
weights = torch.load('QG_kogpt2.pth', map_location=torch.device('cpu'))

# 불러온 가중치 중 모델의 키와 일치하는 가중치만 선택
# weights = {k: v for k, v in weights.items() if k in model.state_dict()}

# 가중치를 모델에 적용합니다.
model.load_state_dict(weights, strict=False)


# model = torch.load('brain.pth')

# torch.save(model, 'brain.pth')
context = "애플의 근거리무선통신(NFC) 결제 서비스 ‘애플페이’가 21일 한국에 상륙했다. NFC 단말기가 설치된 편의점과 프랜차이즈 카페 등에서, 현대카드로만 쓸 수 있어 초기 사용은 제한적인 편이다."
context1 = "LG유플러스가 8부작 스포츠 다큐멘터리 <아워게임: LG트윈스>를 CJ·KT 연합 온라인동영상서비스(OTT) 티빙을 통해 공개한다. 공들여 만든 오리지널 콘텐츠를 자사 채널이 아닌 외부 플랫폼에 내놓는 이유가 뭘까. 최근 지상파 방송도 자체 제작 콘텐츠를 OTT에 먼저 출시하고 있다."
context2 = "2014년 8월 20일 방탄소년단은 첫 번째 정규 앨범 《DARK&WILD》를 발매했고 현재까지(2017년 기준) 16만 장 넘게 팔렸다., 10월 17일부터 19일까지 총 3일간 예스24라이브홀(구 악스 홀)에서 데뷔 1년 4개월여만에 첫 단독 콘서트 ‘BTS 2014 LIVE TRILOGY : EPISODE Ⅱ. THE RED BULLET'을 개최해 성공리에 마무리 지었다. 당초 2회 공연 예정이었던 첫 단독 콘서트는 1회를 추가해 사흘간 진행 되었다. 방탄소년단은 서울 공연을 시작으로 일본, 필리핀, 싱가포르, 태국 등으로 아시아 투어를 진행, 글로벌 팬들과의 만남을 가졌다. 방탄소년단은 이후 10월 말부터 정규 앨범 《DARK&WILD》의 수록곡인 '호르몬 전쟁'으로 후속곡 활동을 했다."

encoded_context = tokenizer.encode(context2)
inputs = torch.tensor([encoded_context.ids])
attention_mask = torch.tensor([[1] * len(inputs[0])])
eos_token_id = tokenizer.token_to_id("</s>")
# inputs = tokenizer.encode(context, return_tensors='pt')
max_length = len(inputs[0]) + 200  # 본문 길이에 여유분을 더합니다.
outputs = model.generate(inputs, attention_mask=attention_mask, pad_token_id=eos_token_id, max_length=max_length, num_return_sequences=1, num_beams=1)
# for output in outputs:
#     print(tokenizer.decode(output.tolist(), skip_special_tokens=True))
output_str  = tokenizer.decode(outputs[-1].tolist(), skip_special_tokens=True)
print(output_str)
# "정답:"과 "질문:" 사이에 있는 문자열을 추출합니다.
answer = output_str.split("정답:")[1].split("질문:")[0].strip()

# "질문:"과 "</s>" 사이에 있는 문자열을 추출합니다.
question = output_str.split("질문:")[1].split("</s>")[0].strip()

print("정답:", answer)
print("질문:", question)