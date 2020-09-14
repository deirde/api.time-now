create table ban
(
    id               INTEGER
        primary key autoincrement,
    insert_date      INTEGER,
    last_update_date INTEGER,
    signature        TEXT,
    counter          INTEGER,
    is_banned        INTEGER
);

create table "default"
(
    id               INTEGER
        primary key autoincrement,
    insert_date      INTEGER,
    last_update_date INTEGER,
    name             TEXT,
    secret           TEXT,
    "limit"          TEXT,
    log              TEXT
);