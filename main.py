#!/usr/bin/env python3
"""Write one funny Wi-Fi SSID that hints at a whole story to /output/entry.txt."""
import os

NAME = "Sorry I Cheated, Take Me Back"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
