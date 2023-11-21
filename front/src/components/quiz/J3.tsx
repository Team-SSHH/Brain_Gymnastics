import React, { useState } from "react";
import { Button } from "antd";
import { answerJ3 } from "../../utiles/news";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
  data: any;
  id: string;
}
interface QuizValue {
  quiz_question: string;
  example: { [key: string]: string };
}

function J3({ current, setCurrent, data, id }: QuizStepProps) {
  const [answer, setAnswer] = useState(new Map<string, string>());

  const onClick = () => {
    setCurrent(current + 1);
  };

  const postj4 = async () => {
    try {
      const response = await answerJ3("김동현", id, answer);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <div>
        <p>MMSE-KC</p>
        {Object.entries(data.result).map(([key, value]) => {
          const quizValue = value as QuizValue;
          return (
            <div key={key}>
              <span>{`${key}번 ${quizValue.quiz_question}`}</span>
              {Object.entries(quizValue.example).map(([key, value]) => (
                <div key={key}>
                  &nbsp;&nbsp;&nbsp;&nbsp;{`${key} : ${value}`}
                </div>
              ))}
            </div>
          );
        })}
        {/* <Button onClick={onClick}></Button> */}
      </div>
    </div>
  );
}

export default J3;
