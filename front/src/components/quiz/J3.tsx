import React, { useState } from "react";
import { Button } from "antd";
import { answerJ3 } from "../../utiles/news";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
  data: any;
  id: string;
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
        {data.result.map((que: any) => (
          <div>
            <p>{que.quiz_question}</p>
            {Object.entries(que.example).map(([key, value]) => (
              <span key={key}>{`${key} : ${value}`}</span>
            ))}
          </div>
        ))}
        {/* <Button onClick={onClick}></Button> */}
      </div>
    </div>
  );
}

export default J3;
