import pandas as pd
import numpy as np


class DataFrameComparator:
    def __init__(self):
        self.left_df = None
        self.right_df = None
        self.normalize_dtypes = None

    def compare(self,left_df, right_df, normalize_dtypes=True):
        self.left_df = left_df
        self.right_df = right_df
        self.normalize_dtypes = normalize_dtypes
        # create new dataframes without modifying input
        left_df = self.left_df.rename(columns=str.lower).sort_index(
            axis=1).reset_index(drop=True)
        right_df = self.right_df.rename(
            columns=str.lower).sort_index(axis=1).reset_index(drop=True)

        # validate dataframes before comparison
        if not left_df.columns.equals(right_df.columns):
            error_msg = 'Dataframes contain incomparable columns left_df/right_df: {}/{}'.format(
                left_df.columns, right_df.columns)
            raise Exception(error_msg)

        # normalise column data types
        if self.normalize_dtypes and not left_df.dtypes.equals(right_df.dtypes):
            right_df = right_df.astype(left_df.dtypes)

        # compare dataframes
        if left_df.equals(right_df):
            return pd.DataFrame()

        diff = left_df.ne(right_df).fillna(False)
        diff = diff.reset_index(drop=True)
        diff.index += 1

        diff_stacked = diff.stack()

        modified = diff_stacked[diff_stacked]
        modified.index.names = ['Line', 'Field']
        diff_location = np.where(diff)
        modified_data = np.column_stack(
            (left_df.values[diff_location], right_df.values[diff_location]))
        result = pd.DataFrame(modified_data, columns=[
                              'left_df', 'right_df'], index=modified.index)
        result = result[['left_df', 'right_df']]
        return result
