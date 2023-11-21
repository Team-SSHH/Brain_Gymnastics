import React, { useEffect, useState } from "react";
import { Button } from "antd";
import { startJ6 } from "../../utiles/news";
import { answerJ6 } from "../../utiles/news";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}
interface j6 {
  example: [];
}
function J6({ current, setCurrent }: QuizStepProps) {
  const [j6, setJ6] = useState<j6>();
  const [currentExIndex, setCurrentExIndex] = useState<number>(0);
  const [index, setIndex] = useState(0);
  const [id, setId] = useState("");
  const [answer, setAnswer] = useState<string[]>([]);
  const [inputValue, setInputValue] = useState("");

  useEffect(() => {
    if (j6 && currentExIndex < j6.example.length) {
      const timer = setTimeout(() => {
        setCurrentExIndex((prevIndex) => prevIndex + 1);
      }, 2000);
      return () => clearTimeout(timer);
    } else {
      setIndex(1);
      console.log(index);
    }
  }, [currentExIndex, j6]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  const handleEnterPress = (event: React.KeyboardEvent) => {
    if (event.key === "Enter") {
      event.preventDefault(); // form의 자동 제출을 막습니다.
      setAnswer((prev) => [...prev, inputValue]);
      setInputValue("");
    }
  };

  const getj6 = async () => {
    try {
      const response = await startJ6("김동현");
      console.log(response);
      setJ6(response.data);
      setId(response.data._id);
    } catch (error) {
      console.error(error);
    }
  };

  const postj6 = async () => {
    try {
      const response = await answerJ6("김동현", id, answer);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    getj6();
  }, []);

  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div>
      <div>
        <p>단어목록회상 검사</p>
        <div>{j6 && j6.example[currentExIndex]}</div>
        {currentExIndex === 10 &&
          (answer.length < 10 ? (
            <div>
              <p>기억나는 단어를 모두 적어주세요</p>
              <input
                type="text"
                placeholder="단어를 적고 엔터를 쳐주세요"
                value={inputValue}
                onChange={handleInputChange}
                onKeyDown={handleEnterPress}
              />
            </div>
          ) : (
            <Button onClick={postj6}>정답 제출</Button>
          ))}
        {/* <Button onClick={onClick}></Button> */}
      </div>
    </div>
  );
}

export default J6;
