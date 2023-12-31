import { api } from "./api";
// 카테고리 지정 뉴스 보기
export const getCategoryNews = (category: Array<string>, page: number) =>
  api.post(`/news/category`, { category, page });

export const saveCategory = async (
  news_id: string,
  category: Array<string>,
  user_id: string
) => {
  const response = await api.post(`/category/save`, {
    news_id,
    category,
    user_id,
  });
  return response;
};

export const detail = (news_id: string) => api.post(`/detail`, { news_id });

export const recommendNews = (user_id: string) =>
  api.post(`/recommend/my`, { user_id });

export const myQuiz = (user_id: string) =>
  api.post(`/user/myQuiz`, { user_id });

export const retryQuiz = (quiz_id: string, answer: Array<string>) =>
  api.post(`/quiz/retry/answer`, { quiz_id, answer });

export const startQuiz = (user_id: string) =>
  api.post(`/quiz/start`, { user_id });

export const answerJ3 = (
  user_id: string,
  quiz_id: string,
  answer: Map<string, string>
) => api.post(`/choice/answer/j3`, { user_id, quiz_id, answer });

export const startJ4 = (user_id: string) =>
  api.post(`/quiz/start/j4`, { user_id });

export const answerJ4 = (
  user_id: string,
  quiz_id: string,
  answer: Array<string>
) => api.post(`/list/answer`, { user_id, quiz_id, answer });

export const startJ6 = (user_id: string) =>
  api.post(`/quiz/start/j6`, { user_id });

export const answerJ6 = (
  user_id: string,
  quiz_id: string,
  answer: Array<string>
) => api.post(`/quiz/answer/j6`, { user_id, quiz_id, answer });

export const startJ7 = (user_id: string) =>
  api.post(`/quiz/start/j7`, { user_id });

export const answerJ7 = (
  user_id: string,
  quiz_id: string,
  answer_o: Array<string>,
  answer_x: Array<string>
) => api.post(`/quiz/answer/j7`, { user_id, quiz_id, answer_o, answer_x });

// 내 점수 보기
export const myScore = (user_id: string) =>
  api.post(`/quiz/myscore`, { user_id });
