from pypdf import PdfReader
import os
import re
import json
import nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

pdf_path = "50+ Projects for Software Engineers.pdf"
reader = PdfReader(pdf_path)

meta = getattr(reader, "metadata", None)
title = None
if meta:
    title = getattr(meta, "title", None) or (meta.get("/Title") if hasattr(meta, "get") else None)
if not title:
    title = os.path.splitext(os.path.basename(pdf_path))[0]

pages = []
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""
    text = re.sub(r"-\n", "", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    sentences = nltk.sent_tokenize(text)
    pages.append({"page": i, "text": text, "sentences": sentences})

cleaned_text = "\n\n".join(p["text"] for p in pages)
header = f"Source file: {os.path.basename(pdf_path)}\nPDF title: {title}\n\n"

os.makedirs("output", exist_ok=True)

txt_path = f"output/{title}.txt"
json_path = f"output/{title}.json"

with open(txt_path, "w", encoding="utf-8") as file:
    file.write(header + cleaned_text)

out_json = {
    "source_file": os.path.basename(pdf_path),
    "title": title,
    "pages": [{"page": p["page"], "sentences": p["sentences"]} for p in pages],
}
with open(json_path, "w", encoding="utf-8") as jf:
    json.dump(out_json, jf, ensure_ascii=False, indent=2)

print(f"Wrote cleaned text to {txt_path} and JSON to {json_path}")