import React, { useState, useEffect } from "react";
import { Button } from "antd";
import { startJ4 } from "../../utiles/news";

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

  const getj4 = async () => {
    try {
      const response = await startJ4("김동현");
      console.log(response);
      setJ4(response.data);
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
    <div>
      <div>
        <p>단어목록기억 검사</p>
        <div>{j4 && j4.example[currentExIndex]}</div>
        {currentExIndex === 10 && (
          <div>
            <p>기억나는 단어를 모두 적어주세요</p>
            <input type="text" placeholder="단어를 적고 엔터를 쳐주세요" />
          </div>
        )}
        {/* <Button onClick={onClick}></Button> */}
      </div>
    </div>
  );
}

export default J4;
