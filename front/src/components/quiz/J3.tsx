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
    <div>
      <div>
        <p>MMSE-KC</p>
        {Object.entries(data.result).map(([key, value]) => {
          const quizValue = value as QuizValue;
          return (
            <div key={key}>
              <p>{`${key}번 ${quizValue.quiz_question}`}</p>
              <Radio.Group
                onChange={(e) =>
                  handleRadioChange(quizValue.quiz_question, e.target.value)
                }
              >
                {Object.entries(quizValue.example).map(([key, value]) => (
                  <Radio value={key} key={key}>
                    &nbsp;&nbsp;{`${key} : ${value}`}
                  </Radio>
                ))}
              </Radio.Group>
            </div>
          );
        })}
        <Button onClick={postj3}>제출</Button>
      </div>
    </div>
  );
}

export default J3;
