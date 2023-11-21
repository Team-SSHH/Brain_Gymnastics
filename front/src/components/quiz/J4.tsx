import React, { useState, useEffect } from "react";
import { Button } from "antd";
import { startJ4 } from "../../utiles/news";
import { answerJ4 } from "../../utiles/news";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}
interface j4 {
  example: [];
}

function J4({ current, setCurrent }: QuizStepProps) {
  const [j4, setJ4] = useState<j4>();
  const [currentExIndex, setCurrentExIndex] = useState<number>(0);
  const [index, setIndex] = useState(0);
  const [id, setId] = useState("");
  const [answer, setAnswer] = useState<string[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [com, setCom] = useState(0);

  useEffect(() => {
    if (j4 && currentExIndex < j4.example.length) {
      const timer = setTimeout(() => {
        setCurrentExIndex((prevIndex) => prevIndex + 1);
      }, 2000);
      return () => clearTimeout(timer);
    } else {
      setIndex(1);
      console.log(index);
    }
  }, [currentExIndex, j4]);

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

  const getj4 = async () => {
    try {
      const response = await startJ4("김동현");
      console.log(response);
      setJ4(response.data);
      setId(response.data._id);
    } catch (error) {
      console.error(error);
    }
  };

  const postj4 = async () => {
    if (com) {
      return;
    }

    try {
      const response = await answerJ4("김동현", id, answer);
      console.log(response.data);
      if (response.data.status === 200) {
        setCom(1);
        return;
      }
      setJ4(response.data);
      setCurrentExIndex(0);
      setIndex(0);
      setAnswer([]);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    getj4();
  }, []);

  const onClick = () => {
    setCurrent(current + 1);
  };

  return (
    <div className="flex flex-col items-center justify-center bg-gray-100">
      <p className="text-5xl mb-10 mt-10 font-bold">단어목록기억 검사</p>
      <div className="text-2xl mb-5">
        <div className="text-5xl">{j4 && j4.example[currentExIndex]}</div>
        {currentExIndex === 10 &&
          (answer.length < 10 ? (
            <div className="w-full h-32">
              <p className="text-2xl mb-5">기억나는 단어를 모두 적어주세요</p>
              <input
                type="text"
                className="text-2xl border mb-5 w-full"
                placeholder="단어를 적고 엔터를 쳐주세요"
                value={inputValue}
                onChange={handleInputChange}
                onKeyDown={handleEnterPress}
              />
            </div>
          ) : (
            <Button
              className="right-16 font-bold text-xl fixed w-44 h-14  bg-secondary hover:border-none hover:text-3xl hover:text-black"
              type="primary"
              onClick={postj4}
            >
              {com === 0 ? "정답 제출" : "완료"}
            </Button>
          ))}
      </div>
    </div>
  );
}

export default J4;
