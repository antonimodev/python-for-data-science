from tqdm import tqdm
from Loading import ft_tqdm
from time import sleep


def main() -> None:
    for elem in tqdm(range(500)):
        sleep(0.005)
    for elem in ft_tqdm(range(500)):
        sleep(0.005)


if __name__ == "__main__":
    main()
