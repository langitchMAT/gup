# gup (Git Update & Push)

gup is a lightweight Python CLI utility designed to automate routine Git workflows (add, pull, commit, push) into a single command with built-in safety checks.

---

## Features

- Security Check: Scans staged files for sensitive data (.env, keys) before committing.
- Auto-Sync: Runs git pull --rebase --autostash automatically.
- Smart Commit Messages: Generates an automatic commit message with branch name and timestamp if omitted.
- Zero Dependencies: Powered entirely by Python 3 standard libraries.

---

## Installation

1. Clone the repository:
   git clone [https://github.com/langitchMAT/gup.git](https://github.com/langitchMAT/gup.git)
   cd gup

2. Make executable and move to ~/.local/bin:
   chmod +x gup.py
   mv gup.py ~/.local/bin/gup

(Ensure ~/.local/bin is in your PATH).

---

## Usage

Run inside any Git repository:

# Automatic commit with timestamp:
gup

# Custom commit message:
gup fix user authorization bug

---

## License

MIT (see LICENSE file)
