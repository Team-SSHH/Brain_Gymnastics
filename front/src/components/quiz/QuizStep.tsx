import React, { useState } from "react";
import { Steps } from "antd";
import "./QuizStep.css";

interface QuizStepProps {
  current: number;
}

const description = "This is a description.";
const items = [
  {
    title: "J1",
    description,
  },
  {
    title: "J2",
    description,
  },
  {
    title: "J3",
    description,
  },
  {
    title: "J4",
    description,
  },
  {
    title: "J5",
    description,
  },
  {
    title: "J6",
    description,
  },
  {
    title: "J7",
    description,
  },
  {
    title: "J8",
    description,
  },
  {
    title: "J9",
    description,
  },
];
function QuizStep({ current }: QuizStepProps) {
  return (
    <div>
      <Steps
        current={current}
        percent={(100 / 9) * (current + 1)}
        labelPlacement="vertical"
        items={items}
      />
    </div>
  );
}

export default QuizStep;
