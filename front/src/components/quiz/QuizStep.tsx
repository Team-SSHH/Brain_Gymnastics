import React, { useState } from "react";
import { Steps } from "antd";
import "./QuizStep.css";
import BackBtn from "../ui/backBtn";
import TitleBtn from "../ui/titleBtn";

interface QuizStepProps {
  current: number;
}

const items = [
  {
    title: <div className="font-bold text-lg">J1</div>,
    description: <div className="font-bold text-2xl">언어유창성 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J2</div>,
    description: <div className="font-bold text-2xl">보스톤 이름대기 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J3</div>,
    description: <div className="font-bold text-2xl">MMSE-KC</div>,
  },
  {
    title: <div className="font-bold text-lg">J4</div>,
    description: <div className="font-bold text-2xl">단어목록기억 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J5</div>,
    description: <div className="font-bold text-2xl">구성행동 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J6</div>,
    description: <div className="font-bold text-2xl">단어목록회상 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J7</div>,
    description: <div className="font-bold text-2xl">단어목록재인 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J8</div>,
    description: <div className="font-bold text-2xl">구성회상 검사</div>,
  },
  {
    title: <div className="font-bold text-lg">J9</div>,
    description: <div className="font-bold text-2xl">길 만들기 검사 A, B</div>,
  },
];
function QuizStep({ current }: QuizStepProps) {
  return (
    <div>
      <div className="flex items-center">
        <BackBtn />
        <TitleBtn name="오늘의 문제" />
      </div>
      <div className="mt-10 ml-10 bg-white p-3 rounded-2xl w-10/12 flex">
        <Steps
          className="font-default"
          direction="vertical"
          current={current}
          percent={(100 / 9) * (current + 1)}
          labelPlacement="vertical"
          items={items}
        />
      </div>
    </div>
  );
}

export default QuizStep;
