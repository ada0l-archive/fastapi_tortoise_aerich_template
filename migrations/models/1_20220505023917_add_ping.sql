-- upgrade --
CREATE TABLE IF NOT EXISTS "ping" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL
);
-- downgrade --
DROP TABLE IF EXISTS "ping";
