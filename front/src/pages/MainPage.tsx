import React from "react";
import { Link } from "react-router-dom";
import main1 from "../assets/main1.png";
import main2 from "../assets/main2.png";
import main3 from "../assets/main3.png";
import main4 from "../assets/main4.png";

function MainPage() {
  return (
    <div className="h-full flex flex-col items-center justify-center tracking-wider">
      <p className="font-extrabold text-center text-6xl mb-4">
        김동현님 반갑습니다.
      </p>
      <Link
        to="/profile"
        className="absolute top-10 right-10 w-1/5 flex flex-col items-center justify-center hover:scale-110"
      >
        <img src={main4} alt="내 정보" className="w-1/5 no-drag" />
        <p className="text-2xl font-bold text-center pt-8">내 정보 확인하기</p>
      </Link>
      <div className="bg-secondary flex items-center justify-center w-10/12 rounded-3xl p-5 h-2/3">
        <Link
          to="/readNews"
          className="w-1/3 flex flex-col items-center justify-between h-2/3  hover:scale-110"
        >
          <img src={main1} alt="뉴스 듣기" className="w-3/5 no-drag" />
          <p className="text-4xl font-bold text-center pt-8">
            오늘의 뉴스 듣기
          </p>
        </Link>

        <Link
          to="/readNews"
          className="w-1/3 flex flex-col items-center justify-between h-2/3 hover:scale-110"
        >
          <img src={main2} alt="뉴스 보기" className="w-3/5 no-drag" />
          <p className="text-4xl font-bold text-center pt-8">
            오늘의 뉴스 보기
          </p>
        </Link>

        <Link
          to="/quiz"
          className="w-1/3 flex flex-col items-center justify-between h-2/3 hover:scale-110"
        >
          <img src={main3} alt="문제 풀기" className="w-3/5 no-drag pt-20" />
          <p className="text-4xl font-bold text-center pt-8">
            오늘의 문제 풀기
          </p>
        </Link>
      </div>
    </div>
  );
}

export default MainPage;
