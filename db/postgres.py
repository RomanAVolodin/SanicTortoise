from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise

from core.config import settings


TORTOISE_ORM = {
    'connections': {'default': settings.database_dsn},
    'apps': {
        'models': {
            'models': ['models.customer', 'models.order', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}


def init_db(app: Sanic) -> None:
    register_tortoise(
        app,
        db_url=settings.database_dsn,
        modules={'models': ['models.customer', 'models.order']},
        generate_schemas=settings.debug_mode,
    )
