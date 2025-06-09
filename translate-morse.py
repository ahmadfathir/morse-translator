from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# Fungsi untuk menerjemahkan kode Morse ke teks biasa
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

# Fungsi utama untuk memproses file WAV menjadi teks
def decode_morse_wav(file_path):
    # Load dan normalisasi audio
    audio = AudioSegment.from_wav(file_path)
    audio = audio.set_channels(1)
    audio = audio.apply_gain(-audio.max_dBFS)

    # Deteksi bagian tidak diam (bunyi)
    nonsilent_ranges = detect_nonsilent(audio, min_silence_len=50, silence_thresh=-40)

    # Ambil durasi beep dan jeda
    durations = []
    for i in range(len(nonsilent_ranges)):
        start, end = nonsilent_ranges[i]
        durations.append(("beep", end - start))
        if i + 1 < len(nonsilent_ranges):
            next_start = nonsilent_ranges[i + 1][0]
            durations.append(("silence", next_start - end))

    # Konversi ke simbol Morse
    morse_code = ""
    for kind, duration in durations:
        if kind == "beep":
            if duration < 100:
                morse_code += "."
            else:
                morse_code += "-"
        elif kind == "silence":
            if 150 <= duration < 300:
                morse_code += " "      # antar huruf
            elif duration >= 300:
                morse_code += "   "    # antar kata

    # Terjemahkan ke teks biasa
    decoded_text = morse_to_text(morse_code)
    return morse_code, decoded_text

# Contoh penggunaan
file_path = "morse.wav"  # Ganti dengan path file yang sesuai
morse, result = decode_morse_wav(file_path)
print("Kode Morse:", morse)
print("Hasil Decode:", result)
