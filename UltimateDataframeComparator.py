import pandas as pd

df1 = pd.read_csv(r'D:\Career\Learning\Python\Projects\Sample\input.csv')
df2 = pd.read_csv(r'D:\Career\Learning\Python\Projects\Sample\output.csv')


def DfMetadataComparator(left_df, right_df):
    left_shape = left_df.shape
    right_shape = right_df.shape

    if left_shape != right_shape:
        print("Dataframe shapes do not match")
        print(
            f"Left dataframe shape: Rows: {left_shape[0]} Columns: {left_shape[1]}")
        print(
            f"Right dataframe shape: Rows: {right_shape[0]} Columns: {right_shape[1]}")
        return False

    if set(left_df.columns) != set(right_df.columns):
        print("Dataframes have different columns")
        print(f"Left dataframe columns: {left_df.columns}")
        print(f"Right dataframe columns: {right_df.columns}")
        return False

    if left_df.dtypes.to_dict() != right_df.dtypes.to_dict():
        print("Dataframes have different column types")
        print(f"Left dataframe types: {left_df.dtypes.to_dict()}")
        print(f"Right dataframe types: {right_df.dtypes.to_dict()}")
        return False

    return True


def DfComparator(left_df, right_df):
    if DfMetadataComparator(left_df, right_df):
        mismatch_df = pd.DataFrame(
            columns=['Line', 'Column', 'Left Value', 'Right Value'])

        for line, (row_1, row_2) in enumerate(zip(left_df.itertuples(index=False), right_df.itertuples(index=False)), 1):
            if row_1 != row_2:
                for (name, cell_1, cell_2) in zip(left_df.columns, row_1, row_2):
                    if cell_1 != cell_2:
                        mismatch_df = mismatch_df.append(
                            {'Line': line, 'Column': name, 'Left Value': cell_1, 'Right Value': cell_2}, ignore_index=True)

        return mismatch_df
    else:
        return None


DfComparator(df1, df2)
