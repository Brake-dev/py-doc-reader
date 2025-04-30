import { createOllama } from "ollama-ai-provider";
import { Agent } from "@mastra/core/agent";
import { Memory } from "@mastra/memory";

import { memoryConfig } from "../memory.js";

const ollama = createOllama({
  baseURL: "http://localhost:11434/api",
});

const model = ollama.chat("llama3.2", {
  simulateStreaming: true,
});

const memory = new Memory({
  ...memoryConfig,
  embedder: ollama.embedding("mxbai-embed-large"),
});

const prompt = `You are an intent assistant. Figure out the intent of users message.`;

export const intentAgent = new Agent({
  name: "Intent Agent",
  instructions: prompt,
  model,
  memory,
});
