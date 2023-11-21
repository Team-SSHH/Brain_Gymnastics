import React from "react";
import { Button } from "antd";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}

function J1({ current, setCurrent }: QuizStepProps) {
  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100 mr-10">
      <p className="text-5xl mb-10 mt-10 font-bold">언어 유착성 검사</p>
      <div className="text-3xl mb-5 leading-loose ">
        지금부터 '동물'에 속하는 것들의 이름을 모두 말씀해보십시오.
        <br />
        1분의 시간을 드리겠습니다.
        <br />
        1분 동안 생각 나는 동물의 이름을 모두 적어주세요.
      </div>
      <textarea
        className="border mb-5 p-3 w-9/12 h-32 text-2xl"
        placeholder="동물의 이름을 입력하세요."
      />
    </div>
  );
}

export default J1;
