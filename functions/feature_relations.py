import seaborn as sns
from matplotlib import pyplot as plt


class FeatureRelations:
    def __init__(self, *, dataset=None):
        self.dataset = dataset

    def show_confusion_metrix(self):
        correlation = self.dataset.corr(
            method='spearman'
        )

        plt.figure(figsize=(10, 5))
        sns.heatmap(correlation, cmap="Blues", annot=True, fmt=".2f")
        plt.title("Correlation Matrix")
        plt.show()