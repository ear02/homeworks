import asyncio

from aiohttp import ClientSession

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def get_users():
    """
    get id, username, name from USERS_DATA_URL
    """
    res = []
    async with ClientSession() as session:
        json_data = await fetch_json(session, USERS_DATA_URL)

    for user in json_data:
        res.append({
            'id': user['id'],
            'name': user['name'],
            'username': user['username'],
            'email': user['email']
        })

    # print(res)
    return res


async def get_posts():
    """
    get id, userID, title, body from POSTS_DATA_URL
    """
    res = []
    async with ClientSession() as session:
        json_data = await fetch_json(session, POSTS_DATA_URL)

    for post in json_data:
        res.append({
            'id': post['id'],
            'title': post['title'],
            'userId': post['userId'],
            'body': post['body']
        })

    return res


async def get_data():
    return await asyncio.gather(
        get_users(),
        get_posts(),
    )
