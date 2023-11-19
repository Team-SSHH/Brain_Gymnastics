from sklearn.feature_extraction.text import TfidfVectorizer

# 유저가 분석한 키워드 배열
user_keywords = [
    '사과', '자전거', '구름', '별', '해변',
    '커피', '책상', '휴대폰', '의자', '호랑이',
    '비행기', '바다', '햇빛', '키보드', '강아지',
    '고양이', '꽃', '나무', '새', '하늘',
    '도시', '눈의', '풍경', '모니터', '소파',
    '축구', '테니스의','테니스의','테니스의','테니스의','테니스의','테니스의','테니스의','테니스의', '배구', '골프', '야구',
    '수영', '쇼핑', '음식', '음악', '영화',
    '여행', '운동', '잠', '화장품', '운전',
    '산책', '공부', '친구', '가족', '사랑',
    '행복', '돈', '시간', '건강', '꿈','꿈','축구','축구','축구','축구','축구','축구','축구','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','클라우드 보안'
]

# 키워드 배열을 하나의 텍스트로 변환
user_keywords_text = ' '.join(user_keywords)

# TF-IDF 벡터화
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([user_keywords_text])

# 단어와 해당 단어의 TF-IDF 값을 추출
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray()[0]

# 상위 4~5개의 키워드 선택
top_n = 5
top_indices = tfidf_matrix.toarray()[0].argsort()[-top_n:][::-1]
recommended_keywords = [feature_names[i] for i in top_indices]

print(recommended_keywords)

for word, score in zip(feature_names, tfidf_scores):
    print(f"단어: {word}, TF-IDF Score: {score}")
