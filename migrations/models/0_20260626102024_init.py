from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "city" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "timezone" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "country" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "population" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm1v2jAQx7+K5VedxCZgsFa8o0jTNm1U6h40aZoi4xzBqmOn9mUta/nuk52EBAgMJL"
    "ZSwSvEPSR3P939Lw801iFI+2ogcEp75IEqFgPtkQV7g1CWJKXVGZCNpA/kRcTIomEcaY+M"
    "mbTQIDQEy41IUGhFe0SlUjqj5haNUFFpSpW4TSFAHQFOwNAe+fGzQahQIdyDLf4mN8FYgA"
    "wXyhShe7e3BzhNvO29wrc+0L1tFHAt01iVwckUJ1rNo4VCZ41AgWEI7vFoUle+qy7vsugo"
    "q7QMyUqs5IQwZqnESrtbMuBaOX5CoWv4gUbuLS/brc555+L1m85Fg1BfydxyPsvaK3vPEj"
    "2B4Rc6836GLIvwGEtu/neF3GDCTD26In4JnkWzDK9AtYleYSjxlSOzJ34xuw8kqAgnDlq3"
    "u4HWt/714F3/+qzd7b5w3WjDeDbbw9zVznwOaYkQRQy/tdoJYzXnyFG6lR7nKz3f8RHjN3"
    "fMhMGKR7f1uthVV9yOly1MscjjcU26DgqB06lCU699uWuz/FWCTgp4UsBjUsBEJ6lkvrDt"
    "R3Ax6e+juC+azacdxQORu68WjK0Tu8yxUerSechJ6E5Cd0xCBzETcheG84T9QPznI/gfbg"
    "Wz9k6bcBeK1Zwjn8YDOR99MIJP6u5H7tl4QFgZc7ogz+iC/AJjaz/y1q9uJeXIN7cqgm41"
    "doCYhz9PgK1mcwuArWZzLUDvWwTItULIdnAR4ofPV8N6iJWUJZCh4EgeiRQWDxPobD0/16"
    "8rOrb2VlaxnX3qf18mOvh4den71xYj45/iH3D51Idl9geg4icO"
)
