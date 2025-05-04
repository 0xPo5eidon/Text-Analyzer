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

## 📝 Examples

### Analyze a file:
```bash
python main.py document.txt
```

### Analyze from stdin:
```bash
echo "This is a sample text." | python main.py
```

### Analyze a string directly:
```bash
python main.py -s "The quick brown fox jumps over the lazy dog."
```

### Get JSON output:
```bash
python main.py article.txt -f json
```

### Get CSV output:
```bash
python main.py report.txt -f csv
```

### Pipe file content:
```bash
cat essay.txt | python main.py -f standard
```

## 📚 Readability Interpretation

The Flesch Reading Ease score indicates the reading level of the text:

| Score Range | Reading Ease       | Education Level    |
|-------------|-------------------|--------------------|
| 90-100      | Very Easy         | 5th grade          |
| 80-89       | Easy              | 6th grade          |
| 70-79       | Fairly Easy       | 7th grade          |
| 60-69       | Standard          | 8th-9th grade      |
| 50-59       | Fairly Difficult  | 10th-12th grade    |
| 30-49       | Difficult         | College level      |
| 0-29        | Very Difficult    | Graduate level     |

## 💡 Use Cases

1. **Content Writing**: Check readability of articles and blog posts
2. **Academic Writing**: Analyze complexity of research papers
3. **SEO Optimization**: Ensure content meets target reading level
4. **Editing**: Identify overused words and complex sentences
5. **Language Learning**: Track vocabulary diversity
6. **Writing Analysis**: Compare multiple documents statistically

## 💡 Tips

- Use the JSON output for integration with other tools
- Combine with other Unix tools using pipes
- For large files, consider text preprocessing first
- The readability score works best with complete sentences
- Word frequency helps identify content themes
- Lexical diversity indicates vocabulary richness

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
