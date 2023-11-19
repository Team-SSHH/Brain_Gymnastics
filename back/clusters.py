from sklearn.cluster import KMeans
import numpy as np

# 배열 목록 준비
keywords = [
    '사과', '자전거', '구름', '별', '해변',
    '커피', '책상', '휴대폰', '의자', '호랑이',
    '비행기', '바다', '햇빛', '키보드', '강아지',
    '고양이', '꽃', '나무', '새', '하늘',
    '도시', '눈', '풍경', '모니터', '소파',
    '축구', '테니스', '배구', '골프', '야구',
    '수영', '쇼핑', '음식', '음악', '영화',
    '여행', '운동', '잠', '화장품', '운전',
    '산책', '공부', '친구', '가족', '사랑',
    '행복', '돈', '시간', '건강', '꿈','꿈','축구','축구','축구','축구','축구','축구','축구','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스','테니스',
]

keywords1 = [
    '인공지능', '빅데이터', '클라우드 컴퓨팅', '블록체인', '사물인터넷',
    '머신러닝', '딥러닝', '가상현실', '증강현실', '자율주행',
    '사회네트워크', '사이버 보안', '가상화폐', '스마트 시티', '생체인식',
    '인터넷 of Things', '클러스터링', '자연어 처리', '영상 인식', '강화학습',
    '데이터 마이닝', '오픈소스', '로보틱스', '인공신경망', '감정 분석',
    '가짜 뉴스', '클라우드 서비스', '데이터 시각화', '블로그 분석', '금융 기술',
    '음성 인식', '얼굴 인식', '자율 로봇', '데이터 보안', '인공지능 비서',
    '기계 번역', '자율 주행 자동차', '의료 데이터', '스마트 홈', '스마트 팩토리',
    '가상현실 게임', '데이터 분석', '온라인 광고', '영화 추천', '자동 음성 번역',
    '인공지능 예측', '데이터 암호화', '신경망 모델', '지능형 로봇', '클라우드 보안'
]

# 벡터화를 위한 배열 목록을 숫자로 변환
keyword_vectors = np.array(range(len(keywords))).reshape(-1, 1)

# K-means 클러스터링 수행
kmeans = KMeans(n_clusters=3)  # 3개의 클러스터로 분류
kmeans.fit(keyword_vectors)

# 클러스터링 결과 확인
labels = kmeans.labels_
clusters = {}
for i, label in enumerate(labels):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(keywords[i])

# 클러스터링 결과 출력
for cluster_id, keywords in clusters.items():
    print(f"Cluster {cluster_id + 1}:")
    print(keywords)
    print()

# 대표 키워드 선택
representative_keywords = []
for cluster_id, keywords in clusters.items():
    cluster_center = kmeans.cluster_centers_[cluster_id][0]
    closest_keyword_idx = np.argmin(np.abs(keyword_vectors - cluster_center))
    if closest_keyword_idx >= len(keywords):
        closest_keyword_idx = len(keywords) - 1
    representative_keyword = keywords[closest_keyword_idx]
    representative_keywords.append(representative_keyword)

# 대표 키워드 출력
for i, keyword in enumerate(representative_keywords):
    print(f"Cluster {i + 1} 대표 키워드:")
    print(keyword)
    print()
