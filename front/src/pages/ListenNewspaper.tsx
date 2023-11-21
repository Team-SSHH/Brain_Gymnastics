import React, { useEffect, useState } from "react";
import BackBtn from "../components/ui/backBtn";
import TitleBtn from "../components/ui/titleBtn";
import { saveCategory } from "../utiles/news";
import { useLocation } from "react-router";
import { NewsDetailType } from "../types";
import ear from "../assets/ear.png";

const ListenNewspaper = () => {
  const { state } = useLocation();
  const [data, setData] = useState<NewsDetailType>();

  useEffect(() => {
    const getNews = async () => {
      const response = await saveCategory(
        state.news_id,
        state.category,
        "김동현"
      );
      setData(response.data.return_object.documents[0]);
      console.log(response.data.return_object.documents[0]);
      console.log(data);
    };
    getNews();

    return () => {
      window.speechSynthesis.cancel();
    };
  }, [state]);

  const speak = (title: string, content: string) => {
    const speech = new SpeechSynthesisUtterance(
      `제목: ${title}. 본문: ${content}`
    );
    window.speechSynthesis.speak(speech);
  };

  return (
    <div className="h-full overflow-y-hidden">
      <div className="flex items-center">
        <BackBtn />
        <TitleBtn name="뉴스 주제 선택" />
      </div>
      <div className="mt-10 flex items-center justify-center h-full ">
        <div className="bg-gray rounded-3xl w-4/5 h-full p-14 relative">
          {data && (
            <>
              <img
                src={ear}
                alt="귀"
                className="w-24 h-24 absolute top-5 right-5 cursor-pointer"
                onClick={() => speak(data.title, data.content)}
              />
              <div className="font-extrabold text-5xl text-center pt-10">
                {data.title}
              </div>
              <br />
              <div className="text-4xl font-bold mt-10 leading-loose">
                {data.content}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ListenNewspaper;
