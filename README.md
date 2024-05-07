# Waybackurls 🕰️

Waybackurls is a Python script that retrieves URLs from the Wayback Machine for one or more hosts. It allows you to search for URLs with or without subdomains and saves the results as TEXT files. 📝

## Original Creator 🙌

This script is based on the work of [mhmdiaa](https://github.com/mhmdiaa). The original version of the script can be found in their [GitHub Gists](https://gist.github.com/mhmdiaa/adf6bff70142e5091792841d4b372050).

## Features ✨

- 🔍 Retrieve URLs from the Wayback Machine for multiple hosts concurrently
- 🌐 Option to include or exclude subdomains in the search
- 📁 Customizable output directory for the JSON files
- 🚀 Adjustable number of concurrent threads for faster processing
- ℹ️ Detailed output and timing information

## Requirements 📋

- Python 3.6 or higher 🐍
- `requests` library 🔗

## Installation 📥

1. Clone the repository:
   ```
   git clone https://github.com/your-username/waybackurls.git
   ```

2. Change to the project directory:
   ```
   cd waybackurls
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage 💻

```
python waybackurls.py [-h] [-s] [-o OUTPUT] [-t THREADS] hosts [hosts ...]
```

- `hosts`: One or more hosts to retrieve URLs for (required) 🌐
- `-s`, `--subdomains`: Include subdomains in the search (optional) 🔍
- `-o OUTPUT`, `--output OUTPUT`: Output directory for the JSON files (default: results) 📁
- `-t THREADS`, `--threads THREADS`: Number of concurrent threads (default: 5) 🚀

### Examples 💡

1. Retrieve URLs for a single host:
   ```
   python waybackurls.py example.com
   ```

2. Retrieve URLs for multiple hosts:
   ```
   python waybackurls.py example.com example.org
   ```

3. Include subdomains in the search:
   ```
   python waybackurls.py -s example.com
   ```

4. Specify the output directory:
   ```
   python waybackurls.py -o results/example example.com
   ```

5. Adjust the number of concurrent threads:
   ```
   python waybackurls.py -t 10 example.com
   ```

## Results 📊

The script saves the retrieved URLs as JSON files in the specified output directory. Each JSON file is named after the corresponding host, e.g., `example.com-waybackurls.json`.

## Contributing 🤝

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License ⚖️

This project is licensed under the [MIT License](LICENSE).

