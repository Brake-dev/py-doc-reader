import React, { FC } from "react";
import { useNavigate } from "react-router";

import * as styles from "./TestView.module.less";

const TestView1: FC = () => {
  const navigate = useNavigate();

  return (
    <div className={styles.container}>
      <div>TestView1</div>
      <button type="button" onClick={() => navigate("/2")}>
        Got to TestView2
      </button>
    </div>
  );
};

export default TestView1;
