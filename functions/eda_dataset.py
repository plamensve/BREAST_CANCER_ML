from functions.display_plots import FeatureVisualizer
from functions.feature_stats import FeatureStats
from IPython.display import Markdown, display


class EdaDataset:
    def __init__(self, *, dataset=None, target_column=None):
        self.dataset = dataset
        self.target_column = target_column

    def analyze_feature(self, feature):
        display(Markdown(f"## Analyzing **{feature}**"))
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

        display(Markdown(f"### Distribution **{feature}**"))
        visualizer.display_all()

        display(Markdown(f"### Statistical analysis with Boxplot and t-test **{feature}**"))
        stats.display_all()