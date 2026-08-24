#!/usr/bin/env python3
import sys
import subprocess
from datetime import datetime

C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_BLUE = "\033[94m"
C_RESET = "\033[0m"

def run(cmd, capture=True):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=capture)
    if res.returncode != 0:
        if capture and res.stderr:
            print(f"{C_RED}❌ Error: {res.stderr.strip()}{C_RESET}")
        sys.exit(res.returncode)
    return res.stdout.strip() if capture else None

def main():
    # 1. Check if inside a git repository
    try:
        run("git rev-parse --is-inside-work-tree")
    except SystemExit:
        print(f"{C_RED}❌ Error: Current directory is not a git repository.{C_RESET}")
        sys.exit(1)

    # 2. Stage changes
    run("git add .")

    # 3. Check for sensitive files in staging
    staged_files = run("git diff --name-only --cached").splitlines()
    dangerous_patterns = [".env", "id_rsa", "credentials", "secret", ".pem"]
    warnings = [f for f in staged_files if any(p in f.lower() for p in dangerous_patterns)]

    if warnings:
        print(f"\n{C_RED}⚠️ WARNING! Potentially sensitive files staged:{C_RESET}")
        for w in warnings:
            print(f"   - {w}")
        confirm = input(f"{C_YELLOW}Push anyway? (y/N): {C_RESET}").strip().lower()
        if confirm != 'y':
            print(f"{C_RED}Aborted. Unstage files using: git restore --staged <file>{C_RESET}")
            sys.exit(1)

    # 4. Pull with autostash
    print(f"{C_BLUE}📥 Pulling changes (git pull --rebase --autostash)...{C_RESET}")
    run("git pull --rebase --autostash", capture=False)

    # 5. Check if there are changes to commit after pull
    if not run("git status --porcelain"):
        print(f"{C_GREEN}✨ Working tree clean, nothing to commit.{C_RESET}")
        return

    # 6. Build commit message
    if len(sys.argv) > 1:
        commit_msg = " ".join(sys.argv[1:])
    else:
        branch = run("git branch --show-current") or "detached"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_msg = f"auto({branch}): update {timestamp}"

    # 7. Commit & Push
    print(f"{C_YELLOW}📝 Committing: '{commit_msg}'...{C_RESET}")
    run(f'git commit -m "{commit_msg}"')

    print(f"{C_BLUE}🚀 Pushing to remote (git push)...{C_RESET}")
    run("git push", capture=False)

    print(f"{C_GREEN}🎉 Done! All changes are up to date.{C_RESET}")

if __name__ == "__main__":
    main()
