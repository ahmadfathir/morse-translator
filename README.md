# Translate Morse Code

Python script to convert WAV audio files containing Morse code into readable text.

## Description

`translate-morse.py` tool can:
- Analyze WAV audio files containing Morse code sounds
- Detect short (dot) and long (dash) beeps
- Convert Morse code to plain text
- Support letters A-Z and numbers 0-9

## Requirements

### Dependencies

Make sure you have installed the following library:

```bash
pip install pydub
```

### System Requirements

- Python 3.x
- WAV format audio files
- `pydub` library for audio processing

## Usage

### 1. File Preparation

Ensure you have a WAV audio file containing Morse code. The file should:
- **Format**: WAV only (other formats not supported)
- **Content**: Clear beeps of different durations (short for dots, long for dashes)
- **Quality**: Good audio quality with distinct pauses between letters and words
- **Channel**: Will be automatically converted to mono during processing

### 2. Running the Script

The script uses interactive input for file selection. Simply run:

```bash
python translate-morse.py
```

You'll see the ASCII art header and then be prompted:

```
Masukkan path file audio Morse (.wav):
```

Enter the path to your WAV file. Examples:
- `morse.wav` (file in current directory)
- `/home/user/audio/morse.wav` (absolute path)
- `../audio/morse.wav` (relative path)

### 3. Output

The script will display:
1. **Kode Morse**: Raw morse code with dots (.) and dashes (-)
2. **Hasil Decode**: Final translated text in uppercase

The script will produce two outputs:
1. **Morse Code**: Representation of dot (.) and dash (-) symbols
2. **Decoded Result**: Translated text

## Example

```bash
# Run with morse.wav file
python translate-morse.py
```

**Example Output:**

```
Morse Code: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
Decoded Result: HELLO WORLD
```

## Configuration Parameters

The script uses the following adjustable parameters:

- `min_silence_len=50`: Minimum silence duration for detection (ms)
- `silence_thresh=-40`: Threshold to detect silence (dB)
- Beep duration:
  - `< 100ms`: Dot (.)
  - `>= 100ms`: Dash (-)
- Pause duration:
  - `150-300ms`: Pause between letters
  - `>= 300ms`: Pause between words

## Troubleshooting

### Error "ModuleNotFoundError: No module named 'pydub'"

```bash
pip install pydub
```

### Audio not detected correctly

- Ensure WAV file quality is good
- Adjust `silence_thresh` (higher value for noisy audio)
- Adjust `min_silence_len` if pauses are too short or long

### Inaccurate decode result

- Check audio file quality
- Adjust duration thresholds for dot/dash
- Ensure proper pauses between letters and words

## Supported Morse Code Structure

### Letters (A-Z)

```
A: .-    B: -...  C: -.-.  D: -..
E: .     F: ..-. G: --.   H: ....
I: ..    J: .--- K: -.-   L: .-..
M: --    N: -.   O: ---   P: .--.
Q: --.-  R: .-.  S: ...   T: -
U: ..-   V: ...- W: .--   X: -..-
Y: -.--  Z: --..
```

### Numbers (0-9)

```
0: -----  1: .----  2: ..---  3: ...--  4: ....-
5: .....  6: -....  7: --...  8: ---..  9: ----.
```

## Contribution

To contribute or report bugs:

1. Fork this repository
2. Create a branch for a new feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This script is intended for educational and IDN CTF (Capture The Flag) purposes.

