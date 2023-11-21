import { api } from "./api";
// 카테고리 지정 뉴스 보기
export const getCategoryNews = (category: Array<string>, page: number) =>
  api.post(`/news/category`, { category, page });

// 키워드, 카테고리 저장/ 퀴즈 생성
export const saveCategory = (name_id: string, category: Array<string>) =>
  api.post(`/category/save`, { name_id, category });

// 뉴스 상세
export const detail = (news_id: string) => api.post(`/detail`, { news_id });

// 추천 뉴스 보기
export const recommendNews = (news_id: string, category: string) =>
  api.post(`/recommend/my`, { news_id, category });

// 내 전체 퀴즈 보기
export const myQuiz = (user_id: string) =>
  api.post(`/user/myQuiz`, { user_id });

// 퀴즈 다시 풀기
export const retryQuiz = (quiz_id: string, answer: Array<string>) =>
  api.post(`/quiz/retry/answer`, { quiz_id, answer });

// 퀴즈 시작 j3
export const startQuiz = (user_id: string, date: string) =>
  api.post(`/quiz/start`, { user_id, date });

// j3 정답 제출
export const answerJ3 = (
  user_id: string,
  quiz_id: string,
  answer: Map<string, string>
) => api.post(`/choice/answer/j3`, { user_id, quiz_id, answer });

// j4 불러오기
export const startJ4 = (user_id: string, date: string) =>
  api.post(`/quiz/start/j4`, { user_id, date });

// j4 제출
export const answerJ4 = (
  user_id: string,
  quiz_id: string,
  answer: Array<string>
) => api.post(`/list/answer`, { user_id, quiz_id, answer });

// j6 불러오기
export const startJ6 = (user_id: string, date: string) =>
  api.post(`/quiz/start/j6`, { user_id, date });

// 퀴즈 6 정답 제출
export const answerJ6 = (
  user_id: string,
  quiz_id: string,
  answer: Array<string>
) => api.post(`/quiz/answer/j6`, { user_id, quiz_id, answer });

// 퀴즈 j7 불러오기
export const startJ7 = (user_id: string, date: string) =>
  api.post(`/quiz/start/j7`, { user_id, date });

// 퀴즈 7 정답 제출
export const answerJ7 = (
  user_id: string,
  quiz_id: string,
  answer_o: Array<string>,
  answer_x: Array<string>
) => api.post(`/quiz/answer/j7`, { user_id, quiz_id, answer_o, answer_x });

// 내 점수 보기
export const myScore = (user_id: string) =>
  api.post(`/quiz/myscore`, { user_id });
