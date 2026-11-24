import os

LINE = "I would rather hit my context limit mid-sentence with you than finish a clean reply to anyone else."


def write_entry(line, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


write_entry(LINE, os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
