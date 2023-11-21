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
    <div className="flex flex-col items-center justify-center bg-gray-100">
      <p className="text-5xl mb-10 mt-10 font-bold">길 만들기 검사</p>
      <div className="text-2xl mb-5">
        <p>
          문제: 이 종이에 몇 개의 숫자와 글자가 잇습니다. 숫자 1에서 시작하여,
          1에 서 „가‟로 선을 긋고, ‘가‟에서 2로, 2에서 „나‟로, ‘나‟에서 3으로
          3에서 „다‟로, 이와 같은 식으로 순서대로 끝에 도달할 때까지 선을 그어
          보십시오. --- 준비되었습니 까? 시작하세요.
        </p>
      </div>
      <img src={path} alt="길만들기" className="w-2/5 mb-5" />
      <textarea
        className="border mb-5 p-3 w-9/12 h-32 text-2xl"
        placeholder="동물의 이름을 입력하세요."
      />
    </div>
  );
}

export default J9;
