import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { sendBaseSepoliaEth } from "./sendTx.js";

const server = new McpServer({
  name: "ethers-server",
  version: "1.0.0"
});

// Add an addition tool
server.registerTool("add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a tool to send ETH on Base Sepolia
server.registerTool("sendEth",
  {
    title: "Send ETH on Base Sepolia",
    description: "Send ETH from my wallet to a recipient on the Base Sepolia network",
    inputSchema: { recipient: z.string().min(42).max(42), amount: z.string() }
  },
  async ({ recipient, amount }) => {
    const result = await sendBaseSepoliaEth(recipient, amount);
    return { content: [{ type: "text", text: result }] };
  }
);

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
await server.connect(transport);