# Restoration Gallery

Build a side-by-side gallery of original and restored images.

## What this project does

This is an original command-line utility for analyzing or presenting computer vision outputs. It does not include pretrained weights, training code, or copied research implementations.

## Input and output

Input example: `Place matching image filenames in separate originals/ and restored/ folders.`

Run: `python main.py originals restored gallery.html`

See `python main.py --help` for positional arguments. Output is written to the requested file, except the neighbor search, which prints ranked results.

## Related tools

NAFNet, Real-ESRGAN, or any image restoration model. This project is independent of those implementations and consumes their exported results where applicable.

## Requirements

Python 3.10 or newer. No third-party Python packages are required.

## Limitations

The tool generates an HTML comparison; it does not perform restoration. Model inference is not locally tested. The utility has only been checked for syntax and on small synthetic inputs.

## License

MIT. See `LICENSE`.
