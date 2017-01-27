:description: This package provides useful scripts to analyze datasets
  themselves and run an method for mining review graphs.

.. _top:

Scripts for Analyzing Review Graphs
===================================
.. raw:: html

   <div class="addthis_inline_share_toolbox"></div>

This package provides useful scripts to analyze datasets themselves and
run an method for mining review graphs.

Installation
------------
Use ``pip`` to install this package.

.. code:: sh

    $ pip install --upgrade rgmining-script


dataset command
----------------
dataset command provides a set of functions to inspect a dataset. Those
functions are divided to two groups, analyzing reviewer information and
analyzing product information.

.. toctree::
  :maxdepth: 2

  reviewer
  product


analyze command
---------------
analyze command loads a dataset and run a method to find anomalous
reviewers and compute a rating summary of each product.

.. toctree::
  :maxdepth: 1

  analyze


API Reference
---------------
.. toctree::
  :glob:
  :maxdepth: 2

  modules/*


License
---------
This software is released under The GNU General Public License Version 3,
see `COPYING <https://github.com/rgmining/script/blob/master/COPYING>`_ for more detail.
