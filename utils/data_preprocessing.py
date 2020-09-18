def get_data(path, layer=0, nans=False):
    """ get_data function

        Description: This function will take the given path and user-defined layer from the dataset, import the datafiles, and then return the combined pandas DataFrame

        Arguments:
            path => string, path to the directory containing the l1-doh.csv, l1-nonhod.csv, etc files.
            layer => int, the level of layer desired. This will change the dataset that is imported. Values can be 1 or 2. Default is 0.
            nans => boolean, Whether the user wants NaNs in the data or wants them removed. This function will automatically remove all rows with Nan values.

        Returns:
            df => pandas.DataFrame, contains complete data

        Raises:
            AttributeError for incorrect layer number
            Any additional read errors are raised to the user

    """
    import pandas as pd

    if layer not in [1,2]:
        raise AttributeError('Must provide valid layer for dataset: layer equals 1 or 2')
    else:

        # Select the files that the user has chosen
        filenames = []
        if layer == 1:
            filenames.append('l1-doh.csv')
            filenames.append('l1-nondoh.csv')
        else:
            filenames.append('l2-benign.csv')
            filenames.append('l2-malicious.csv')

        # Read the files into dataframes
        df0 = pd.read_csv(path + '/' + filenames[0])
        df1 = pd.read_csv(path + '/' + filenames[1])

        df = pd.concat([df0, df1])

        # Remove any rows with Nan values
        if not nans:
            df.dropna(axis='index', inplace=True)

        return df
