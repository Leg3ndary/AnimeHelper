#!/usr/bin/env python3

import asyncio
import os
import json

from colorama import Fore, Style


async def open_episode(episode: int) -> None:
    """
    Open an episode in the browser.
    """
    os.system(f"chromium-browser https://animixplay.to/v1/naruto-shippuuden-dub/ep{episode}")


async def main() -> None:
    """
    Main function."""
    print(f"{Fore.GREEN}Pulling latest from GitHub...{Style.RESET_ALL}")
    os.system("git pull")
    print(f"{Fore.GREEN}Pulled latest from GitHub!{Style.RESET_ALL}")

    print(f"Watching {Fore.YELLOW}Naruto Shippuden [Dubbed]{Style.RESET_ALL}")

    if os.path.exists("current.json"):
        with open("current.json", "r", encoding="utf-8") as file:
            episode = json.loads(file.read())["episode"]
            print(f"{Fore.GREEN}Current episode: {episode}{Style.RESET_ALL}")
        with open("current.json", "w+", encoding="utf-8") as file:
            json.dump({"episode": episode + 1}, file)
    else:
        with open("current.json", "w+", encoding="utf-8") as file:
            rinput = input(
                f"{Fore.RED}No current episode found. Please enter a number to start from.{Style.RESET_ALL}: "
            )
            episode = int(rinput)
            json.dump({"episode": episode + 1}, file)

    asyncio.create_task(open_episode(episode))


if __name__ == "__main__":
    asyncio.run(main())
