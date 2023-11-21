import React from "react";

interface Props {
  name: string;
}

const TitleBtn: React.FC<Props> = ({ name }) => {
  return (
    <div className="font-extrabold text-5xl underline-offset-4 underline decoration-8 decoration-secondary">
      {name}
    </div>
  );
};

export default TitleBtn;
