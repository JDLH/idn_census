#!/bin/env python3
"""count_domains.py -- count the number of domains under a given top-level domain

Copyright 2025 by Jim DeLaHunt, CC0 licence, dedicated to the public domain.
Uses the Common Crawl database.

Based on cc_fetch_page.py <https://gist.githubusercontent.com/thunderpoot/58a748565d2e5b2582520fa535821908/raw/1082718722bbc7dc039276d35eebd4c655ecf96d/cc_fetch_page.py">
The author of that file retains copyright over the parts they wrote.
"""

import json

# For parsing URLs:
from urllib.parse import quote_plus

import idna
import requests

# The URL of the Common Crawl Index server
SERVER = "http://index.commoncrawl.org/"

# The Common Crawl index you want to query
INDEX_NAME = "CC-MAIN-2023-50"  # Replace with the latest index name
# current: "CC-MAIN-2025-05". Older: "CC-MAIN-2023-50" is "November/December 2023 Index"

# The URL you want to look up in the Common Crawl index
target_domain = "भारत"  # Replace with your target URL, e.g. "भारत", "ไทย"
# See also https://en.wikipedia.org/wiki/Country_code_top-level_domain

# It’s advisable to use a descriptive User-Agent string when developing your own applications.
# This practice aligns with the conventions outlined in RFC 7231. Let's use this simple one:
myagent = "count_domains/1.0 (Tutorial data retrieval script; from+commoncrawl@jdlh.com)"


# Function to search the Common Crawl Index
def search_cc_index(domain):
    encoded_url = "*." + quote_plus(domain)
    index_url = f"{SERVER}{INDEX_NAME}-index?" + "&".join(
        [
            f"url={encoded_url}",
            "fields=urlkey,domain",
            "output=json",
            "pageSize=500",
            "output=json",
        ]
    )
    response = requests.get(index_url, headers={"user-agent": myagent})
    if response.status_code == 200:
        records = response.text.strip().split("\n")
        return [json.loads(record) for record in records]
    else:
        return None


def print_domain_counts(labels_tree):
    """print the count of the supplied domains, indented.

    Calls a companion recursive function to do the actual work.
    """
    return print_domain_counts_recursive(labels_tree, [])


def print_domain_counts_recursive(labels_tree, parents):
    """print the count of the supplied domains, indented."""
    indentation = " " * len(parents)
    cumulative = 0
    for label, sublabels in labels_tree.items():
        parents_label = parents + [label]
        domain_name = ".".join(reversed(parents_label))
        n_subdomains = 1
        if len(sublabels):
            print(
                f"{indentation}{domain_name}, which has {len(sublabels)} direct subdomains:"
            )
            n_subdomains += print_domain_counts_recursive(
                sublabels, parents_label
            )
            print(
                f"{indentation}{domain_name} has {n_subdomains} total subdomains."
            )
        else:
            print(f"{indentation}{domain_name}")
        cumulative += n_subdomains
    return cumulative


# Search the index for the target URL
records = search_cc_index(target_domain)
if records:
    print(f"Found {len(records)} URLs for {target_domain}.")

    # catalogue the unique subdomains for target_domain, and number of
    # sub-sub-domains, and so on recursively.
    labels_tree = {}
    for record in records:
        labels = ((record["urlkey"].split(")")[0]).split(":")[0]).split(",")
        parent = labels_tree
        for a_label in labels:
            u_label = idna.decode(a_label)
            parent = parent.setdefault(u_label, {})

    # print out the counts
    _ = print_domain_counts(labels_tree)
else:
    print(f"No records found for {target_domain}")
