import React, { useState } from "react";
import { Modal } from "antd";
import { getCategoryNews, recommendNews } from "../../utiles/news";
import { NewsType } from "../../types/index";
import { useNavigate } from "react-router-dom";
import { LuNewspaper } from "react-icons/lu";

interface Props {
  name: string;
  category: string;
}

const CategoryBtn: React.FC<Props> = ({ name, category }) => {
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const [news, setNews] = useState<NewsType[]>([]);
  const navigate = useNavigate();
  const showModal = () => {
    setIsModalOpen(true);
    getNews();
  };

  const getNews = async () => {
    let response;
    if (name === "맞춤") {
      response = await recommendNews("김동현");
    } else {
      response = await getCategoryNews([name], 1);
    }
    // const response = await getCategoryNews([name], 1);
    console.log(response.data.return_object.documents);
    setNews(response.data.return_object.documents);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  return (
    <>
      <div
        className="rounded-2xl font-bold w-60 bg-secondary h-28 flex justify-center items-center text-4xl hover:bg-red hover:text-white hover:cursor-pointer"
        onClick={showModal}
      >
        {name}
      </div>

      <Modal
        title={
          <div className="font-default text-2xl font-bold flex items-center">
            <LuNewspaper />
            <span className="ml-2">{name}</span>
          </div>
        }
        open={isModalOpen}
        width={1000}
        onCancel={handleCancel}
        cancelButtonProps={{ style: { display: "none" } }}
        okButtonProps={{ style: { display: "none" } }}
      >
        {news &&
          news.map((nowNews, index) => (
            <div
              key={nowNews.news_id}
              onClick={() =>
                navigate(
                  `/${category === "read" ? "read" : "listen"}Newspaper/${
                    nowNews.news_id
                  }`,
                  {
                    state: nowNews,
                  }
                )
              }
            >
              <p className="text-2xl font-bold mt-8">
                <span className="text-primary mr-2 text-3xls font-extrabold">
                  {index + 1}
                </span>
                <span className="hover:text-red cursor-pointer">
                  {nowNews.title}
                </span>
              </p>
            </div>
          ))}
      </Modal>
    </>
  );
};
export default CategoryBtn;
