# Scripts for Analyzing Review Graphs
[![GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/copyleft/gpl.html)
[![Build Status](https://travis-ci.org/rgmining/script.svg?branch=master)](https://travis-ci.org/rgmining/script)
[![wercker status](https://app.wercker.com/status/f973cb1847c2c30e801fa4aa1fd417a6/s/master "wercker status")](https://app.wercker.com/project/byKey/f973cb1847c2c30e801fa4aa1fd417a6)
[![Release](https://img.shields.io/badge/release-0.6.0-brightgreen.svg)](https://github.com/rgmining/script/releases/tag/0.6.0)

[![Logo](https://rgmining.github.io/script/_static/image.png)](https://rgmining.github.io/script/)

This package provides useful scripts to analyze datasets themselves and run
an method for mining review graphs.


## Installation
Use `pip` to install this package.

```sh
$ pip install --upgrade rgmining-script
```


## dataset command
dataset command provides a set of functions to inspect a dataset.
Those functions are divided to two groups, analyzing reviewer information and
analyzing product information.

### Analyzing reviewer information
To analyze reviewer information of a dataset, dataset command provides the
following subcommands:

* retrieve: output the ID of reviewers who review at least one of the given
  products,
* active: output the ID of reviewers who review at least threshold items,
* reviewer_size: output the number of reviews of each reviewer who reviews
  target products,
* filter: output reviews posted by reviewers whose IDs match the given set of
  IDs.


### Analyzing product information
To analyze product information of a dataset, dataset command provides the
following subcommands:

* average: output average rating scores of each product,
* distinct: output distinct product IDs,
* popular: output ID of products of which the member of reviews >= threshold.
* filter: output reviews posted to products of which IDs match the given set of
  IDs.
* variance: output variances of reviews for each product.


### Basic usage
The basic usage of this command is

```sh
$ dataset <dataset-specifier> <dataset-parameters> reviewer <subcommand>
```

or

```sh
$ dataset <dataset-specifier> <dataset-parameters> product <subcommand>
```


where the dataset-specifier is a name of the dataset to be analyzed.
It is depended on which libraries you have installed and
`dataset -h` returns a list of available dataset names.

dataset-parameters are optional arguments specified with `--dataset-param` flag.
The `--dataset-param` flag takes a string which connecting key and value with
a single =.
The `--dataset-param` flag can be given multi-times.
You can find what kinds of parameter keys are defined in the dataset you want
to use from documents of function `load` defined in the dataset.

For example, dataset `file` means loading a dataset from a file,
of which each line contains a review in [the JSON format](https://rgmining.github.io/dataset-io/modules/dataset_io.html#review-data).
To load such dataset, use `file` as the dataset-specifier and give the file path
as a dataset-parameter with `file` key, i.e. `--dataset-param file="path/to/file"`.


See [document site](https://rgmining.github.io/script/) for more information
about each subcommand.


## analyze command
analyze command loads a dataset and run a method to find anomalous reviewers
and compute a rating summary of each product.

The basic usage of this command is

```sh
$ analyze <dataset-specifier> <dataset-parameters> <method-specifier> <method-parameters>
```

The dataset-specifier and datasset-parameters are the same parameters described
in the dataset command explanation.

The method-specifier is a name of installed method.
You can see available method names by `analyze -h`.

method-parameters are optional arguments specified with `--method-param` flag.
The `--method-param` flag takes a string which connecting key and value with
a single =, and can be given multi-times.

You can find what kinds of parameter keys are defined in the method you want
to run from documents of the constructor of the review graph object defined in
the method.

For example, [Fraud Eagle](https://rgmining.github.io/fraud-eagle) takes one
parameter `epsilon` and you can give a value by `--method-param epsilon=0.25`.

See [document site](https://rgmining.github.io/script/) for more information.


## License
This software is released under The GNU General Public License Version 3,
see [COPYING](https://github.com/rgmining/script/blob/master/COPYING) for more detail.
