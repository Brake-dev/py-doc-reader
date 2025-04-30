import React, { useEffect, FC } from "react";
import { useLocation } from "react-router";

const ScrollToTop: FC<{ children?: React.ReactNode }> = ({ children }) => {
  const location = useLocation();

  useEffect(() => {
    if (!location.search.includes("?noScroll")) {
      window.scrollTo(0, 0);
    }
  }, [location]);
  return <>{children}</>;
};

export default ScrollToTop;
