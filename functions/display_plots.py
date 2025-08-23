from matplotlib import pyplot as plt


class DisplayInitialInfo:
    def __init__(self, *, dataset=None, target_column=None, feature=None):
        self.dataset = dataset
        self.target_column = target_column
        self.feature = feature

    def feature_distribution(self):
        # Hist of the whole Radius mean feature
        plt.figure(figsize=(10, 5))
        self.dataset[self.feature].hist(bins=15, edgecolor='black')
        plt.title(f'{self.feature} [Distribution]')
        plt.xlabel('Values')
        plt.ylabel('Count')
        plt.grid(False)
        plt.show()

    def compare_feature_by_diagnosis(self):
        # Multi hist [M and B] - Comparing distributions
        plt.figure(figsize=(10, 5))
        plt.hist(self.dataset[self.dataset[self.target_column] == 0][self.feature],
                 label='Benign', bins=15, alpha=0.5)
        plt.hist(self.dataset[self.dataset[self.target_column] == 1][self.feature],
                 label='Malignant', bins=15, alpha=0.5)
        plt.legend()
        plt.title('Benign and Malignant Tumor [Distribution]')
        plt.xlabel('Values')
        plt.ylabel('Count')
        plt.show()

    def display_all(self):
        self.feature_distribution()
        self.compare_feature_by_diagnosis()


















