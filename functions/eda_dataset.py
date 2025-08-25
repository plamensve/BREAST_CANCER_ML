from functions.display_plots import FeatureVisualizer
from functions.feature_stats import FeatureStats


class EdaDataset:
    def __init__(self, *, dataset=None, target_column=None):
        self.dataset = dataset
        self.target_column = target_column

    def analyze_feature(self, feature):
        print(f"=== {feature} ===")
        visualizer = FeatureVisualizer(
            dataset=self.dataset,
            target_column=self.target_column,
            feature=feature
        )
        stats = FeatureStats(
            dataset=self.dataset,
            target_column=self.target_column,
            feature=feature
        )

        visualizer.display_all()
        stats.display_all()