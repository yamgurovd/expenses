CREATE TABLE "cards"(
    "id" INTEGER NULL,
    "currensy_id" INTEGER NULL,
    "label" VARCHAR(100) NULL
);
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_id_unique" UNIQUE("id");
CREATE TABLE "currency"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "unit" FLOAT(10) NOT NULL
);
ALTER TABLE
    "currency" ADD PRIMARY KEY("id");
CREATE TABLE "expenses"(
    "id" INTEGER NOT NULL,
    "category_id" INTEGER NOT NULL,
    "card_id" INTEGER NOT NULL,
    "sum" FLOAT(8) NOT NULL,
    "date" DATE NOT NULL,
    "comment" VARCHAR(500) NOT NULL
);
ALTER TABLE
    "expenses" ADD PRIMARY KEY("id");
CREATE TABLE "category"(
    "id" INTEGER NOT NULL,
    "name" VARCHAR(100) NOT NULL
);
ALTER TABLE
    "category" ADD PRIMARY KEY("id");
CREATE TABLE "analytics"(
    "id" INTEGER NOT NULL,
    "date_from" DATE NOT NULL,
    "date_to" DATE NOT NULL,
    "category_id" INTEGER NOT NULL,
    "sum_category_period" FLOAT(8) NOT NULL,
    "general_expenses" FLOAT(8) NOT NULL,
    "general_income" FLOAT(8) NOT NULL
);
ALTER TABLE
    "analytics" ADD PRIMARY KEY("id");
CREATE TABLE "income"(
    "id" INTEGER NOT NULL,
    "category_id" INTEGER NOT NULL,
    "card_id" INTEGER NOT NULL,
    "sum" FLOAT(8) NOT NULL,
    "date" DATE NOT NULL,
    "comment" VARCHAR(500) NOT NULL
);
ALTER TABLE
    "income" ADD PRIMARY KEY("id");
ALTER TABLE
    "analytics" ADD CONSTRAINT "analytics_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "category"("id");
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_id_foreign" FOREIGN KEY("id") REFERENCES "income"("card_id");
ALTER TABLE
    "income" ADD CONSTRAINT "income_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "category"("id");
ALTER TABLE
    "expenses" ADD CONSTRAINT "expenses_category_id_foreign" FOREIGN KEY("category_id") REFERENCES "category"("id");
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_currensy_id_foreign" FOREIGN KEY("currensy_id") REFERENCES "currency"("id");
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_id_foreign" FOREIGN KEY("id") REFERENCES "expenses"("card_id");