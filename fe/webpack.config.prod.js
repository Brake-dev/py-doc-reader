import { merge } from "webpack-merge";
import baseConfig from "./webpack.config.js";

export default merge(baseConfig, {
  optimization: {
    minimize: true,
  },
  mode: "production",
  stats: {
    children: false,
    errorDetails: true,
  },
  module: {
    rules: [
      {
        test: /\.(ts|js)x?$/,
        exclude: /node_modules/,
        loader: "ts-loader",
      },
    ],
  },
});
