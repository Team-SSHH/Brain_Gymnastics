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
    <div className="flex flex-col items-center justify-center bg-gray-100 mr-10 mt-10">
      {/* <p className="text-5xl mb-10 mt-10 font-bold">길 만들기 검사</p> */}
      <div className="text-3xl mb-5 leading-loose ">
        <p>
          이 종이에 몇 개의 숫자와 글자가 있습니다.
          <br />
          1에서 시작하여, "가"로 선을 긋고, "가"에서 2로,
          <br />
          2에서 "나"로, "나"에서 3 순서대로 끝에 도달할 때까지 선을 그어
          보십시오.
          <br />
          준비되었습니까? 시작하세요.
        </p>
      </div>
      <img src={path} alt="길만들기" className="w-3/5" />
    </div>
  );
}

export default J9;
