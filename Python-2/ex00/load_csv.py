import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    loading csv provided
    """
    try:
        assert isinstance(path, str), "path problem"
        df = pd.read_csv(path, index_col=None)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except AssertionError as msg:
        print("AssertionError: {}".format(msg))
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
