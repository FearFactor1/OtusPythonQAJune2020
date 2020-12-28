# Guide for postgresql docker setup

```
docker run -e POSTGRES_PASSWORD=root -p 3306:5432 -d postgres
docker exec -it {CONTAINER_ID} bash

psql -U postgres
Enter password: {PASSWORD}
\list - show databases
\c {database_name}

show databases; - показать БД
show tables; - показать таблицы
drop database; - удалить БД
drop table; - удалить таблицу
```