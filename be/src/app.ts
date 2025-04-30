import express from "express";
import path from "path";

import { dir } from "./utils.js";

const app = express();
app.use(express.json());

app.use((req, res, next) => {
  const corsWhiteList = ["http://localhost:3000", "http://192.168.1.101:3000"];

  if (req.headers.origin && corsWhiteList.indexOf(req.headers.origin) !== -1) {
    res.header("Access-Control-Allow-Origin", req.headers.origin);
    res.header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE");
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, X-Requested-With, Content-Type, Accept, authorization"
    );
  }
  next();
});

app.get("/test", async (_, res): Promise<any> => {
  try {
    return res.send(200);
  } catch (err) {
    return res.status(500).send(err);
  }
});

app.get("/test/:name", async (req, res): Promise<any> => {
  const name = req.params.name;
  try {
    return res.sendFile(path.join(dir, `${name}.json`));
  } catch (err) {
    return res.status(500).send(err);
  }
});

app.listen(8081, () => {
  console.log("Server listening at port 8081");
});
