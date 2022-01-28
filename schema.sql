create table files(
  fid         int auto_increment primary key,
  name        text not null,
  drive_url   text not null
);

create table tags(
  tid         int primary key,
  name        text not null
);

create table file_tags(
  tid         int,
  fid         int,
  primary key (tid, fid)
);
