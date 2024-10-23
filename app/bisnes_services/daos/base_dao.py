from app.logger import logger

from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app.database import async_session_maker


def session_handler(func):
    async def wrapper(self, *args, **kwargs):
        try:
            async with async_session_maker() as session:
                result = await func(self, session, *args, **kwargs)
                await session.commit()
                return result
        except IntegrityError as e:
            logger.error("Ошибка целостности: %s", e.orig)
            await session.rollback()
            raise IndentationError()
        except OperationalError as e:
            logger.error("Эксплуатационная ошибка: %s", e.orig)
            raise OperationalError()
        except SQLAlchemyError as e:
            logger.error("Произошла ошибка базы: %s", e.args)
            raise SQLAlchemyError()
        except Exception as e:
            logger.error("Произошла неизвестная ошибка в базе: %s", e.args)
            raise Exception()

    return wrapper


class BaseDao:
    model = None

    @session_handler
    async def add_item(self, session, **kwargs) -> bool:
        smtp = insert(self.model).values(**kwargs)
        await session.execute(smtp)
        return True

    @session_handler
    async def get_item(self, session):
        result = await session.execute(select(self.model))
        return result.scalars().all()
