import glob

from os.path import join
from os.path import isfile
from os.path import dirname
from os.path import basename


__all__ = []
modules = glob.glob(join(dirname(__file__), "*.py"))

for m in modules:
    flag1 = isfile(m)
    flag2 = m.endswith("__init__.py")

    if flag1 and not flag2:
        __all__.append(basename(m)[:-3])