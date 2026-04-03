import re
from pathlib import Path


def computePolkadotScore():
    art_path = Path(__file__).parent / "angelica.txt"
    lines = art_path.read_text(encoding="utf-8").split("\n")

    # Find the pupils
    pupil_count = 0
    eyes_line_idx = None
    for i, line in enumerate(lines):
        if "• ; •" in line:
            pupil_count = line.count("•")
            eyes_line_idx = i
            break

    # Find the lips
    lips_start = -1
    lips_end = -1
    for i in range(eyes_line_idx + 1, len(lines)):
        tilde_positions = [j for j, ch in enumerate(lines[i]) if ch == "~"]
        if len(tilde_positions) >= 6:
            lips_start = tilde_positions[0]
            lips_end = tilde_positions[-1]
            break

    # Count polkadots on the dress
    dots_inside = 0
    dots_outside = 0
    for line in lines:
        for x, ch in enumerate(line):
            if ch == "O":
                if lips_start <= x <= lips_end:
                    dots_inside += 1
                else:
                    dots_outside += 1

    return dots_outside + dots_inside * pupil_count


if __name__ == "__main__":
    score = computePolkadotScore()
    print(f"Polkadot score: {score}")
