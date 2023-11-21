import React from "react";
import { IoCaretBackOutline } from "react-icons/io5";
import { useNavigate } from "react-router-dom";

const BackBtn = () => {
  const navigate = useNavigate();
  const goBack = () => {
    navigate(-1);
  };

  return (
    <IoCaretBackOutline
      onClick={() => goBack()}
      size="60"
      color="#C8CEAA"
      className="cursor-pointer"
    />
  );
};

export default BackBtn;
