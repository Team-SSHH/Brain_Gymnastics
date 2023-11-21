import React, { useEffect, useState } from "react";
import BackBtn from "../components/ui/backBtn";
import TitleBtn from "../components/ui/titleBtn";
import { saveCategory } from "../utiles/news";
import { useLocation } from "react-router";
import { NewsDetailType } from "../types";

const ReadNewspaper = () => {
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
  }, []);

  return (
    <div className="h-full overflow-y-hidden">
      <div className="flex items-center">
        <BackBtn />
        <TitleBtn name="뉴스 주제 선택" />
      </div>
      <div className="mt-10 flex items-center justify-center h-full ">
        <div className="bg-gray rounded-3xl w-4/5 h-full p-14">
          {data && (
            <>
              <div className="font-extrabold text-5xl text-center pt-10 leading-loose">
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

export default ReadNewspaper;
