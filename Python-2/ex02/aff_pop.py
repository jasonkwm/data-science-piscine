import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_pop(df, countries):
    try:
        found = df.loc[countries]
        print(found)
        assert len(found.index) != 0, "country error"
        col = found.columns.values.astype(int)
        only_col = [str(i) for i in col if i >= 1800 and i <= 2050]
        found = found.loc[:,only_col]
        print(found)
        country_0 = found.loc[countries[0]]
        country_1 = found.loc[countries[1]]
        only_col = pd.Series(only_col).astype(int)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.plot(only_col, country_0, label=countries[0])
        plt.plot(only_col, country_1, label=countries[1])
        plt.legend()
        plt.show()
    except Exception as msg:
        print("Error: {}".format(msg))
        return None
    except KeyboardInterrupt:
        print("K Bye.")
        return None


def main():
    """This is a main, By Odin, by Thor ! Use your brain !!!"""
    df = load("population_total.csv")
    aff_pop(df, ["Belgium", "France"])
    pass


if __name__ == "__main__":
    main()