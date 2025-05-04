# 📊 Text Analyzer

A command-line tool for analyzing text content, providing comprehensive statistics and readability metrics.

## ✨ Features

- 📝 Character, word, sentence, and paragraph counting
- 🔤 Most common characters and words
- 📚 Reading time estimation
- 📊 Readability metrics (Flesch Reading Ease score)
- 📈 Lexical diversity analysis
- 🔢 Average word and sentence length
- 📄 Multiple output formats (standard, JSON, CSV)
- 💾 Analyze files or text from stdin

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/text-analyzer.git
cd text-analyzer
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py [file] [options]
```

## ⚙️ Options

file: Text file to analyze (optional, reads from stdin if not provided)
- `-f, --format`: Output format (standard, json, csv)
- `-s, --string`: Analyze a string directly

