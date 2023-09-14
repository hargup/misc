from names_dataset import NameDataset
import re
import os

all_names_file = "all_names.txt"

if not os.path.exists(all_names_file):
    m = NameDataset()

    # Get top 1000 names for males and females in the US
    top_males = [name.lower() for name in m.get_top_names(country_alpha2='US', n=1000)['US']['M']]
    top_females = [name.lower() for name in m.get_top_names(country_alpha2='US', n=1000)['US']['F']]

    # Combine male and female names into one list and convert it to a set
    all_names = set(top_males + top_females)

    # Write all_names to a file
    with open(all_names_file, 'w') as f:
        for name in all_names:
            f.write(name + '\n')
else:
    # Load all_names from a file
    with open(all_names_file, 'r') as f:
        all_names = set(line.strip() for line in f)

def is_likely_portfolio(domain):
    domain = domain.lower().split('.')[0]
    # Generate all possible substrings of domain
    substrings = [domain[i: j] for i in range(len(domain)) for j in range(i + 1, len(domain) + 1)]
    for substring in substrings:
        if substring in all_names:
            return True
    return False

# Sample usage
with open('output_file.txt', 'r') as f:
    domains_1 = set(line.strip() for line in f)

with open('output_file_2.txt', 'r') as f:
    domains_2 = set(line.strip() for line in f)

domains = domains_2 - domains_1

# domains = []
# domains.extend(['johnsmith.com', 'amazon.com', 'sarahc.dev'])
portfolios = [domain for domain in domains if is_likely_portfolio(domain)]

with open('portfolios.txt', 'w') as f:
    for portfolio in portfolios:
        f.write(portfolio + '\n')
