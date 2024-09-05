import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pydantic import BaseModel


class CorePlotDetails(BaseModel):
    column: str
    title: str
    xlabel: str
    ylabel: str


class HistogramDetails(CorePlotDetails):
    bins: int
    color: str
    edgecolor: str = "black"


class BoxplotDetails(CorePlotDetails):
    color: str


def get_outliers(
    df: pd.DataFrame, column: str, min_only: bool = False, max_only: bool = False
) -> pd.DataFrame:
    """
    Given a dataframe and column name, calculate the Q1, Q3, and IQR for the column, then extract the upper and lower bound outliers into a new DataFrame.

    Parameters:
        df (pandas.DataFrame): a full record DataFrame to extract the outliers from
        column (string): the name of the column containing outliers
        min_only (boolean, optional): a flag for extracting only the minimum valued outliers. `False` by default
        max_only (boolean, optional): a flag for extracting only the maximum valued outliers. `False` by default
    """
    if column not in set(df.columns.to_list()):
        raise ValueError(f"Invalid column name. Options: '{df.columns.to_list()}'")

    df = df.copy()
    Q1 = df[column].quantile(q=0.25)
    Q3 = df[column].quantile(q=0.75)
    IQR = Q3 - Q1

    max_threshold = Q3 + 1.5 * IQR
    min_threshold = Q1 - 1.5 * IQR

    max_condition = df[column] > max_threshold
    min_condition = df[column] < min_threshold

    if min_only:
        return df[min_condition]

    if max_only:
        return df[max_condition]

    return df[min_condition | max_condition]


def plot_histograms(
    df: pd.DataFrame,
    details: list[HistogramDetails],
    figsize: tuple[int, int] = (15, 5),
) -> None:
    """Creates a set of histogram plots based on the number of detailed provided and displays them."""
    plt.figure(figsize=figsize)

    num_plots = len(details)

    for i, detail in enumerate(details):
        plt.subplot(1, num_plots, i + 1)
        plt.hist(
            df[detail.column],
            bins=detail.bins,
            color=detail.color,
            edgecolor=detail.edgecolor,
        )
        plt.title(detail.title)
        plt.xlabel(detail.xlabel)
        plt.ylabel(detail.ylabel)

    plt.tight_layout()
    plt.show()


def plot_boxes(
    df: pd.DataFrame,
    details: list[BoxplotDetails],
    figsize: tuple[int, int] = (15, 5),
) -> None:
    """Creates a set of box plots based on the number of detailed provided and displays them."""
    plt.figure(figsize=figsize)

    num_plots = len(details)

    for i, detail in enumerate(details):
        plt.subplot(1, num_plots, i + 1)
        sns.boxplot(
            df[detail.column],
            color=detail.color,
        )
        plt.title(detail.title)
        plt.xlabel(detail.xlabel)
        plt.ylabel(detail.ylabel)

    plt.tight_layout()
    plt.show()
