from pypdf import PdfReader
import json

# Read LinkedIn profile - prefer the trimmed text version, it costs about half the
# tokens of the raw PDF extraction and every request resends it
try:
    with open("./data/linkedin.txt", "r", encoding="utf-8") as f:
        linkedin = f.read()
except FileNotFoundError:
    try:
        reader = PdfReader("./data/linkedin.pdf")
        linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                linkedin += text
    except FileNotFoundError:
        linkedin = "LinkedIn profile not available"

# Read other data files
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)