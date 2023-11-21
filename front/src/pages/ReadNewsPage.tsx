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

      <div className="grid grid-cols-3 gap-20 mx-20 pt-28 justify-items-center">
        <CategoryBtn name="맞춤" category="read" />
        <CategoryBtn name="정치" category="read" />
        <CategoryBtn name="경제" category="read" />
        <CategoryBtn name="사회" category="read" />
        <CategoryBtn name="문화" category="read" />
        <CategoryBtn name="국제" category="read" />
        <CategoryBtn name="지역" category="read" />
        <CategoryBtn name="스포츠" category="read" />
        <CategoryBtn name="IT_과학" category="read" />
      </div>
    </div>
  );
};

export default ReadNewsPage;
