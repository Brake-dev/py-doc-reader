import { Mastra } from "@mastra/core";

import { intentAgent } from "./agents/intentAgent.js";

export const mastra = new Mastra({
  agents: { intentAgent },
});
