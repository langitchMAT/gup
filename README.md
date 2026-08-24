# 🚀 gup (Git Update & Push)

**gup** is a lightweight Python CLI utility designed to automate routine Git workflows (`add`, `pull`, `commit`, `push`) into a single command with built-in safety checks.

Eliminate the need to type repetitive multi-step Git commands for everyday updates.

---

## ✨ Features

- 🔒 **Leak Prevention:** Scans staged files for sensitive data (`.env`, `id_rsa`, `.pem`, etc.) before committing.
- 🔄 **Auto-Sync:** Runs `git pull --rebase --autostash` to fetch remote updates without creating merge commits or breaking unstaged changes.
- ⏱ **Smart Commit Messages:** Generates an automatic commit message with the branch name and timestamp if none is provided (e.g., `auto(main): update 2026-08-25 00:22`).
- ⚡️ **Zero Dependencies:** Powered entirely by Python 3 standard libraries.

---

## 📥 Installation

1. Clone the repository:

```bash
git clone [https://github.com/langitchMAT/gup.git](https://github.com/langitchMAT/gup.git)
cd gup
```

2. Make the script executable and move it to `~/.local/bin` as `gup`:

```bash
chmod +x gup.py
mv gup.py ~/.local/bin/gup
```

*(Ensure `~/.local/bin` is in your `PATH` environment variable).*

---

## 🚀 Usage

Run it inside any Git repository:

```bash
# Automatic commit with timestamp
gup

# Custom commit message
gup "commit message"
```

---

## 📄 License

[MIT](LICENSE)
