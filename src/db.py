
import sqlite3
from dataclasses import dataclass


# queries to create the db tables


@dataclass
class File:
    name: str
    link: str
    tags: "list[str]"


def create_tables():
    db = sqlite3.connect('files.db')
    cursor = db.cursor()

    cursor.execute('''
    create table if not exists files(
    fid         int auto_increment primary key,
    name        text not null,
    drive_url   text not null
    );''')
    cursor.execute('''
    create table if not exists tags(
    tid         int primary key,
    name        text not null
    );''')
    cursor.execute('''
	create table if not exists file_tags(
  	tid         int,
    fid         int,
    primary key (tid, fid)
    );''')

    db.commit()
    db.close()


def list_files(query: str, tags: "list[str]") -> "list[File]":
    """
    List files in database that match query (a simple search box query) and tags.
    """
    # TODO: query from db

    return [
        File(
            name="file1",
            link="https://example.com/file1",
            tags=["tag1", "tag2"]
        ),
        File(
            name="file2",
            link="https://example.com/file2",
            tags=["tag1", "tag2"]
        ),
        File(
            name="file3",
            link="https://example.com/file3",
            tags=["tag1", "tag2"]
        ),
    ]


def add_files(files: "list[File]"):
    """
    Add files to database.
    """
    # TODO: add to db
    """
    for file in files:
        query = f"INSERT INTO files(name, drive_url) VALUES ('{file.name}', '{file.link}');"
        cursor.execute(query)
        db.commit()
        print("added", file.name)

    """
    print("adding file")
    pass
