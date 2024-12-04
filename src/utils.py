def fn_out(day: int) -> str:
    return f"out/{day:02d}.txt"


def fn_in(day: int) -> str:
    return f"in/{day:02d}.txt"


def download_file(day: int) -> None:
    from requests import get
    from dotenv import dotenv_values

    env = dotenv_values()
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookies = {"session": env["session"]}
    puzzle = get(url, cookies=cookies).text
    with open(fn_in(day), "w") as f:
        f.write(puzzle)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    download_file(args.day)
