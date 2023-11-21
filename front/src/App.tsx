import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect } from "react";
import axios from "axios";
import "./App.css";
import logo from "./assets/logo.png";

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
      <div className="App bg-primary">
        <header className="App-header">
          <img src={logo} alt="두뇌체조로고" className="w-32" />
        </header>
        {/* <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/board" element={<Board />} />
        </Routes> */}
        <div>여기여기</div>
      </div>
    </BrowserRouter>
  );
}

export default App;
