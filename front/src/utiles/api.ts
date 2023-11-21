import axios from "axios";

// Axios 인스턴스 생성
export const api = axios.create({
  baseURL: "http://54.180.172.43:5000", // API의 기본 URL
  // withCredentials: true,
});
