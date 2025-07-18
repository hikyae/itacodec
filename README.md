# itacodec
Variation Selector Encoder/Decoder

This is a Python script that encodes and decodes text using Unicode variation selectors. It provides a fun and obfuscated way to represent text by mapping each byte to a variation selector character.

## Features

- Encode any string into variation selectors.
- Decode variation selector strings back into the original text.
- Loop encoding/decoding for nesting obfuscation.
- Command-line interface with stdin and file input support.

## Usage
```bash
python itacodec.py -e -n "🥳" "hello world" > hello_world_in_emoji.txt
<hello_world_in_emoji.txt python itacodec.py -d
python itacodec.py -e -l -n "😈" "nested" "hidden" "messages" > nested.txt
<nested.txt python itacodec.py -d -l
```

Input strings can be provided as command-line arguments. If omitted, input is read from stdin.

### Options
- -e, --encode: Encode text to UTF-8 encoded variation selectors.
- -d, --decode: Decode variation selectors to text.
- -l, --loop: Use recursive loop encoding or decoding.
- -n, --normal: Prepend normal text before encoded string. Use with -e flag.
