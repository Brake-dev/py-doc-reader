import path from "path";
import { fileURLToPath } from "url";

const { dirname } = path;
const __dirname = dirname(fileURLToPath(import.meta.url));

export const dir = path.join(__dirname, "../public");
