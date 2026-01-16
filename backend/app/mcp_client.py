# import os
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client
# from langchain_mcp_adapters.tools import load_mcp_tools
# from langchain.agents import create_agent

# async def run_gmail_mcp(prompt: str):
#     server_params = StdioServerParameters(
#         command="gmail-mcp-server",
#         args=[],
#         env={
#             "TRANSPORT": "stdio",
#             "OPENAI_API_KEY": os.environ["OPENAI_API_KEY"],
#             "GMAIL_CLIENT_ID": os.environ["GMAIL_CLIENT_ID"],
#             "GMAIL_CLIENT_SECRET": os.environ["GMAIL_CLIENT_SECRET"],
#         }
#     )

#     async with stdio_client(server_params) as (read, write):
#         async with ClientSession(read, write) as session:
#             await session.initialize()

#             tools = await load_mcp_tools(session)
#             agent = create_agent("openai:gpt-4o-mini", tools)

#             response = await agent.ainvoke({
#                 "messages": prompt
#             })

#             return response["messages"][-1].content



import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
import logging

logging.basicConfig(level=logging.INFO)

# Full path to MCP binary inside Docker container
MCP_BINARY = "/usr/local/bin/gmail-mcp-server"

async def run_gmail_mcp(prompt: str):
    import logging
    logging.info("Starting Gmail MCP server subprocess")
    server_params = StdioServerParameters(
        command="gmail-mcp-server",
        args=[],
        env={
            "TRANSPORT": "stdio",
            "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY"),
            "GMAIL_CLIENT_ID": os.environ.get("GMAIL_CLIENT_ID"),
            "GMAIL_CLIENT_SECRET": os.environ.get("GMAIL_CLIENT_SECRET"),
        }
    )

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                logging.info("MCP session initialized successfully")
                tools = await load_mcp_tools(session)
                logging.info(f"Loaded MCP tools: {[t.name for t in tools]}")
                agent = create_agent("openai:gpt-4o-mini", tools)
                response = await agent.ainvoke({"messages": prompt})
                return response["messages"][-1].content
    except Exception as e:
        logging.error("Gmail MCP failed")
        logging.exception(e)
        raise


# async def run_gmail_mcp(prompt: str):
#     server_params = StdioServerParameters(
#         command=MCP_BINARY,
#         args=[],
#         env={
#             "TRANSPORT": "stdio",
#             "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", ""),
#             "GMAIL_CLIENT_ID": os.environ.get("GMAIL_CLIENT_ID", ""),
#             "GMAIL_CLIENT_SECRET": os.environ.get("GMAIL_CLIENT_SECRET", ""),
#         }
#     )

#     async with stdio_client(server_params) as (read, write):
#         async with ClientSession(read, write) as session:
#             await session.initialize()

#             tools = await load_mcp_tools(session)
#             logging.info(f"Loaded tools: {[t.name for t in tools]}")

#             agent = create_agent("openai:gpt-4o-mini", tools)

#             response = await agent.ainvoke({
#                 "messages": prompt
#             })

#             return response["messages"][-1].content


