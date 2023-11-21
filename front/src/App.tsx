import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect } from "react";
import axios from "axios";
import "./App.css";
import logo from "./assets/logo.png";
import MainPage from "./pages/MainPage";
import ProfilePage from "./pages/ProfilePage";
import QuizPage from "./pages/QuizPage";

function App() {
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
