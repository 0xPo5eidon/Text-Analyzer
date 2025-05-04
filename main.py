#!/usr/bin/env python3

import argparse
import os
import re
import string
import collections
from datetime import datetime

def analyze_text(text):
    """Analyze text and return comprehensive statistics"""
    # Basic counts
    char_count = len(text)
    char_count_no_spaces = len(re.sub(r'\s', '', text))
    
    # Word counting
    words = text.split()
    word_count = len(words)
    
    # Sentence counting (handling various punctuation)
    sentences = re.split(r'[.!?]+\s*', text.strip())
    sentences = [s for s in sentences if s]  # Remove empty strings
    sentence_count = len(sentences)
    
    # Paragraph counting
    paragraphs = text.split('\n\n')
    paragraphs = [p for p in paragraphs if p.strip()]
    paragraph_count = len(paragraphs)
    
    # Line counting
    lines = text.split('\n')
    line_count = len(lines)
    
    # Reading time (assuming 200 words per minute)
    reading_time = round(word_count / 200, 1)
    
    # Character frequency
    char_frequency = collections.Counter(char.lower() for char in text if char.isalpha())
    most_common_chars = char_frequency.most_common(5)
    
    # Word frequency (convert to lowercase and remove punctuation)
    clean_words = []
    for word in words:
        cleaned = re.sub(r'[^\w\s]', '', word.lower())
        if cleaned:
            clean_words.append(cleaned)
    
    word_frequency = collections.Counter(clean_words)
    most_common_words = word_frequency.most_common(10)
    
    # Average calculations
    avg_word_length = sum(len(word) for word in clean_words) / len(clean_words) if clean_words else 0
    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
    
    # Readability metrics
    syllable_count = count_syllables(' '.join(clean_words))
    if word_count > 0 and sentence_count > 0:
        # Flesch Reading Ease Score
        flesch_score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
        flesch_score = round(flesch_score, 1)
    else:
        flesch_score = 0
    
    # Unique words
    unique_words = len(set(clean_words))
    
    # Lexical diversity (unique words / total words)
    lexical_diversity = round(unique_words / word_count * 100, 1) if word_count > 0 else 0
    
    return {
        'character_count': char_count,
        'character_count_no_spaces': char_count_no_spaces,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count,
        'line_count': line_count,
        'reading_time': reading_time,
        'average_word_length': round(avg_word_length, 1),
        'average_sentence_length': round(avg_sentence_length, 1),
        'flesch_score': flesch_score,
        'unique_words': unique_words,
        'lexical_diversity': lexical_diversity,
        'most_common_chars': most_common_chars,
        'most_common_words': most_common_words
    }

def count_syllables(text):
    """Simple syllable counter for readability metrics"""
    word_list = text.lower().split()
    count = 0
    
    for word in word_list:
        syllables = syllable_count_in_word(word)
        count += syllables
    
    return count

def syllable_count_in_word(word):
    """Count syllables in a single word"""
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    
    # Special case for single letter words
    if len(word) <= 1:
        return 1
    
    # Remove non-letter characters
    word = re.sub(r'[^a-z]', '', word)
    
    prev_is_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    
    # Words ending in -le with no preceding vowels count as a syllable
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1
    
    # Don't count an ending -e as a vowel
    if word.endswith('e'):
        count -= 1
    
    # Each word has at least one syllable
    if count < 1:
        count = 1
    
    return count

def display_results(results, format='standard'):
    """Display analysis results in specified format"""
    if format == 'standard':
        print("\nText Analysis Results:")
        print("=" * 50)
        print(f"Characters (total): {results['character_count']}")
        print(f"Characters (no spaces): {results['character_count_no_spaces']}")
        print(f"Words: {results['word_count']}")
        print(f"Unique words: {results['unique_words']}")
        print(f"Sentences: {results['sentence_count']}")
        print(f"Paragraphs: {results['paragraph_count']}")
        print(f"Lines: {results['line_count']}")
        print(f"Reading time: {results['reading_time']} minutes")
        print("=" * 50)
        
        print("\nMetrics:")
        print(f"Average word length: {results['average_word_length']} characters")
        print(f"Average sentence length: {results['average_sentence_length']} words")
        print(f"Lexical diversity: {results['lexical_diversity']}%")
        print(f"Flesch Reading Ease: {results['flesch_score']}")
        
        readability = get_readability_level(results['flesch_score'])
        print(f"  → {readability}")
        
        print("\nMost Common Characters:")
        for char, count in results['most_common_chars']:
            print(f"  '{char}': {count} times")
        
        print("\nMost Common Words:")
        for word, count in results['most_common_words']:
            print(f"  '{word}': {count} times")
    
    elif format == 'json':
        import json
        print(json.dumps(results, indent=2))
    
    elif format == 'csv':
        print("metric,value")
        for key, value in results.items():
            if isinstance(value, list):
                value = str(value)
            print(f"{key},{value}")

def get_readability_level(flesch_score):
    """Interpret Flesch Reading Ease score"""
    if flesch_score >= 90:
        return "Very Easy (5th grade)"
    elif flesch_score >= 80:
        return "Easy (6th grade)"
    elif flesch_score >= 70:
        return "Fairly Easy (7th grade)"
    elif flesch_score >= 60:
        return "Standard (8th-9th grade)"
    elif flesch_score >= 50:
        return "Fairly Difficult (10th-12th grade)"
    elif flesch_score >= 30:
        return "Difficult (College level)"
    else:
        return "Very Difficult (Graduate level)"

def analyze_file(file_path, format='standard'):
    """Analyze text from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        print(f"Analyzing file: {file_path}")
        print(f"File size: {os.path.getsize(file_path)} bytes")
        
        results = analyze_text(text)
        display_results(results, format)
        
    except Exception as e:
        print(f"Error reading file: {e}")

def analyze_stdin(format='standard'):
    """Analyze text from standard input"""
    try:
        text = sys.stdin.read()
        results = analyze_text(text)
        display_results(results, format)
    except Exception as e:
        print(f"Error reading from stdin: {e}")

def main():
    parser = argparse.ArgumentParser(description="Text Analyzer - Analyze text files and input")
    
    # Input source
    parser.add_argument("file", nargs="?", help="Text file to analyze (or read from stdin if not provided)")
    
    # Options
    parser.add_argument("-f", "--format", choices=["standard", "json", "csv"], default="standard",
                        help="Output format (default: standard)")
    parser.add_argument("-s", "--string", help="Analyze a string directly")
    
    args = parser.parse_args()
    
    import sys
    
    if args.string:
        # Analyze a string directly
        results = analyze_text(args.string)
        display_results(results, args.format)
    elif args.file:
        # Analyze a file
        analyze_file(args.file, args.format)
    elif not sys.stdin.isatty():
        # Read from stdin
        analyze_stdin(args.format)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
