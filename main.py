import uvicorn
from fastapi import FastAPI
from loguru import logger as log

from util.common import init_loguru, uvicorn_log

init_loguru("./conf/loguru_conf.json")
log_config = uvicorn_log("./conf/uvicorn_log.json")


# 创建 FastAPI 应用
app = FastAPI()


@app.get("/")
async def read_root():
    log.info("get /")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    log.info(f"get /items/{item_id}")
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    # 设置 uvicorn 日志级别为 info 并启动应用
    uvicorn.run(app, host="127.0.0.1", port=8000, log_config=log_config)
