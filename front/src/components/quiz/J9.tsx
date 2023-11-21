import React from "react";
import { Button } from "antd";
import path from "../../assets/path.jpg";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}

function J9({ current, setCurrent }: QuizStepProps) {
  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100 mr-10">
      <p className="text-5xl mb-10 mt-10 font-bold">길 만들기 검사</p>
      <div className="text-3xl mb-5 leading-loose ">
        이 종이에 몇 개의 숫자와 글자가 잇습니다.
        <br />
        숫자 1에서 시작하여, 1에서 "가"로 선을 긋고,
        <br />
        "가"에서 2로, 2에서 "나"로, "나"에서 3으로 3에서 "다"로,
        <br />
        이와 같은 식으로 순서대로 끝에 도달할 때까지 선을 그어 보십시오.
      </div>
      <img src={path} alt="길만들기" className="w-3/5" />
    </div>
  );
}

export default J9;
