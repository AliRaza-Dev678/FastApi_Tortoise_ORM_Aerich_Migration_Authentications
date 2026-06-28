from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL
);
        DROP TABLE IF EXISTS "users";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""


MODELS_STATE = (
    "eJztlm1r2zAQx7+K0KsOsuFkyVr8Lg2MbWwpdA8MSjGKrDiisuRK57VZmu8+JNux8+QlkK"
    "0p8auQe7Dvftz9zzMcq5AJ82bAYYp9NMOSxAz7aMneQpgkSWm1BiAj4QJpETEyoAkF7KMx"
    "EYa1EA6ZoZonwJXEPpKpENaoqAHNZVSaUsnvUxaAihhMmMY+urltIcxlyB6ZKf4md8GYMx"
    "EulclD+25nD2CaONtHCe9doH3bKKBKpLEsg5MpTJRcRHMJ1hoxyTQBZh8POrXl2+ryLouO"
    "skrLkKzESk7IxiQVUGl3RwZUScuPS7ANz3Bk3/K60+6edy/evutetBB2lSws5/OsvbL3LN"
    "ERGH7Dc+cnQLIIh7Hk5n7XyA0mRG9GV8SvwDOgV+EVqOroFYYSXzkyB+IXk8dAMBnBxELr"
    "9Wpo/ehfDz70r886vd4r243ShGazPcxdncxnkZYIgcfst5J7YazmnDhKu9LjfKUXOz4i9O"
    "6B6DBY86iO2ha77oo78aqFSBI5PLZJ20EhcCqVoDdrX+6ql79KUKOAjQKekgImKkkFcYXt"
    "PoLLSX8fxUPR9J53FI9E7r4bpy5rWufstUKXFhGNyjUqd0oqx2LCxT4MFwmHgfjPR/A/HA"
    "pizIPS4T4UqzknPo1Hcjv6THM62XQ9ck/t/SBlTHNBXtAF+cW02fiFt311KyknvrlVEbSr"
    "sQfEPPxlAmx73g4A2563FaDzLQOkSgLLdnAZ4qevV8PNECspKyBDTgE9IcENHCfQ+XZ+tl"
    "9bdGzMvahiO/vS/7lKdPD56tL1rwxE2j3FPeDyuQ/L/A9E3yW1"
)
