from dataclasses import dataclass

@dataclass
class File:
    name: str
    link: str
    tags: list[str]


def list_files(tags: list[str]) -> list[File]:
    """
    List files in database that match query and tags.
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
    # TODO: add to db
    pass
