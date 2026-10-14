import pandas as pd

from script import data


def create_dataframe():
    return pd.DataFrame(data)


def test_dataframe_shape():
    df = create_dataframe()

    assert df.shape == (4, 3)


def test_dataframe_columns():
    df = create_dataframe()

    assert list(df.columns) == ["Name", "Age", "City"]


def test_dataframe_names():
    df = create_dataframe()

    assert df["Name"].tolist() == [
        "Alice",
        "Bob",
        "Charlie",
        "David",
    ]


def test_dataframe_ages():
    df = create_dataframe()

    assert df["Age"].tolist() == [25, 30, 35, 40]


def test_dataframe_cities():
    df = create_dataframe()

    assert df["City"].tolist() == [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
    ]


def test_mean_age():
    df = create_dataframe()

    assert df["Age"].mean() == 32.5


def test_age_column_is_numeric():
    df = create_dataframe()

    assert pd.api.types.is_numeric_dtype(df["Age"])


def test_no_missing_values():
    df = create_dataframe()

    assert df.isnull().sum().sum() == 0
