import asyncio
import argparse
import nest_asyncio

import tortoise
import uuid

import config
from kernel.tools import get_extension_models
from external_modules.context.models import Infs
from dp_client.client import Client


async def show_bots():
    await tortoise.Tortoise.init(
        db_url=config.NLAB_SOVA_DB_DSN,
        modules={
            'models': await get_extension_models()
        }
    )
    # Generate the schema
    await tortoise.Tortoise.generate_schemas()

    infs = await Infs.all()
    for inf in infs:
        print(f"{inf.uuid_str}\t{inf.inf_profile}")
    await tortoise.Tortoise.close_connections()


async def create(args):
    await tortoise.Tortoise.init(
        db_url=config.NLAB_SOVA_DB_DSN,
        modules={
            'models': await get_extension_models()
        }
    )
    # Generate the schema
    await tortoise.Tortoise.generate_schemas()

    u = uuid.UUID(args.buid).hex
    try:
        await Infs.get(uuid=args.buid)
        print(f"Бот с идентификатором {args.buid} уже существует")
    except tortoise.exceptions.DoesNotExist as err:
        inf = Infs(uuid=u, inf_profile=args.profile)
        await inf.save()
        print(f"Бот успешно создан")
    except tortoise.exceptions.BaseORMException as err:
        print(f"При создании бота произошла ошибка: {err}")
    await tortoise.Tortoise.close_connections()


async def change(args):
    await tortoise.Tortoise.init(
        db_url=config.NLAB_SOVA_DB_DSN,
        modules={
            'models': await get_extension_models()
        }
    )
    # Generate the schema
    await tortoise.Tortoise.generate_schemas()

    try:
        inf = await Infs.get(uuid=args.buid)
        inf.inf_profile = args.profile
        await inf.save()
        dp_client = Client(connection_string=config.NLAB_SOVA_ENGINE_HOST)
        dp_client.purge_inf(inf_id=inf.id)
        print(f"Изменения бота {args.buid} успешно сохранены")

    except tortoise.exceptions.DoesNotExist as err:
        print(f"Бот {args.buid} отсутствует")
    await tortoise.Tortoise.close_connections()


def run_change(args):
    nest_asyncio.apply()
    asyncio.run(change(args))


def run_create(args):
    nest_asyncio.apply()
    asyncio.run(create(args))


def run_list(args):
    nest_asyncio.apply()
    asyncio.run(show_bots())


parser = argparse.ArgumentParser(description='Утилита для управления ботами')
parser.set_defaults(func=run_list)

subparsers = parser.add_subparsers()
parser_create = subparsers.add_parser('bot:create', help='Создание бота')
parser_change = subparsers.add_parser("bot:change", help='Редактирование бота')
parser_list = subparsers.add_parser("bot:list", help='Список ботов')

parser_create.add_argument(
    '--buid',
    default="6944d0b0-ca59-4007-97bf-867d6c4385a9",
    type=str,
    help="uid бота (по умолчанию '6944d0b0-ca59-4007-97bf-867d6c4385a9')",
)
parser_create.add_argument(
    "--profile",
    default='default',
    type=str,
    help='профиль бота (по умолчанию "default")'
)
parser_create.set_defaults(func=run_create)
parser_change.add_argument(
    '--buid',
    default="6944d0b0-ca59-4007-97bf-867d6c4385a9",
    type=str,
    help="uid бота (по умолчанию '6944d0b0-ca59-4007-97bf-867d6c4385a9')"
)
parser_change.add_argument(
    "--profile",
    default='default',
    type=str,
    help='профиль бота (по умолчанию "default")'
)
parser_change.set_defaults(func=run_change)
parser_list.set_defaults(func=run_list)

args = parser.parse_args()
args.func(args)
