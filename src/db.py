from dataclasses import dataclass

@dataclass
class File:
    name: str
    link: str
    tags: list[str]


def list_files(query: str, tags: list[str]) -> list[File]:
    """
    List files in database that match query and tags.
    """
    # TODO: query from db
    return []


def add_files(files: list[File]):
    """
    Add files to database.
    """
    # TODO: add to db
    pass
