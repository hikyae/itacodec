#!/usr/bin/env python
import argparse
import sys

VS1 = 0xFE00
VS16 = 0xFE0F
VS17 = 0xE0100
VS256 = 0xE01EF


def to_vs(byte: int) -> str:
    # byte must be between 0 and 255
    if 0 <= byte < 16:
        return chr(VS1 + byte)
    return chr(VS17 + byte - 16)


def to_cp(vs: str) -> int | None:
    vscp = ord(vs)
    if VS1 <= vscp <= VS16:
        return vscp - VS1
    elif VS17 <= vscp <= VS256:
        return vscp - VS17 + 16
    return None


def enc(text: str) -> str:
    return "".join(to_vs(byte) for byte in text.encode("utf-8"))


def enc_loop(texts: list) -> str:
    vs = ""
    for text in reversed(texts):
        vs = enc(f"{text}{vs}")
    return vs


def dec(text: str) -> str:
    cps: list = []
    for char in text:
        cp = to_cp(char)
        if cp is not None:
            cps.append(cp)
    return bytes(cps).decode("utf-8")


def dec_loop(cipher: str) -> list:
    texts: list = [cipher]
    decoded: str = dec(cipher)
    while decoded:
        texts.append(decoded)
        decoded = dec(decoded)
    return texts


def main():
    parser = argparse.ArgumentParser(
        description="Variation selector and UTF-8 character converter"
    )

    parser.add_argument("data", nargs="*", help="Data to convert")
    parser.add_argument(
        "-n",
        "--normal",
        type=str,
        default="",
        help="Normal string to prepend before encoded string",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-e",
        "--encode",
        action="store_true",
        help="Convert characters to variation selectors",
    )
    group.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="Convert variation selectors to characters",
    )

    parser.add_argument("-l", "--loop", action="store_true", help="Loop mode")

    args = parser.parse_args()

    if args.data:
        input_data = args.data
    else:
        input_data = [sys.stdin.read()]

    if args.encode:
        if args.loop:
            print(args.normal + enc_loop(input_data), end="")
        else:
            print(args.normal + enc(" ".join(input_data)), end="")
    else:
        if args.loop:
            print("\n---\n".join(dec_loop("".join(input_data))))
        else:
            print(dec(enc(" ").join(input_data)), end="")


if __name__ == "__main__":
    sys.exit(main())
