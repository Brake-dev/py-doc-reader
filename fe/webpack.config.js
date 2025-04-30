import path from "path";
import { fileURLToPath } from "url";
import HtmlWebpackPlugin from "html-webpack-plugin";
import CompressionPlugin from "compression-webpack-plugin";

const { dirname } = path;
const __dirname = dirname(fileURLToPath(import.meta.url));

export default {
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx"],
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },
  output: {
    filename: "[name].[contenthash].js",
    path: path.resolve(__dirname, "dist"),
    clean: true,
    publicPath: "/",
  },
  optimization: {
    runtimeChunk: "single",
    splitChunks: {
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendors",
          chunks: "all",
        },
      },
    },
  },
  module: {
    rules: [
      {
        test: /\.svg$/,
        type: "asset/inline",
      },
      {
        test: /\.less$/i,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: { modules: { localIdentName: "[local]_[hash:base64:5]" } },
          },
          {
            loader: "less-loader",
            options: {
              lessOptions: {
                paths: [path.resolve(__dirname, "src")],
              },
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new CompressionPlugin({
      test: /\.(js?|jsx|ts|tsx|svg|gif|png|jpe?g|otf|eot|woff|woff2|ttf|ico)$/,
    }),
    new HtmlWebpackPlugin({
      template: "src/index.html",
      favicon: "src/favicon.png",
    }),
  ],
};
