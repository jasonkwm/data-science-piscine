

def ft_tqdm(lst: range) -> None:
    """
    Loading Bar function base on range
    """
    for i in lst:
        loading_bar = ""
        pcnt = (i + 1) / len(lst)
        fill = round(pcnt * 64)
        round_pcnt = round(pcnt * 100, 2)
        loading_bar += (("#" * fill) + (" " * (64 - fill)))
        yield print(f"{round_pcnt}% | [{loading_bar}] | {i + 1}/{len(lst)}   ",
                    end="\r")
