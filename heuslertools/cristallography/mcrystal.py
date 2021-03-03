from crystals import Crystal, symmetry_expansion
from .mcif_parser import MCIFParser
from functools import lru_cache
from pathlib import Path
from operator import attrgetter

CIF_ENTRIES = frozenset((Path(__file__).parent / "cifs").glob("*.cif"))

class MCrystal(Crystal):

    builtins = frozenset(map(attrgetter("stem"), CIF_ENTRIES))

    @classmethod
    @lru_cache(maxsize=len(builtins))
    def from_mcif(cls, path, **kwargs):
        """
        Returns a Crystal object created from a CIF 1.0, 1.1 or 2.0 file.
        Keyword arguments are passed to the Crystal constructor.
        Parameters
        ----------
        path : path-like
            File path
        """
        with MCIFParser(filename=path) as parser:
            return cls(
                unitcell=symmetry_expansion(
                    parser.atoms(), parser.symmetry_operators()
                ),
                lattice_vectors=parser.lattice_vectors(),
                source=str(path),
                **kwargs,
            )