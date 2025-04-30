import React, { FC } from "react";
import { useNavigate } from "react-router";

const TestView2: FC = () => {
  const navigate = useNavigate();

  return (
    <div>
      <div>TestView2</div>
      <button type="button" onClick={() => navigate("/")}>
        Got to TestView1
      </button>
    </div>
  );
};

export default TestView2;
