import os

INPUT_DIR = "input"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "all_files.md")

EXTENSIONS = (".ts", ".tsx", ".css", ".prisma")

EXTENSION_LANGUAGE_MAP = {
    ".ts": "typescript",
    ".tsx": "typescript",
    ".css": "css",
    ".prisma": "prisma",
}

def files_merger():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    all_files = []
    for root, _, files in os.walk(INPUT_DIR):
        for file_name in sorted(files):
            if file_name.endswith(EXTENSIONS):
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, INPUT_DIR)
                all_files.append((relative_path, file_path))

    all_files.sort(key=lambda x: x[0])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        output.write("# Arquivos do Projeto\n\n")
        output.write(f"Total de arquivos encontrados: **{len(all_files)}**\n\n")
        output.write("---\n\n")

        for relative_path, file_path in all_files:
            ext = os.path.splitext(file_path)[1]
            language = EXTENSION_LANGUAGE_MAP.get(ext, "")

            depth = relative_path.count(os.sep)
            heading_level = "#" * min(depth + 2, 6)

            output.write(f"{heading_level} `{relative_path}`\n\n")

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            output.write(f"```{language}\n")
            output.write(content)
            if not content.endswith("\n"):
                output.write("\n")
            output.write("```\n\n")
            output.write("---\n\n")

    print(f"Arquivos processados com sucesso! Total: {len(all_files)}")

if __name__ == "__main__":
    files_merger()