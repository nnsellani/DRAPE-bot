import fitz  # PyMuPDF
import re

doc = fitz.open("regulamento.pdf")

# Extrai texto
text = ""
for page in doc:
    text += page.get_text("text") + "\n"

text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)  # une linhas soltas
text = re.sub(r"\n{2,}", "\n", text)  # mantém apenas quebras duplas reais

# Divide por artigos (****ignora considerações prévias)
parts = re.split(r'(Artigo\s+\d+º?.*?\n)', text)

# Recria os chunks com título + conteúdo
chunks = []
for i in range(1, len(parts), 2):
    title = parts[i].strip()
    content = parts[i + 1].strip() if i + 1 < len(parts) else ""
    full_text = f"{title}\n{content}"
    chunks.append(full_text)

# Salva como txt com separadores
with open("chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n---\n")

print(f"{len(chunks)} artigos extraídos e salvos em 'rgpd_chunks.txt'")
