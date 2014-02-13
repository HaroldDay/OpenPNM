
"""
module throat_seeds
===============================================================================

"""
import scipy as sp


def constant(geometry,network,propname,value,**params):
    r"""
    Assign specified constant value
    """
    network.set_throat_data(locations=geometry,prop=propname,data=value)

def random(geometry,network,propname,**params):
    r"""
    Assign random number to throats
    note: should this be called 'poisson'?  
    """
    print('random: nothing yet')

def neighbor_min(geometry,network,propname,**params):
    r"""
    Adopt the minimum seed value from the neighboring pores
    """
    value=sp.amin(network.get_pore_data(prop='seed')[network.get_throat_data(prop='connections')],1)
    network.set_throat_data(locations=geometry,prop=propname,data=value)

def neighbor_max(geometry,network,propname,**params):
    r"""
    Adopt the maximum seed value from the neighboring pores
    """
    value=sp.amax(network.get_pore_data(prop='seed')[network.get_throat_data(prop='connections')],1)
    network.set_throat_data(locations=geometry,prop=propname,data=value)