import { FlatCompat } from "@eslint/eslintrc";
import globals from "globals";
import path from "path";
import { fileURLToPath } from "url";
import js from "@eslint/js";
import ts from "typescript-eslint";
import react from "eslint-plugin-react";
import eslintPluginPrettierRecommended from "eslint-plugin-prettier/recommended";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

export default [
  {
    files: ["**/*.{js,mjs,ts,jsx,tsx}"],
    languageOptions: {
      globals: {
        ...globals.browser,
      },
    },
    plugins: {
      react,
    },
  },
  js.configs.recommended,
  ...ts.configs.recommended,
  react.configs.flat.recommended,
  ...compat.extends("plugin:react-hooks/recommended"),
  eslintPluginPrettierRecommended,
  {
    ignores: ["node_modules", "dist"],
  },
];
