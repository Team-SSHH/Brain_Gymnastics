import React from "react";
import BackBtn from "../components/ui/backBtn";
import TitleBtn from "../components/ui/titleBtn";
import CategoryBtn from "../components/ui/categoryBtn";
const ReadNewsPage = () => {
  return (
    <div>
      <div className="flex items-center">
        <BackBtn />
        <TitleBtn name="뉴스 주제 선택" />
      </div>

      <div className="grid grid-cols-3 gap-24 mx-20 pt-28 justify-items-center">
        <CategoryBtn name="맞춤" />
        <CategoryBtn name="정치" />
        <CategoryBtn name="경제" />
        <CategoryBtn name="사회" />
        <CategoryBtn name="문화" />
        <CategoryBtn name="국제" />
        <CategoryBtn name="지역" />
        <CategoryBtn name="스포츠" />
        <CategoryBtn name="IT_과학" />
      </div>
    </div>
  );
};

export default ReadNewsPage;
