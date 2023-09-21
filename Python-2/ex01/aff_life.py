from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def aff_life(df, country):
    """
    PROVIDE A LINE GRAPH BASE ON YEAR AND LIFE EXPENTANCY
    """
    try:
        found = df.loc[df["country"] == country]
        assert len(found.index) != 0, "country error"
        col = found.columns[1:].values.astype(int)
        row = found.iloc[0, 1:].values
        plt.title(f"{country} Life expentancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.plot(col, row)
        plt.show()
    except Exception as msg:
        print("Error: {}".format(msg))
        return None
    except KeyboardInterrupt:
        print("K Bye.")
        return None


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""
    df = load("life_expectancy_years.csv")
    aff_life(df, "Malaysia")
    pass


if __name__ == "__main__":
    main()