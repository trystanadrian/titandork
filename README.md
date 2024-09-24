# Titandork - Google Dorking Automation Tool

Titandork is a powerful and easy-to-use tool designed for security researchers and penetration testers. It automates Google dorking to find sensitive information and vulnerabilities on websites using predefined Google search queries (dorks). With Titandork, you can quickly scan a target domain for potential exposures such as configuration files, admin login pages, backup files, and more.

## Features
- Perform Google dorking on any domain to find:
  - Exposed configuration files (`.env`, `.ini`, `.cfg`)
  - Exposed credentials (passwords, API keys)
  - Database dumps (`.sql`, `.db`)
  - Sensitive documents (`.xls`, `.csv`, `.pdf`)
  - Publicly accessible admin panels
  - Backup files and source code
  - Debug information and error logs
- Saves the results in a timestamped output file for easy reference.
- Color-coded terminal output for clear visual feedback (green for results, red for no results).
- Built-in delay to avoid Google CAPTCHA detection.

## Installation

### Installing Titandork

You can install Titandork by cloning the repository and using the installation script or by installing it as a `.deb` package.

#### 1. Install from GitHub (Source)
To install the tool directly from source:
```
git clone https://github.com/trystanadrian/titandork.git
```
```
cd titandork
```
```
sudo ./install.sh
```

#### 2. Install using .deb package 
To install the tools
```
sudo dpkg -i titandork.deb
```
Make sure you have the following dependencies installed:
* Python 3.x
* requests
* beautifulsoup4
You can install the dependencies using pip:
```
pip install -r requirements.txt
```

## Usage
Once installed, you can start using Titandork by typing the following command in your terminal:
```
titandork
```
The tool will prompt you to enter a target domain (e.g., vulnweb.com). It will then run a series of Google dorking queries and display the results in the terminal.

### Example
![image](https://github.com/user-attachments/assets/946bb60c-da94-40b5-bd53-e4b3bdff2c33)


### Output
Titandork will generate an output file for each scan. The output file will be stored in the same directory where the tool is run and named as dorking_results_YYYYMMDD.txt.

for example: **dorking_results_20240924.txt**

This file will contain all the results from the dorking process, making it easy to review the findings later.

### Updating Titandork
You can update the tool by pulling the latest version from the GitHub repository:
```
git pull origin main
```

## Contributing
Contributions are welcome! If you'd like to contribute to the development of Titandork, you can:
Fork this repository.
- Create a new branch (git checkout -b feature/my-feature).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/my-feature).
- Open a Pull Request.
Feel free to report any issues or suggest new features by opening an issue.

## Disclaimer
Titandork is intended for legal, ethical, and educational purposes only. Use of this tool is your responsibility. Make sure you have permission from the owner of the target domain before running any scans.

Happy dorking! 😎


### Key Features:
- **Simple Installation Instructions**: This makes it easy for newbies to install the tool.
- **Basic Usage Examples**: Clear examples of how to use the tool with sample output.
- **Contribution Guidelines**: Encourages new developers to contribute to the tool.
- **Disclaimer**: Legal disclaimer to ensure ethical usage.

Let me know if you’d like any further customization!







