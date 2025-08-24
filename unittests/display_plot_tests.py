import unittest
import warnings

import pandas as pd
from unittest.mock import patch
from matplotlib import pyplot as plt
from functions.display_plots import DisplayInitialInfo


class TestDisplayInitialInfo(unittest.TestCase):

    def setUp(self):
        self.dataset = pd.DataFrame({
            "feature1": [1, 2, 3, 4, 5, 6, 7],
            "target": [0, 1, 0, 1, 0, 1, 0]
        })
        self.obj = DisplayInitialInfo(dataset=self.dataset,
                                      target_column="target",
                                      feature="feature1")

    @patch("matplotlib.pyplot.show")
    def test_methods_run_without_error(self, mock_show):
        self.obj.feature_distribution()
        self.obj.compare_feature_by_diagnosis()
        self.obj.display_all()

        self.assertTrue(mock_show.called)
        self.assertGreater(len(plt.get_fignums()), 0)

    @patch("matplotlib.pyplot.hist")
    @patch("matplotlib.pyplot.show")
    def test_compare_feature_by_diagnosis_hist_calls(self, mock_show, mock_hist):
        self.obj.compare_feature_by_diagnosis()

        self.assertEqual(mock_hist.call_count, 2)

        args_benign, kwargs_benign = mock_hist.call_args_list[0]
        self.assertTrue(all(val in [1, 3, 5, 7] for val in args_benign[0]))

        args_malignant, kwargs_malignant = mock_hist.call_args_list[1]
        self.assertTrue(all(val in [2, 4, 6] for val in args_malignant[0]))


if __name__ == "__main__":
    unittest.main()
