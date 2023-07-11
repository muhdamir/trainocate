from fastapi import FastAPI

ch03 = FastAPI()


@ch03.get("/")
async def test_conn():
    return True


@ch03.get("/ha")
async def haha():
    return True
