import json
from collections import Counter
import re

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_news_text(rss_data):
    items = rss_data['rss']['channel']['items']
    texts = []
    for item in items:
        description = item.get('description', '')
        texts.append(description)
    return ' '.join(texts)

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
    filename = 'newsafr.json'  # название файла
    json_data = load_json(filename)
    news_text = extract_news_text(json_data)
    cleaned_text = clean_text(news_text)
    top_words = get_top_frequent_words(cleaned_text)
    print("Топ 10 самых часто встречающихся слов длиннее 6 символов в descriptions:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()