# Author: Leif R Bruce ~/00xNetrunner
# Date: May 07, 2024
# Description: Waybackurls - Retrieve URLs from the Wayback Machine for multiple hosts

import requests
import sys
import argparse
import concurrent.futures
import time
import os
from datetime import datetime

def waybackurls(host, with_subs):
    if with_subs:
        url = f'http://web.archive.org/cdx/search/cdx?url=*.{host}/*&output=json&fl=timestamp,original&collapse=urlkey'
    else:
        url = f'http://web.archive.org/cdx/search/cdx?url={host}/*&output=json&fl=timestamp,original&collapse=urlkey'
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        results = r.json()
        return results[1:]
    except requests.exceptions.RequestException as e:
        print(f'Error occurred while making the request: {e}')
        return []

def save_results(urls, filename):
    # Create the directory if it doesn't exist
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)

    with open(filename, 'w') as f:
        for url in urls:
            timestamp, original_url = url
            date = datetime.strptime(timestamp, '%Y%m%d%H%M%S').strftime('%Y-%m-%dT%H:%M:%SZ')
            f.write(f'{date} - {original_url}\n')
    print(f'[*] Saved results to {filename}')

def process_host(host, with_subs, output_dir):
    start_time = time.time()
    urls = waybackurls(host, with_subs)
    if urls:
        filename = f'{output_dir}/{host}-waybackurls.txt'
        save_results(urls, filename)
    else:
        print(f'[-] No URLs found for {host}')
    end_time = time.time()
    print(f'[*] Processed {host} in {end_time - start_time:.2f} seconds')

def main():
    parser = argparse.ArgumentParser(description='Retrieve URLs from the Wayback Machine')
    parser.add_argument('hosts', nargs='+', help='One or more hosts to retrieve URLs for')
    parser.add_argument('-s', '--subdomains', action='store_true', help='Include subdomains in the search')
    parser.add_argument('-o', '--output', default='results', help='Output directory for the text files (default: results)')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of concurrent threads (default: 5)')
    args = parser.parse_args()

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for host in args.hosts:
            futures.append(executor.submit(process_host, host, args.subdomains, args.output))
        
        for future in concurrent.futures.as_completed(futures):
            future.result()

    end_time = time.time()
    print(f'\n[*] Total execution time: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    main()
