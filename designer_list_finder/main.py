from urllib.parse import urlparse
from pathlib import Path

def extract_websites(file_path):
    websites = set()
    with open(file_path, 'r') as f:
        for line in f:
            parsed_uri = urlparse(line.strip())
            netloc = parsed_uri.netloc
            if netloc:
                # Remove 'www.' if it exists
                netloc = netloc.lstrip('www.')
                websites.add(netloc)
    return websites

if __name__ == '__main__':
    all_websites = set()

    for history_file in ['firefox_history.txt', 'chrome_history.txt', 'safari_history.txt']:
        if Path(history_file).is_file():
            websites = extract_websites(history_file)
            all_websites.update(websites)

    with open('visited_websites.txt', 'w') as f:
        for website in sorted(all_websites):
            f.write(website + '\n')
