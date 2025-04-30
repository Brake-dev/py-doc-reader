import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const { dirname } = path;
const __dirname = dirname(fileURLToPath(import.meta.url));

export const dir = path.join(__dirname, "../../public");

const app = express();

app.use(express.json());

app.use((req, res, next) => {
  const corsWhiteList = ["http://localhost:3000", "http://192.168.1.101:3000"];

  if (req.headers.origin && corsWhiteList.includes(req.headers.origin)) {
    res.header("Access-Control-Allow-Origin", req.headers.origin);
    res.header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE");
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, X-Requested-With, Content-Type, Accept"
    );
  }
  next();
});

app.get("/test", async (_req, res) => {
  res.status(200).send();
});

app.listen(8080, () => {
  console.log("Listening at port 8080");
});
