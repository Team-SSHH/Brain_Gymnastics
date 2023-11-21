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
    <div className="flex flex-col items-center justify-center">
      <p className="absolute text-5xl top-20 font-bold">구성 행동 검사</p>
      <p className="text-2xl mb-5  mt-32">
        보여드리는 그림을 순서대로 그려주세요.
      </p>
      <img src={art} alt="핸드" className="w-1/3 mb-5" />
      <CanvasDraw
        className="border w-9/12 h-32 text-2xl mt-7"
        brushColor="black"
        brushRadius={2}
      />
    </div>
  );
}

export default J5;
