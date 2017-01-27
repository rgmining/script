:description: Explaining the basic usage of the analyze command.


Analyze command usage
=======================
.. raw:: html

   <div class="addthis_inline_share_toolbox"></div>


The basic usage of this command is

.. code:: sh

    $ analyze <dataset-specifier> <dataset-parameters> <method-specifier> <method-parameters> <options>

The dataset-specifier and datasset-parameters are the same parameters
described in the dataset command explanation.

The method-specifier is a name of installed method. You can see
available method names by ``analyze -h``.

method-parameters are optional arguments specified with
``--method-param`` flag. The ``--method-param`` flag takes a string
which connecting key and value with a single =, and can be given
multi-times.

You can find what kinds of parameter keys are defined in the method you
want to run from documents of the constructor of the review graph object
defined in the method.

For example, `Fraud Eagle <https://rgmining.github.io/fraud-eagle>`__
takes one parameter ``epsilon`` and you can give a value by
``--method-param epsilon=0.25``.

analyze also takes three options:

* ``--threshold``: threshold to distinguish an update is negligible
  (Default: :math:`10^{-5}`),
* ``--loop``: the maximum number of iterations (Default: 20),
* ``--output``: file path to store results (Default: stdout).

Most of methods, the Review Graph Mining project provides, are loop based
algorithms, which iterate some procedure until the update will be negligible.
The ``--threshold`` flag sets a threshold and if an update is smaller than
or equal to the threshold, it will be decided as negligible and the iteration
will be ended.

On the other hand, some methods with some datasets won't converge or even if
they will converge but it takes lots of time.
The ``--loop`` flag sets the maximum number of iterations to stop algorithms.


Datasets the Review Graph Mining Project provides
---------------------------------------------------
* :ref:`A Synthetic Review Dataset Loader <synthetic:top>`
  (`rgmining-synthetic-dataset <https://pypi.python.org/pypi/rgmining-synthetic-dataset>`_),
* :ref:`amazon:top`
  (`rgmining-amazon-dataset <https://pypi.python.org/pypi/rgmining-amazon-dataset>`_),
* :ref:`tripadvisor:top`
  (`rgmining-tripadvisor-datast <https://pypi.python.org/pypi/rgmining-tripadvisor-dataset>`_).

All packages are available on `PyPI <https://pypi.python.org/pypi>`_ and you can
install them by ``pip install``.


Methods the Review Graph Mining Project provides
---------------------------------------------------
* :ref:`Mutually Reinforcing Analysis (MRA) <ria:top>` [#DEXA2011]_
  (`rgmining-ria <https://pypi.python.org/pypi/rgmining-ria>`_),
* :ref:`Repeated Improvement Analysis (RIA) <ria:top>` [#DEIM2015]_
  (`rgmining-ria <https://pypi.python.org/pypi/rgmining-ria>`_),
* :ref:`Detecting Product Review Spammers Using Rating Behaviors <ria:top>` [#CIKM2010]_
  (`rgmining-ria <https://pypi.python.org/pypi/rgmining-ria>`_),
* :ref:`Review Spammer Detection <rsd:top>` [#ICDM2011]_
  (`rgmining-rsd <https://pypi.python.org/pypi/rgmining-rsd>`_),
* :ref:`Fraud Eagle <fraud-eagle:top>` [#ICWSM13]_
  (`rgmining-fraud-eagle <https://pypi.python.org/pypi/rgmining-fraud-eagle>`_),
* :ref:`FRAUDAR <fraudar:top>` [#KDD2016]_
  (`rgmining-fraudar <https://pypi.python.org/pypi/rgmining-fraudar>`_).

All packages are also available on `PyPI <https://pypi.python.org/pypi>`_ and you can
install them by ``pip install``.


References
------------
.. [#DEXA2011] Kazuki Tawaramoto, `Junpei Kawamoto`_, `Yasuhito Asano`_, and `Masatoshi Yoshikawa`_,
  "|springer| `A Bipartite Graph Model and Mutually Reinforcing Analysis for Review Sites
  <http://www.anrdoezrs.net/links/8186671/type/dlg/http://link.springer.com/chapter/10.1007%2F978-3-642-23088-2_25>`_,"
  Proc. of `the 22nd International Conference on Database and Expert Systems Applications <http://www.dexa.org/>`_ (DEXA 2011),
  pp.341-348, Toulouse, France, August 31, 2011.
.. [#DEIM2015] `川本 淳平`_, 俵本 一輝, `浅野 泰仁`_, `吉川 正俊`_,
  "|pdf| `初期レビューを用いた長期間評価推定 <http://db-event.jpn.org/deim2015/paper/253.pdf>`_,"
  `第7回データ工学と情報マネジメントに関するフォーラム <http://db-event.jpn.org/deim2015>`_,
  D3-6, 福島, 2015年3月2日～4日. |deim2015-slide|
.. [#CIKM2010] `Ee-Peng Lim <https://sites.google.com/site/aseplim/>`_,
  `Viet-An Nguyen <http://www.cs.umd.edu/~vietan/>`_,
  Nitin Jindal,
  `Bing Liu`_,
  `Hady Wirawan Lauw <http://www.smu.edu.sg/faculty/profile/9621/Hady-W-LAUW>`_,
  "`Detecting Product Review Spammers Using Rating Behaviors
  <http://dl.acm.org/citation.cfm?id=1871557>`_,"
  Proc. of the 19th ACM International Conference on Information and Knowledge Management,
  pp.939-948, 2010.
.. [#ICDM2011] `Guan Wang <https://www.cs.uic.edu/~gwang/>`_,
  `Sihong Xie <http://www.cse.lehigh.edu/~sxie/>`_, `Bing Liu`_,
  `Philip S. Yu <http://bdsc.lab.uic.edu/people.html>`_,
  "`Review Graph Based Online Store Review Spammer Detection
  <http://ieeexplore.ieee.org/document/6137345/?reload=true&arnumber=6137345>`_,"
  Proc. of the 11th IEEE International Conference on Data Mining (ICDM 2011),
  pp.1242-1247, 2011.
.. [#ICWSM13] `Leman Akoglu <http://www.andrew.cmu.edu/user/lakoglu/>`_,
  Rishi Chandy, and `Christos Faloutsos`_,
  "|pdf| `Opinion Fraud Detection in Online Reviews by Network Effects
  <https://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/viewFile/5981/6338>`_,"
  Proc. of `the 7th International AAAI Conference on WeblogsS and Social Media
  <http://www.icwsm.org/2013/>`_ (ICWSM 2013), Boston, MA, July, 2013.
.. [#KDD2016] `Bryan Hooi <https://www.andrew.cmu.edu/user/bhooi/index.html>`_,
  `Hyun Ah Song <http://www.cs.cmu.edu/~hyunahs/>`_,
  `Alex Beutel <http://alexbeutel.com/>`_,
  `Neil Shah <http://www.cs.cmu.edu/~neilshah/>`_,
  `Kijung Shin <http://www.cs.cmu.edu/~kijungs/>`_,
  `Christos Faloutsos`_,
  "|pdf| `FRAUDAR: Bounding Graph Fraud in the Face of Camouflage
  <http://www.andrew.cmu.edu/user/bhooi/papers/fraudar_kdd16.pdf>`_,"
  Proc. of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016),
  pp.895-904, 2016.

.. _Junpei Kawamoto: https://www.jkawamoto.info
.. _Yasuhito Asano: http://www.iedu.i.kyoto-u.ac.jp/intro/member/asano
.. _Masatoshi Yoshikawa: http://www.db.soc.i.kyoto-u.ac.jp/~yoshikawa/
.. _川本 淳平: https://www.jkawamoto.info
.. _浅野 泰仁: http://www.iedu.i.kyoto-u.ac.jp/intro/member/asano
.. _吉川 正俊: http://www.db.soc.i.kyoto-u.ac.jp/~yoshikawa/
.. _Bing Liu: https://www.cs.uic.edu/~liub/
.. _Christos Faloutsos: http://www.cs.cmu.edu/afs/cs/usr/christos/www/


.. |springer| image:: img/springer.png

.. |pdf| raw:: html

  <i class="fa fa-file-pdf-o" aria-hidden="true"></i>

.. |deim2016-slide| raw:: html

  <a href="http://www.slideshare.net/jkawamoto/ss-59672505">
   <i class="fa fa-slideshare" aria-hidden="true"></i>
  </a>

.. |deim2015-slide| raw:: html

 <a href="http://www.slideshare.net/jkawamoto/deim2015-45470497">
  <i class="fa fa-slideshare" aria-hidden="true"></i>
 </a>
