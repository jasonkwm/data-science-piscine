from tqdm import tqdm
from time import sleep

def iterator():
    yield "#"

def ft_tqdm(lst: range) -> None:
    loading_bar = "["
    for i in range(40 - len(loading_bar)):
        
        loading_bar = loading_bar + "#"
    loading_bar = loading_bar + "]"
    print(loading_bar)
    yield "#"
    

# for elem in tqdm(range(333)):
#     sleep(0.005)

for i in ft_tqdm(range(333)):
    sleep(0.005)