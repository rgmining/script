:description: To analyze reviewer information of a dataset, dataset reviewer
  command provides several subcommands. This document explains basic usage of
  each command.


Analyzing reviewer information
================================
.. raw:: html

   <div class="addthis_inline_share_toolbox"></div>

To analyze reviewer information of a dataset, dataset command provides
the following subcommands.

The basic usage of this command is

.. code:: sh

    $ dataset <dataset-specifier> <dataset-parameters> reviewer <subcommand>

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

retrieve
----------
retrieve subcommand takes a list of product IDs and outputs IDs of reviewers who
review at least one product belonging to the given set of products.

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> reviewer retrieve <file>

The specified file consists of product IDs and each line has one ID.


active
-------
active subcommand takes an optional argument, threshold, and outputs IDs
of reviewers whose the number of reviews are greater than or equal to the
threshold.
The default value of the threshold is 2.

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> reviewer active --threshold 5

The above example outputs IDs of reviewers who review at least 5 products.


reviewer_size
--------------
reviewer_size subcommand takes a list of product IDs and outputs IDs of
reviewers who review at least one product in the given set of products,
the number of reviews they posts, and which product in the product set they
review.

The output is in the following JSON format:

.. code-block:: none

  {
    "reviewer": <Reviewer ID>,
    "size": <The number of reviews the reviewer posts>,
    "product": <Product ID which the reviewer reviews in the targets>
  }

Each line of the output has one above JSON object.

The usage is

.. code-block:: sh

  $ dataset <dataset-specifier> <dataset-parameters> reviewer reviewer_size <file>

The specified file consists of product IDs and each line has one ID.

This command receives ``--csv`` flag, and if it is set, the output will be
formatted in a simple CSV format.


filter
-------
filter subcommand takes a set of reviewer IDs and outputs reviews posted by
the set of reviewers.

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

  $ dataset <dataset-specifier> <dataset-parameters> reviewer filter <file>

The specified file consists of reviewer IDs and each line has one ID.

This command receives ``--csv`` flag, and if it is set, the output will be
formatted in a simple CSV format.
