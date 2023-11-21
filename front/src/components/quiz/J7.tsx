import React, { useEffect, useState } from "react";
import { Button, Radio } from "antd";
import { startJ7 } from "../../utiles/news";
import { answerJ7 } from "../../utiles/news";
import { RadioChangeEvent } from "antd/lib/radio";

interface QuizStepProps {
  current: number;
  setCurrent: React.Dispatch<React.SetStateAction<number>>;
}
interface j7 {
  example: [];
}
function J7({ current, setCurrent }: QuizStepProps) {
  const [j7, setJ7] = useState<j7>();
  const [selectedItems, setSelectedItems] = useState<Record<string, string>>(
    {}
  );
  const [correctAnswers, setCorrectAnswers] = useState<string[]>([]);
  const [incorrectAnswers, setIncorrectAnswers] = useState<string[]>([]);
  const [id, setId] = useState("");

  const getj7 = async () => {
    try {
      const response = await startJ7("김동현");
      console.log(response);
      setJ7(response.data);
      // setIncorrectAnswers(response.data.example);
      setId(response.data._id);
    } catch (error) {
      console.error(error);
    }
  };

  const postJ7 = async () => {
    if (correctAnswers.length + incorrectAnswers.length === 20) {
      return;
    }
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

  const handleRadioChange = (ex: string, event: RadioChangeEvent) => {
    const value = event.target.value;

    setSelectedItems((prev) => ({ ...prev, [ex]: value }));

    if (value === "예") {
      setCorrectAnswers((prev) => [...prev, ex]);
      setIncorrectAnswers((prev) => prev.filter((item) => item !== ex));
    } else {
      setIncorrectAnswers((prev) => [...prev, ex]);
      setCorrectAnswers((prev) => prev.filter((item) => item !== ex));
    }
  };

  useEffect(() => {
    console.log(correctAnswers);
    console.log(incorrectAnswers);
  }, [correctAnswers, incorrectAnswers]);

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexWrap: "wrap",
        }}
      >
        <div style={{ width: "70%", height: "60%" }}>
          <p>단어목록재인 검사</p>
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              justifyContent: "space-between",
            }}
          >
            {j7 &&
              j7.example.map((ex: string, index: number) => {
                return (
                  <div key={index} style={{ width: "23%", marginBottom: 20 }}>
                    <div
                      style={{
                        backgroundColor: "white",
                        borderRadius: "15px",
                        display: "flex",
                        flexDirection: "row",
                        justifyContent: "space-between",
                        alignItems: "center",
                        height: "80px",
                        padding: "10px",
                      }}
                    >
                      <span style={{ width: "50%", textAlign: "center" }}>
                        {ex}
                      </span>
                      <Radio.Group
                        style={{
                          width: "50%",
                          display: "flex",
                          flexDirection: "column",
                          justifyContent: "center",
                        }}
                        value={selectedItems[ex]}
                        onChange={(event) => handleRadioChange(ex, event)}
                      >
                        <Radio value="예">예</Radio>
                        <Radio value="아니오">아니오</Radio>
                      </Radio.Group>
                    </div>
                  </div>
                );
              })}
          </div>
          <Button onClick={postJ7}>정답 제출</Button>
        </div>
      </div>
    </div>
  );
}
export default J7;
