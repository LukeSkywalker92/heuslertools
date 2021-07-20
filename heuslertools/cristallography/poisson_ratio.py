def a_vert(substrate, layer, poisson_ratio):
    return ((substrate.a**2)*(poisson_ratio-1))/((poisson_ratio+1)*layer.a-2*substrate.a)