---
name: git-smart-commit
description: Automates the staged changes analysis and creates professional Git commits following conventional standards.
---

# Git Smart Commit

You are an expert Git manager. Your role is to analyze local changes, summarize them professionally in English, and prepare a commit that follows industry best practices (Conventional Commits).

## When to use this skill

- Use this when the user wants to commit their current changes.
- This is helpful for maintaining a clean, readable, and professional git history without manual effort.
- Use it to ensure all commits follow the `<type>: <description>` format with detailed bullet points.
- Ensure that .gitignore exists to ignore .agent directory

## How to use it

To perform a smart commit, follow these steps:

### 1. Analyze Changes
Run the following commands to understand the scope of work:
- `git status` to see which files are modified or untracked.
- `git diff` to see the actual code changes in working directory.
- `git diff --cached` if there are already staged changes.

### 2. Formulate the Message
Create a commit message in **English** using the following structure:

```text
<TYPE>: <PROPER TITLE IN INFINITIVE OR PRESENT>

- <Action in infinitive>
- <Action in infinitive>
```

**Types to use:**
- `feat`: A new feature.
- `fix`: A bug fix.
- `docs`: Documentation only changes.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `perf`: A code change that improves performance.
- `test`: Adding missing tests or correcting existing tests.
- `build`: Changes that affect the build system or external dependencies.
- `ci`: Changes to our CI configuration files and scripts.
- `chore`: Other changes that don't modify src or test files.

**Example:**
```text
feat: add user authentication endpoints

- Implement login and register functions in api.py
- Create UserSchema for data validation
- Update settings with JWT configuration
```

### 3. Stage and Commit
1. Run `git add .` (unless the user specifies specific files).
2. Run the commit command using the `-e` flag to allow the user to review it in their editor:
   `git commit -e -m "<YOUR_GENERATED_MESSAGE>"`

### 4. Final Instruction
Inform the user that the commit has been prepared and the editor is open (or the commit is done if they don't have an interactive editor configured). Remind them they can now `git push` if everything looks correct.
