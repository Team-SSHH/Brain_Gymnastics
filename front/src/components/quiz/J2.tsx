import React, { useEffect, useState } from "react";
import { Button } from "antd";
import hand from "../../assets/hand.png";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}

function J2({ current, setCurrent }: QuizStepProps) {
  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100">
      <p className="absolute text-5xl top-20 font-bold">보스톤 이름대기 검사</p>

      <div className="text-3xl mb-5 leading-loose ">
        지금부터 제가 몇 개의 그림을 보여 드리겠습니다.
        <br />각 그림의 이름을 적어주십시오.
        <br />
        “이 사물의 이름은 무엇입니까?”
      </div>
      <img src={hand} alt="핸드" className="w-1/6 mb-5" />
      <textarea
        className="border mb-5 p-3 w-9/12 h-32 text-2xl"
        placeholder="사물의 이름을 입력하세요."
      />
    </div>
  );
}

export default J2;
