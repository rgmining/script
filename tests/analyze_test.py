#
# analyze_test.py
#
# Copyright (c) 2017 Junpei Kawamoto
#
# This file is part of rgmining-script.
#
# rgmining-script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rgmining-script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rgmining-script. If not, see <http://www.gnu.org/licenses/>.
#
# pylint: disable=import-error,invalid-name
"""Unit test for analyze command.
"""
from __future__ import absolute_import
from collections import defaultdict
import json
from StringIO import StringIO
import tempfile
import unittest

import analyze
import ria
from tests.dataset import store_dataset, SMALL_DATASET


class TestLoad(unittest.TestCase):
    """Test case for function load.
    """

    def test_ria_graph(self):
        """Test for creating a RIA graph with a small dataset.
        """

        reviewer_names = {review["member_id"] for review in SMALL_DATASET}
        product_names = {review["product_id"] for review in SMALL_DATASET}

        with tempfile.NamedTemporaryFile() as fp:
            store_dataset(fp)
            fp.flush()
            graph = analyze.load(
                "ria", ["alpha=2"], "file", ["file={0}".format(fp.name)])

        self.assertIsInstance(graph, ria.BipartiteGraph)
        self.assertEqual(graph.alpha, 2)
        self.assertTrue(graph.reviewers)
        for r in graph.reviewers:
            self.assertIn(r.name, reviewer_names)

        self.assertTrue(graph.products)
        for p in graph.products:
            self.assertIn(p.name, product_names)


class TestAnalyze(unittest.TestCase):
    """Test case for function analyze.
    """

    def test_iteration(self):
        """Test analyze runs at most given number of iteration.
        """
        with tempfile.NamedTemporaryFile() as fp:
            store_dataset(fp)
            fp.flush()
            graph = analyze.load(
                "ria", ["alpha=2"], "file", ["file={0}".format(fp.name)])

        buf = StringIO()
        analyze.analyze(graph, output=buf, loop=5, threshold=0)

        res = defaultdict(list)
        for line in buf.getvalue().split("\n"):
            if not line:
                continue
            obj = json.loads(line)
            res[obj["iteration"]].append(obj)

        self.assertIn(0, res)
        self.assertIn(5, res)
        self.assertNotIn(6, res)
        self.assertIn("final", res)


if __name__ == "__main__":
    unittest.main()
