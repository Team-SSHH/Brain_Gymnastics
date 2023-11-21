import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect } from "react";
import axios from "axios";
import "./App.css";
import logo from "./assets/logo.png";
import MainPage from "./pages/MainPage";
import ProfilePage from "./pages/ProfilePage";
import QuizPage from "./pages/QuizPage";

function App() {
  useEffect(() => {
    // axios를 사용하여 백엔드 API 호출
    const fetchData = async () => {
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/recommend/my",
          {
            // 요청에 필요한 데이터를 여기에 추가
          }
        );
        const data = response.data;
        // API 응답 데이터 처리
        console.log(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  return (
    <BrowserRouter>
      <div className="bg-primary h-screen font-default">
        <header className="App-header">
          <img src={logo} alt="두뇌체조로고" className="w-32 no-drag" />
        </header>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/quiz" element={<QuizPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
