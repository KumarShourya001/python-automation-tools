# Python Automation Tools ⚙️

This repository contains a collection of small Python automation and utility scripts designed to simplify everyday tasks and demonstrate practical programming use cases.

## 🚀 Tools Included

### 1. Fun Fact Generator 🎲
- Generates random fun facts
- Demonstrates randomness and basic data handling

### 2. PDF Audio Converter 📄🔊
- Converts PDF text into audio
- Demonstrates file handling and text-to-speech

### 3. Web Scraper 🌐
- Extracts data from websites
- Demonstrates web scraping using Python

### 4. Voice Recorder 🎤
- Records audio using microphone input
- Demonstrates audio processing

---

## 🛠️ Tech Stack
- Python
- Libraries may include:
  - requests / BeautifulSoup
  - pyttsx3 / gTTS
  - sounddevice / pyaudio

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-automation-tools.git

## Dependencies

- Install Python dependencies:

```bash
pip install -r requirements.txt
```

- After installing `nltk`, download required NLTK data (examples below):

```bash
python -m nltk.downloader punkt stopwords wordnet averaged_perceptron_tagger
```

These packages enable better sentence tokenization, stopword removal, and lemmatization which improve text cleaning, summarization, and TTS quality.

---

Updated to include `nltk` and PDF/OCR helper packages. For OCR use, install Tesseract separately and ensure it's on your PATH.
