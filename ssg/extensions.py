import sys
import importlib


from pathlib import Path


def load_module(self, directory, name):
    sys.path.insert(0, directory)
    import_module(name)
    sys.path.pop(0)

def load_directory(self, directory):
    for path in Path(directory).rglob(".py"):
        load_module(directory.as_posix(), path.stem)

def load_bundled(self):
    directory= Path(__file__).parent / "extensions"
    self.load_directory(directory)
