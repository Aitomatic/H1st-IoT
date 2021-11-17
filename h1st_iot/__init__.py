"""H1st IoT package metadata."""


from importlib.metadata import version
from typing import Sequence   # TODO: Py3.9: use generics/collections.abc


__all__: Sequence[str] = ('__version__',)


__version__: str = version(distribution_name='H1st-IoT')