from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",
    port=8050,
)

@mcp.tool()
def add(a:int,b:int)->int:
    return a+b

if __name__ == "__main__":
    transport = "sse"
    if transport=="stdio":
        print("Running server with stdio")
        mcp.run(transport="stdio")
    elif transport=="sse":
        print("Running server with sse")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknow transport {transport}")