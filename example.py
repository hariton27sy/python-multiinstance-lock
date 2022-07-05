from contextlib import contextmanager
import os
import pathlib


# linux specific code
@contextmanager
def try_acquire_global_resource(label: str):
    if not label:
        label = 'base_lock'
    pid = str(os.getpid())
    dir_path = f'/tmp/{label}'
    os.makedirs(dir_path, exist_ok=True)
    path = pathlib.Path(dir_path, pid)
    path.touch(exist_ok=True)
    try:
        yield len(os.listdir(dir_path)) < 2
    finally:
        path.unlink(missing_ok=True)
