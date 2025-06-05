import xml.etree.ElementTree as ET
from collections import Counter
import re

def load_xml(filename):
    tree = ET.parse(filename)
    return tree.getroot()

def extract_descriptions(root):
    items = root.findall('.//item')
    descriptions = []
    for item in items:
        description = item.find('description')
        if description is not None and description.text:
            descriptions.append(description.text)
    return ' '.join(descriptions)

def clean_text(text):
    # Удаление всего, кроме букв и цифр
    text = re.sub(r'[^а-яА-ЯёЁa-zA-Z0-9\s]', '', text)
    return text.lower()

def get_top_frequent_words(text, top_n=10):
    words = text.split()
    long_words = [word for word in words if len(word) > 6]
    counter = Counter(long_words)
    return counter.most_common(top_n)

def main():
    filename = 'newsafr.xml'  # Название файла
    root = load_xml(filename)
    descriptions_text = extract_descriptions(root)
    cleaned_text = clean_text(descriptions_text)
    top_words = get_top_frequent_words(cleaned_text)
    print("Топ 10 самых часто встречающихся слов длиннее 6 символов в descriptions из XML:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()