from sklearn.base import BaseEstimator,TransformerMixin


class ColumnsRemover(TransformerMixin):
    """Removes selected columns"""

    def __init__(self, remove_cols=[]):
        self.removed_cols = remove_cols

    def __repr__(self):
        return f"ColumnsRemover(removed_cols={self.removed_cols})"

    def fit(self, x, y=None):
        self.selected_cols = list(set(x.columns) - set(self.removed_cols))
        return self

    def transform(self, x, y=None):
        data = x.copy()
        return data.loc[:, self.selected_cols]

    def get_feature_names_out(self, input_features=None):
        return self.selected_cols


class StringColumnsRemover(TransformerMixin):
    """Removes all columns with string values"""

    def __repr__(self):
        return f"StringColumnsRemover()"

    def fit(self, x, y=None):
        self.selected_cols = list(
            x.select_dtypes(include=['int64', 'float64']).columns
        )
        return self

    def transform(self, x, y=None):
        return x.loc[:, self.selected_cols]

    def get_feature_names_out(self, input_features=None):
        return self.selected_cols


class NullThresholdColumnsRemover(TransformerMixin):
    """Removes columns with nulls values above the threshold param"""

    def __init__(self, threshold=0.1):
        self.threshold = threshold

    def __repr__(self):
        return f"NullThresholdColumnsRemover(threshold={self.threshold})"

    def fit(self, x, y=None):
        max_nulls = x.shape[0] * self.threshold
        self.selected_cols = list(
            x.columns[x.isnull().sum() < max_nulls]
        )
        return self

    def transform(self, x, y=None):
        return x.loc[:, self.selected_cols]

    def get_feature_names_out(self, input_features=None):
        return self.selected_cols

