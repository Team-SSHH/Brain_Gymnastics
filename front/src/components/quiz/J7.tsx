import React, { useEffect, useState } from "react";
import { Button } from "antd";
import { startJ7 } from "../../utiles/news";
import { answerJ7 } from "../../utiles/news";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}
interface j7 {
  example: [];
}
function J7({ current, setCurrent }: QuizStepProps) {
  const [j7, setJ7] = useState<j7>();
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});
  const [correctAnswers, setCorrectAnswers] = useState<string[]>([]);
  const [incorrectAnswers, setIncorrectAnswers] = useState<string[]>([]);
  const [id, setId] = useState("");

  const getj7 = async () => {
    try {
      const response = await startJ7("김동현");
      console.log(response);
      setJ7(response.data);
      setIncorrectAnswers(response.data.example);
      setId(response.data._id);
    } catch (error) {
      console.error(error);
    }
  };

  const postJ7 = async () => {
    try {
      const response = await answerJ7(
        "김동현",
        id,
        correctAnswers,
        incorrectAnswers
      );
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    getj7();
  }, []);

  const onClick = () => {
    setCurrent(current + 1);
  };

  const handleCheckboxChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = event.target;
    setCheckedItems((prev) => ({ ...prev, [name]: checked }));

    if (checked) {
      setCorrectAnswers((prev) => [...prev, name]);
      setIncorrectAnswers((prev) => prev.filter((item) => item !== name));
    } else {
      setIncorrectAnswers((prev) => [...prev, name]);
      setCorrectAnswers((prev) => prev.filter((item) => item !== name));
    }
  };
  useEffect(() => {
    console.log(correctAnswers);
    console.log(incorrectAnswers);
  }, [correctAnswers, incorrectAnswers]);

  return (
    <div>
      <div>
        <p>단어목록재인 검사</p>
        {j7 &&
          j7.example.map((ex: string, index: number) => {
            return (
              <div>
                <div
                  key={index}
                  style={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                  }}
                >
                  <p>{ex}</p>
                  <input
                    type="checkbox"
                    name={ex}
                    checked={checkedItems[ex] || false}
                    onChange={handleCheckboxChange}
                  />
                </div>
              </div>
            );
          })}
        {/* <Button onClick={onClick}></Button> */}
        <Button onClick={postJ7}>정답 제출</Button>
      </div>
    </div>
  );
}

export default J7;
