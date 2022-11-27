#!/usr/bin/env python3

import asyncio
import json
import os

from colorama import Fore, Style

animes = (
    "naruto-shippuuden-dub",
    "shingeki-no-kyojin-season-2",
    "shingeki-no-kyojin-season-3",
    "shingeki-no-kyojin-season-3-part-2",
)


async def open_episode(anime: str, episode: int) -> None:
    """
    Open an episode in the browser.
    """
    print(f"{Fore.BLUE}Opening {anime} episode {episode}...{Style.RESET_ALL}")
    os.system(f"chromium-browser https://animixplay.to/v1/{anime}/ep{episode}")


async def main() -> None:
    """
    Main function.
    """
    print(f"{Fore.GREEN}Pulling latest from GitHub...{Style.RESET_ALL}")
    os.system("git pull")
    print(f"{Fore.GREEN}Pulled latest from GitHub!{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Please Enter The Anime you want to Watch{Style.RESET_ALL}")
    for num, anime in enumerate(animes):
        print(f"{num} {anime}")
    anime = animes[int(input("Anime Number: "))]

    print(f"Watching {Fore.YELLOW}{anime}{Style.RESET_ALL}")

    if os.path.exists("current.json"):
        with open("current.json", "r", encoding="utf-8") as file:
            full = dict(json.loads(file.read()))
            episode = full[anime]
            full.update({anime: episode + 1})
            print(f"{Fore.GREEN}Current episode: {episode}{Style.RESET_ALL}")
        with open("current.json", "w+", encoding="utf-8") as file:
            json.dump(full, file)
    else:
        with open("current.json", "w+", encoding="utf-8") as file:
            rinput = input(
                f"{Fore.RED}No current episode found. Please enter a number to start from.{Style.RESET_ALL}: "
            )
            episode = int(rinput)
            json.dump(full, file)

    asyncio.create_task(open_episode(anime, episode))


if __name__ == "__main__":
    asyncio.run(main())
