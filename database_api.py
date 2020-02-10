class FileEntry:
  idnum: int
  filename: str
  hashnum: str

  def __init__(self, filename: str, hashnum: str, idnum: int = None):
    self.idnum = idnum
    self.filename = filename
    self.hashnum = hashnum

  def __str__(self):
    return " FileEntry Instance \n--------------------\n  ID: %s\n  Filename: %s\n  Hash: %s" % (self.idnum, self.filename, str(self.hashnum) if self.hashnum is not None else "N/A")


def create_entry(file):
  pass


def search_hash(hash: str) -> FileEntry:
  pass


def search_name(name: str) -> FileEntry:
  pass


def update_entry(file: FileEntry):
  pass


def delete_from_id(id: int):
  pass


def delete_from_hash(hash: str):
  pass


def delete_from_name(name: str):
  pass