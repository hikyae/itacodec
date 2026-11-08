# itacodec
Variation Selector Steganography

`itacodec` is a Python command-line tool for hiding text in Unicode variation selectors. It encodes the UTF-8 bytes of a message as variation-selector code points; decoding extracts those code points and reconstructs the message. Use `--normal` to prepend visible text, which can act as a carrier for the hidden message. This is obfuscation, not encryption.

## Features

- Hide UTF-8 text as a sequence of variation-selector code points.
- Extract and decode variation selectors from input text; other characters are ignored.
- Apply or decode nested layers with loop mode.
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
- -e, --encode: Encode the input's UTF-8 bytes as variation-selector code points.
- -d, --decode: Extract variation-selector code points and decode them as UTF-8.
- -l, --loop: Apply or decode nested encoding layers.
- -n, --normal: Prepend visible text before the encoded payload. Use with `-e`.
