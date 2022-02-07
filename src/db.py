from dataclasses import dataclass
import os
import sqlite3


@dataclass
class File:
    name: str
    link: str
    tags: list[str]


def list_files(tags: list[str]) -> list[File]:
    """
    List files in database that have the tags.
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
            tags=["tag2", "tag3"]
        ),
        File(
            name="file3",
            link="https://example.com/file3",
            tags=["tag3", "tag4"]
        ),
    ]


def add_files(files: list[File]):
    """
    Add files to database.
    """
    
    for file in files:
        query1 = "INSERT INTO files(name, drive_url) VALUES (?,?) RETURNING fid"
        _cur.execute(query1, [file.name, file.link])
        fid = _cur.fetchone()[0]

        for tag in file.tags:
            tid = get_tagid_or_insert(tag)
            query2 = "INSERT INTO file_tags(tid,fid) VALUES (?,?)" 
            _cur.execute(query2, [tid, fid])


    _conn.commit()
    
    pass

def get_tagid_or_insert(tag:str) -> int:
    query = "SELECT tid FROM tags WHERE name = ?"
    _cur.execute(query, [tag])
    tid = _cur.fetchone()
    if tid is None:
        query = "INSERT INTO tags(name) VALUES (?) RETURNING tid"
        _cur.execute(query, [tag])
        tid = _cur.fetchone()[0]
    else:
        tid = tid[0]

    _conn.commit()  

    return tid  



_conn: sqlite3.Connection
_cur: sqlite3.Cursor


def connect(db_path: str):
    global _conn, _cur

    self_path = os.path.dirname(os.path.realpath(__file__))
    schema = os.path.join(self_path, "schema.sql")

    _conn = sqlite3.connect(db_path)
    _cur = _conn.cursor()
    with open(schema, "r") as f:
        _cur.executescript(f.read())
        _conn.commit()        
