import { api } from "./api";

export const getCategoryNews = (category: Array<string>, page: number) =>
  api.post(`/news/category`, { category, page });
