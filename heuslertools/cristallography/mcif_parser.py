from crystals.parsers import CIFParser, ParseError
from crystals.spg_data import HM2Hall, Number2Hall, SymOpsHall
from contextlib import AbstractContextManager, suppress

class MCIFParser(CIFParser):

    def symmetry_operators(self):
        """
        Returns the symmetry operators that map the fractional atomic positions in a
        CIF file to the crystal *conventional* unit cell.
        Returns
        -------
        sym_ops : iterable of ndarray, shape (4,4)
            Transformation matrices. Since translations and rotation are combined,
            the transformation matrices are 4x4.
        """
        block = self.structure_block

        equivalent_sites_str = None
        for tag in ["_symmetry_equiv_pos_as_xyz", "_space_group_symop_operation_xyz", "_space_group_symop_magn_operation.xyz"]:
            with suppress(KeyError):
                equivalent_sites_str = block.GetLoop(tag).get(tag)

        # P1 space group only has a single equivalent site
        if isinstance(equivalent_sites_str, str):
            equivalent_sites_str = [equivalent_sites_str]

        with suppress(ParseError):
            if not equivalent_sites_str:
                equivalent_sites_str = SymOpsHall[self.hall_symbol()]
            elif len(equivalent_sites_str) != len(SymOpsHall[self.hall_symbol()]):
                warnings.warn(
                    "The number of equivalent sites is not in line with the database. The file might be incomplete"
                )

        return list(map(self.sym_ops_from_equiv, equivalent_sites_str))