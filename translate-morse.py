from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# ASCII Art Header
HEADER = """
#  ▗▖  ▗▖ ▗▄▖ ▗▄▄▖  ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▖    ▗▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖
#  ▐▛▚▞▜▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌     █  ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌   ▐▌ ▐▌ █ ▐▌ ▐▌▐▌ ▐▌
#  ▐▌  ▐▌▐▌ ▐▌▐▛▀▚▖ ▝▀▚▖▐▛▀▀▘  █  ▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌ ▝▀▚▖▐▌   ▐▛▀▜▌ █ ▐▌ ▐▌▐▛▀▚▖
#  ▐▌  ▐▌▝▚▄▞▘▐▌ ▐▌▗▄▄▞▘▐▙▄▄▖  █  ▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌▗▄▄▞▘▐▙▄▄▖▐▌ ▐▌ █ ▝▚▄▞▘▐▌ ▐▌
"""

CREDITS = """
    Script by           :  Ahmad Fathir
    Version             :  1.0
    Codename            :  lalatx1
    Follow me on Github :  @ahmadfathir
"""

def morse_to_text(morse_code):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    inverse_dict = {v: k for k, v in morse_dict.items()}

    words = morse_code.strip().split("   ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = [inverse_dict.get(letter, '?') for letter in letters]
        decoded_words.append("".join(decoded_letters))
    return " ".join(decoded_words)

def decode_morse_wav(file_path):
    try:
        audio = AudioSegment.from_wav(file_path)
        audio = audio.set_channels(1)
        audio = audio.apply_gain(-audio.max_dBFS)

        nonsilent_ranges = detect_nonsilent(audio, min_silence_len=50, silence_thresh=-40)

        durations = []
        for i in range(len(nonsilent_ranges)):
            start, end = nonsilent_ranges[i]
            durations.append(("beep", end - start))
            if i + 1 < len(nonsilent_ranges):
                next_start = nonsilent_ranges[i + 1][0]
                durations.append(("silence", next_start - end))

        morse_code = ""
        for kind, duration in durations:
            if kind == "beep":
                if duration < 100:
                    morse_code += "."
                else:
                    morse_code += "-"
            elif kind == "silence":
                if 150 <= duration < 300:
                    morse_code += " "
                elif duration >= 300:
                    morse_code += "   "

        decoded_text = morse_to_text(morse_code)
        return morse_code, decoded_text
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def main():
    # Display header and credits
    print(HEADER)
    print(CREDITS)
    print("\n" + "="*50 + "\n")

    # Get user input
    file_path = input("Masukkan path file audio Morse (.wav): ").strip()

    # Process file
    morse, result = decode_morse_wav(file_path)

    # Display results
    if morse and result:
        print("\nKode Morse:", morse)
        print("Hasil Decode:", result)
    else:
        print("Gagal memproses file. Pastikan path benar dan format file adalah WAV.")

if __name__ == "__main__":
    main()
