import React, { useState } from "react";
import { Button, Radio } from "antd";
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

  const postj3 = async () => {
    try {
      const response = await answerJ3("김동현", id, answer);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleRadioChange = (question: string, value: string) => {
    setAnswer(new Map(answer.set(question, value)));
  };

  return (
    <div className="mt-32 text-xl leading-loose mr-10">
      {Object.entries(data.result).map(([key, value]) => {
        const quizValue = value as QuizValue;
        return (
          <div key={key} className="mb-5">
            <p className="text-3xl leading-loose">
              <span className="font-extrabold ">{key}번 </span>
              <span className="font-bold">{quizValue.quiz_question}</span>
            </p>
            <Radio.Group
              onChange={(e) =>
                handleRadioChange(quizValue.quiz_question, e.target.value)
              }
            >
              {Object.entries(quizValue.example).map(([key, value]) => (
                <Radio value={key} key={key} className="font-default text-2xl">
                  &nbsp;&nbsp;{`${value}`}
                </Radio>
              ))}
            </Radio.Group>
            <br />
            <br />
          </div>
        );
      })}
      <Button
        className="right-16 font-bold text-xl fixed w-44 h-14  bg-secondary hover:border-none hover:text-3xl hover:text-black"
        type="primary"
        onClick={postj3}
      >
        제출
      </Button>
    </div>
  );
}

export default J3;
