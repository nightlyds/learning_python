import asyncio


async def main():
    task = asyncio.Task(other_function())
    returned_value = await task
    print(f"Returned value is {returned_value}")
    print("A")
    await asyncio.sleep(1)
    print("B")


async def other_function():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "returned value"

asyncio.run(main())


# Example
async def get_data(url):
    await asyncio.sleep(3)
    return {"id": 0, "name": "name", "email": "email@email.com"}


async def post_data(data, message):
    await asyncio.sleep(1)
    posted_data = (data, message)
    return True, posted_data


async def to_make_post(message):
    print("Start making the post..")
    get_data_task = asyncio.Task(get_data("url"))
    print("Data is getting..")
    _get_data = await get_data_task
    print(f"Data already got.. {_get_data}")
    post_data_task = asyncio.Task(post_data(get_data, message))
    print("Data is posting..")
    _post_data = await post_data_task
    print(f"Data already posted {_post_data}")
    print('Finished..')

asyncio.run(to_make_post('message'))