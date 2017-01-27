:description: To analyze product information of a dataset, dataset product
  command provides several subcommands. This document explains basic usage of
  each command.


Analyzing product information
===============================
.. raw:: html

   <div class="addthis_inline_share_toolbox"></div>

To analyze product information of a dataset, dataset command provides
the following subcommands.

The basic usage of this command is

.. code:: sh

    $ dataset <dataset-specifier> <dataset-parameters> product <subcommand>

where the dataset-specifier is a name of the dataset to be analyzed. It
is depended on which libraries you have installed and ``dataset -h``
returns a list of available dataset names.

dataset-parameters are optional arguments specified with
``--dataset-param`` flag. The ``--dataset-param`` flag takes a string
which connecting key and value with a single =. The ``--dataset-param``
flag can be given multi-times. You can find what kinds of parameter keys
are defined in the dataset you want to use from documents of function
``load`` defined in the dataset.

For example, dataset ``file`` means loading a dataset from a file, of
which each line contains a review in `the JSON
format <https://rgmining.github.io/dataset-io/modules/dataset_io.html#review-data>`_.
To load such dataset, use ``file`` as the dataset-specifier and give the
file path as a dataset-parameter with ``file`` key, i.e.
``--dataset-param file="path/to/file"``.

The other datasets the Review Graph Mining project provides are:

* :ref:`A Synthetic Review Dataset Loader <synthetic:top>`
  (`rgmining-synthetic-dataset <https://pypi.python.org/pypi/rgmining-synthetic-dataset>`_),
* :ref:`amazon:top`
  (`rgmining-amazon-dataset <https://pypi.python.org/pypi/rgmining-amazon-dataset>`_),
* :ref:`tripadvisor:top`
  (`rgmining-tripadvisor-datast <https://pypi.python.org/pypi/rgmining-tripadvisor-dataset>`_).

All packages are available on `PyPI <https://pypi.python.org/pypi>`_ and you can
install them by ``pip install``.


average
--------
average subcommand outputs the average rating score of each product.
The output is formatted in a JSON format such as

.. code-block:: none

  {
    "product_id": <Product ID>,
    "summary": <Average rating score>
  }

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> product average

This command receives ``--csv`` flag, and if it is set, the output will be
formatted in a simple CSV format.


distinct
---------
distinct subcommand outputs the distinct product IDs in a chosen dataset.
In the output, each line has one product ID.

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> product distinct


popular
--------
popular subcommand takes an optional argument, threshold, and outputs IDs
of product to which the number of reviews are greater than or equal to the
threshold.
The default value of the threshold is 2.

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> product popular --threshold 5

The above example outputs IDs of product which at least 5 reviews are posted to.


filter
-------
filter subcommand takes a set of product IDs and outputs reviews posted to
the set of products.

The output format is as same as
`the JSON format
<https://rgmining.github.io/dataset-io/modules/dataset_io.html#review-data>`_,
i.e. each line has a JSON object such as

.. code-block:: none

  {
    "member_id": <Reviewer ID>,
    "product_id": <Product ID>,
    "rating": <Rating score>,
    "date": <Date the review posted>
  }

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> product filter <file>

The specified file consists of product IDs and each line has one ID.

This command receives ``--csv`` flag, and if it is set, the output will be
formatted in a simple CSV format.


variance
----------
variance subcommand outputs the variance of rating scores of each product.

Each line of the output is formatted as a JSON format such as

.. code-block:: none

  {
    "product_id": <Product ID>,
    "size": <number of reviews>,
    "variance": <variance of reviews>
  }

This command also receives ``--csv`` flag and ``--target <file>`` option.

If ``--csv`` is set, the output will be formatted in a simple CSV format.
If target is supplied, only products of which ID is in the target will be
outputted.
The specified file consists of product IDs and each line has one ID.
