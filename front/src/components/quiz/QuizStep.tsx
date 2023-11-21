import React, { useState, useEffect } from "react";
import { Steps } from "antd";
import "./QuizStep.css";
import { startQuiz } from "../../utiles/news";

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
  const getj4 = async () => {
    try {
      const response = await startQuiz("김동현");
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    getj4();
  }, []);
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
