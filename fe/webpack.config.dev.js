import webpack from "webpack";
import { merge } from "webpack-merge";
import baseConfig from "./webpack.config.js";
import ReactRefreshWebpackPlugin from "@pmmmwh/react-refresh-webpack-plugin";
import ReactRefreshTypeScript from "react-refresh-typescript";

const { HotModuleReplacementPlugin } = webpack;

export default merge(baseConfig, {
  mode: "development",
  devtool: "inline-source-map",
  entry: ["webpack-hot-middleware/client", "./src/index.tsx"],
  module: {
    rules: [
      {
        test: /\.(ts|js)x?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: "ts-loader",
            options: {
              getCustomTransformers: () => ({
                before: [ReactRefreshTypeScript()],
              }),
              transpileOnly: true,
            },
          },
        ],
      },
    ],
  },
  plugins: [new HotModuleReplacementPlugin(), new ReactRefreshWebpackPlugin()],
});
