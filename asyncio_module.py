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
async def getData(url):
    await asyncio.sleep(3)
    return {"id": 0, "name": "name", "email": "email@email.com"}

async def postData(data, message):
    await asyncio.sleep(1)
    posted_data = (data, message)
    return (True, posted_data)

async def toMakePost(message):
    print("Start making the post..")
    get_data_task = asyncio.Task(getData("url"))
    print("Data are getting..")
    get_data = await get_data_task
    print(f"Data already got.. {get_data}")
    post_data_task = asyncio.Task(postData(get_data, message))
    print("Data are posting..")
    post_data = await post_data_task
    print(f"Data already posted {post_data}")
    print('Finished..')

asyncio.run(toMakePost('message'))