from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "customer" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "email" VARCHAR(200) NOT NULL UNIQUE,
    "age" INT NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_customer_email_0c7dc6" ON "customer" ("email");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
