import React from "react";
import { Button } from "antd";
import CanvasDraw from "react-canvas-draw";
import art from "../../assets/art.png";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}

function J5({ current, setCurrent }: QuizStepProps) {
  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100">
      <p className="text-5xl mb-10 mt-10 font-bold">구성 행동 검사</p>
      <div className="text-2xl mb-5">
        <p>문제: 보여드리는 그림을 순서대로 그려주세요.</p>
      </div>
      <img src={art} alt="핸드" className="w-1/3 mb-5" />
      <CanvasDraw
        className="border mb-5 w-9/12 h-32 text-2xl"
        brushColor="black"
        brushRadius={2}
      />
    </div>
  );
}

export default J5;
