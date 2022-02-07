create table if not exists files(
  fid         INTEGER primary key AUTOINCREMENT,
  name        text not null,
  drive_url   text not null
);

create table if not exists tags(
  tid         INTEGER primary key AUTOINCREMENT,
  name        text not null
);

create table if not exists file_tags(
  tid         INTEGER,
  fid         INTEGER,
  primary key (tid, fid)
);
