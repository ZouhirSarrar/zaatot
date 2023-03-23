from zaatot.routes import router


@router.get("/", tags=["home"])
async def get_index():
    return {"haha": "LOL"}
