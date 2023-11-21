import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect } from "react";
import axios from "axios";
import "./App.css";
import logo from "./assets/logo.png";
import MainPage from "./pages/MainPage";
import ProfilePage from "./pages/ProfilePage";
import QuizPage from "./pages/QuizPage";
import ReadNewsPage from "./pages/ReadNewsPage";
import ReadNewspaper from "./pages/ReadNewspaper";
import ListenNewsPage from "./pages/ListenNewsPage";
import ListenNewspaper from "./pages/ListenNewspaper";

function App() {
  return (
    <BrowserRouter>
      <div className="bg-primary tracking-wider h-screen font-default pt-5">
        {/* <header className="App-header">
          <img src={logo} alt="두뇌체조로고" className="w-32 no-drag" />
        </header> */}
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/quiz" element={<QuizPage />} />
          <Route path="/readNews" element={<ReadNewsPage />} />
          <Route path="/ReadNewspaper/:id" element={<ReadNewspaper />} />
          <Route path="/listenNews" element={<ListenNewsPage />} />
          <Route path="/ListenNewspaper/:id" element={<ListenNewspaper />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
