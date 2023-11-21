import React from "react";
import { Button } from "antd";
import CanvasDraw from "react-canvas-draw";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}

function J8({ current, setCurrent }: QuizStepProps) {
  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100">
      <p className="absolute text-5xl top-20 font-bold">구성 회상 검사</p>
      <div className="text-2xl mb-5">
        <p>
          앞선 검사에서 그렸던 그림들이 기억 나시나요?
          <br />
          아까 그렸던 그림들을 다시 한번 그려주세요.
        </p>
      </div>

      <CanvasDraw
        className="border mb-5 w-9/12 h-32 text-2xl"
        brushColor="black"
        brushRadius={2}
      />
    </div>
  );
}

export default J8;
