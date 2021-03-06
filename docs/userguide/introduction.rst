.. introduction:

###############################################################################
Introduction to the OpenPNM Framework
###############################################################################

===============================================================================
Module Overview
===============================================================================

The OpenPNM framework contains 6 Modules:


1 `Utilities`_:  Contains the Base class and several helper classes that are used as mixins to add functionality to the base objects

2 `Network`_: Consists of the GenericNetwork class which contains numerous methods for querying and manipulating networks, and subclasses which contain the generation protocols for various network topologies.  

3 `Geometry`_: Contains methods for applying pore scale geometry (e.g. pore size, throat length, etc)

4 `Fluids`_: Contains methods for estimating physical properties of fluids as a function of conditions in the network (e.g. viscosity as a function of temperature).

5 `Physics`_: Contains methods for calculating pore scale physics properties which combine fluid and geometry values (e.g. hydraulic conductance which combines pore size and fluid viscosity).

6 `Algorithms`_: This module is the home of the actual algorithms that use the network properties defined by the above modules (e.g. ordinary percolation for computing capillary pressure drainage curves, and Fickian diffusion algorithms for computing the diffusion of a gaseous species through the air filled pores).


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Utilities
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
This module contains the main abstract `Base` class from which all OpenPNM objects derive.  The main functionality offered by this class is the logger which outputs debugging info and error message to the console.  There is also a save and load object method.

This module also contains the `Tools` class, which possesses the for most important methods in the framework: `get_pore_data`, `set_pore_data`, `get_pore_info` and `set_pore_info`.  Cumulatively, these methods are referred to as the setters and getters.  They are used to access to actual network data.  The `Tools` class is a subclass of `Base` so posses all of the methods defined there, plus its own additional methods.  The `Network` and `Fluids` objects both inherit from `Tools`, while the other objects listed below only inherit from `Base`.  The reason for this is that both `Network` and `Fluids` store data on their own objects, hence they need access to the setters and getters.  The objects either store data on the `Network` or the `Fluid`, so don't require these tools.  

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Network
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
This module is the heart of OpenPNM.  It contains a GenericNetwork class which possesses suite of network query methods, as well as adjacency and incidence matrices. 

This module also contains numerous subclasses of the GenericNetwork, which possess the code for actually generating specific network topologies (e.g. cubic, random, etc).  The GenericNetwork class contains a `generate` method which is implemented only in the subclasses, which provides for a consistent interface for generating network topologies.  

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Geometry
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The Geometry class contains methods for calculating pore scale properties such as pore diameter and throat length.  It's name should not be confused with `topology`, which is handled by the Network module.  

Geometry objects are 'built' by the user to contain the specific methods that are to be used to calculate the pore and throat geometry properties.    For instance, a Geometry object can calculate pore volume assuming the pore is a sphere, cuboid or any other shape.  The user can use the methods supplied with OpenPNM, or add their own.  

There can be multiple Geometry objects defined for different locations in a Network simultaneously.  This was intended to allow for multi-layer media (such fuel cell gas diffusion layers with microporous layers on one side).  

The Geometry module contains a GenericGeometry class essentially contains 2 methods: ``add_method``, and ``regenerate``.  Geometry objects are essentially empty when initialized, and the user then adds the desired methods to the object (a process called `composition`).  For example, it is typical to assign a random seed to each pore which is subsequently used in the calculation of pore size from some sort of statistical distribution.  OpenPNM comes with several methods that can be used to generate random seeds.  These are stored in a submodule called `pore_seeds`, where the options include ``constant``, ``na`` and ``random``.  It is envisioned that each user may add their own methods for generating seeds (or any other calculation) to this submodule (or any other), so the process of adding methods to the object was designed to be as flexible and customizable as possible.  For more information on this process see the ref::`geometry <Geometry>` documentation.  The ``regenerate`` method does as its name suggests and regenerates all the data of the object.  As methods are added to the object (using ``add_method``) they are noted in a list, which is then referenced at regeneration time so all custom added methods are invoked. 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Fluids
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The `Fluids` class contains methods for estimating or predicting the thermo-physical properties of fluids, such as viscosity or density.  Despite it's name, this class can also be used to calculate solid properties.

Fluid objects are 'built' by the user to contain the specific methods that are to be used to calculate the fluid properties.  For instance, a Fluid object can calculate viscosity assuming a constant value, or Reynolds equation.  The user can use the methods supplied with OpenPNM, or add their own.  

Typically there will be multiple Fluid objects defined for each simulation, since most models will have at least an invading fluid and a defending fluid.  There can be an unlimited number of fluids associated with a Network.  

This module works identically to the `Geometry`_ module.  There is a GenericFluid object that contains only ``add_method`` and ``regenerate``.  Fluid objects are essentially empty when initialized, and the user adds the desired methods.  For example, the molar density of a fluid is a fundamental property that is required for many other calculations.  OpenPNM comes with several methods that can calculate the molar density of a fluid.  These stored in a submodule called `molar_density`, and options include ``constant`` and ``ideal_gas``.  It is envisioned that each user may add their own methods for generating seeds (or any other calculation) to this submodule (or any other), so the process of adding methods to the object was designed to be as flexible and customizable as possible.  For more information on this process see the ref::`fluids <Fluids>` documentation.  The ``regenerate`` method does as its name suggests and regenerates all the data of the object.  As methods are added to the object (using ``add_method``) they are noted in a list, which is then referenced at regeneration time so all custom added methods are invoked. 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Physics
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
asdf

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Algorithms
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
asdf

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Visualization
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
asdf

