import React, { useState, useEffect } from "react";
import QuizStep from "../components/quiz/QuizStep";
import J1 from "../components/quiz/J1";
import J2 from "../components/quiz/J2";
import J3 from "../components/quiz/J3";
import J4 from "../components/quiz/J4";
import J5 from "../components/quiz/J5";
import J6 from "../components/quiz/J6";
import J7 from "../components/quiz/J7";
import J8 from "../components/quiz/J8";
import J9 from "../components/quiz/J9";
import { startQuiz } from "../utiles/news";
import { Button } from "antd";
import { position } from "stylis";

interface j3 {
  result: {};
}

function QuizPage() {
  const [current, setCurrent] = useState(0);
  const [j6, setJ6] = useState<j3>();
  const [id, setId] = useState("");

  const onClick = () => {
    setCurrent(current + 1);
  };
  const getj3 = async () => {
    try {
      const response = await startQuiz("김동현");
      console.log(response.data);
      setJ6(response.data);
      setId(response.data._id);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    // getj3();
  }, []);
  return (
    <div>
      <div>
        <QuizStep current={current} />
        {current === 0 && <J1 current={current} setCurrent={setCurrent} />}
        {current === 1 && <J2 current={current} setCurrent={setCurrent} />}
        {current === 2 && (
          <J3 current={current} setCurrent={setCurrent} data={j6} id={id} />
        )}
        {current === 3 && <J4 current={current} setCurrent={setCurrent} />}
        {current === 4 && <J5 current={current} setCurrent={setCurrent} />}
        {current === 5 && <J6 current={current} setCurrent={setCurrent} />}
        {current === 6 && <J7 current={current} setCurrent={setCurrent} />}
        {current === 7 && <J8 current={current} setCurrent={setCurrent} />}
        {current === 8 && <J9 current={current} setCurrent={setCurrent} />}
      </div>
      <Button
        onClick={onClick}
        style={{
          position: "fixed",
          width: "200px",
          height: "50px",
          right: "100px",
          bottom: "100px",
        }}
      ></Button>
    </div>
  );
}

export default QuizPage;
