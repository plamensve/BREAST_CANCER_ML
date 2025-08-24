import pandas as pd
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


class FeatureStats:
    def __init__(self, *, dataset=None, target_column=None, feature=None):
        self.dataset = dataset
        self.target_column = target_column
        self.feature = feature

    def display_boxplot(self):
        # Аdd boxplot to visualize outliers and compare distribution for Negative vs. Positive results
        plt.figure(figsize=(10, 5))
        sns.boxplot(x=self.target_column,
                    y=self.feature,
                    data=self.dataset,
                    hue=self.target_column,
                    palette={0: 'blue', 1: 'red'},
                    dodge=False)

        plt.title(f'{self.feature} Boxplot')
        plt.xticks([0, 1], ['Negative', 'Positive'], rotation=45)
        plt.legend([], [], frameon=False)
        plt.show()

    def display_ttest(self):
        negative = self.dataset[self.dataset[self.target_column] == 0][self.feature]
        positive = self.dataset[self.dataset[self.target_column] == 1][self.feature]

        t_stat, p_value = ttest_ind(negative, positive)

        results = {
            'Feature': [self.feature],
            't-statistic': t_stat,
            'p-value': p_value
        }

        df_results = pd.DataFrame(results)

        display(df_results)

    def display_all(self):
        self.display_boxplot()
        self.display_ttest()