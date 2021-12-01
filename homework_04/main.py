"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from models import User, Post, Base, engine, Session
from jsonplaceholder_requests import get_data


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def fill_table_users(user_data, post_data):
    user_list = [User(username=user["username"], name=user["name"], email=user["email"]) for user in user_data]
    post_list = [Post(title=post["title"], body=post["body"], user_id=post["userId"]) for post in post_data]
    async with Session() as session:
        async with session.begin():
            session.add_all(
                user_list,
            )
            session.add_all(
                post_list,
            )


async def async_main():
    await create_tables()
    user_data, post_data = await get_data()
    await fill_table_users(user_data, post_data)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
