import { PostgresStore, PgVector } from "@mastra/pg";

export const memoryConfig = {
  storage: new PostgresStore({
    host: "localhost",
    port: 4444,
    user: "mastra",
    database: "mastra",
    password: "zeus",
  }),
  vector: new PgVector("postgresql://mastra:zeus@localhost:4444/mastra"),
  options: {
    semanticRecall: {
      topK: 10,
      messageRange: 2,
    },
  },
};
