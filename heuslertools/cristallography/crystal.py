import crystals as c
import numpy as np

class Crystal():

    def __init__(self, xuCrystal, base=[[1,0,0], [0,1,0], [0,0,1]]):
        self.xuCrystal = xuCrystal
        self.base = base
        self.generateLattice()
        self.a = self.xuCrystal.lattice.a
        self.b = self.xuCrystal.lattice.b
        self.c = self.xuCrystal.lattice.c
    
    def generateLattice(self):
        self.atom_properties = {}
        atoms = []
        for a, pos, occ, b in self.xuCrystal.lattice.base():
            atoms.append(c.Atom(a.name, pos))
            if a.name not in self.atom_properties:
                self.atom_properties[a.name] = {
                    'color': a.color,
                    'weight': a.weight,
                    'radius': a.radius
                }
        self.crystal = c.Crystal(atoms, self.base)

    def get_3D_lattice(self, u, v, w, offset=[0,0,0], units=False):
        x, y, z, c, r = [], [], [], [], []
        for atm in self.crystal.supercell(u+1, v+1, w+1):
            coords = atm.coords_fractional
            if coords[0] <= u and coords[1] <= v and coords[2] <= w:
                coords = np.sum([coords, offset], axis=0)
                if units:
                    coords[0] = coords[0]*self.xuCrystal.lattice.a*1e-10
                    coords[1] = coords[1]*self.xuCrystal.lattice.b*1e-10
                    coords[2] = coords[2]*self.xuCrystal.lattice.c*1e-10
                x.append(coords[0])
                y.append(coords[1])
                z.append(coords[2])
                c.append(self.atom_properties[str(atm)]['color'])
                r.append(self.atom_properties[str(atm)]['radius'])

        return np.asarray(x), np.asarray(y), np.asarray(z), np.asarray(c), np.asarray(r)

    def get_2D_lattice(self, u, v, w, plane, offset=[0,0,0], units=False):
        x, y, c, r = [], [], [], []
        for atm in self.crystal.supercell(u+1, v+1, w+1):
            coords = atm.coords_fractional
            if coords[0] <= u and coords[1] <= v and coords[2] <= w:                
                coords = np.sum([coords, offset], axis=0)
                if units:
                    coords[0] = coords[0]*self.xuCrystal.lattice.a*1e-10
                    coords[1] = coords[1]*self.xuCrystal.lattice.b*1e-10
                    coords[2] = coords[2]*self.xuCrystal.lattice.c*1e-10
                x.append(np.dot(coords, plane[0]/np.linalg.norm(plane[0])))
                y.append(np.dot(coords, plane[1]/np.linalg.norm(plane[1])))
                c.append(self.atom_properties[str(atm)]['color'])
                r.append(self.atom_properties[str(atm)]['radius'])
        return np.asarray(x), np.asarray(y), np.asarray(c), np.asarray(r)