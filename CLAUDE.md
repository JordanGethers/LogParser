# CLAUDE.md — Project Memory File
> This file is automatically read by Claude Code at the start of every session.
> Update it as your project evolves to keep Claude informed.

---

## 📁 Project Overview

- **Project Type:** Python learning project
- **Goal:** Build a log file parser
- **Skill Level:** Learning / beginner-friendly explanations preferred

---

## 🐍 Language & Environment

- **Language:** Python
- **OS:** Windows with WSL2
- **Editor:** Visual Studio Code

---

## 📌 Session Notes
> Add important notes, decisions, and progress here after each session.

### Session — 2026-03-19

#### Accomplished
- Set up `log_parser.py` with `os.path.dirname(__file__)` to reliably find the log file regardless of working directory
- Used `f.readlines()` to read the log into a list of lines (one line per element)
- Added a `re.search(r"Failed password", line)` loop that finds and prints failed SSH login lines from `logFiles/sample_auth.log`

#### Concepts Covered
- `re.search()` — searches for a pattern anywhere in a string, returns a match object or None
- `re.compile()` and named groups `(?P<name>...)` — introduced but deferred as too complex for now
- `group(1)` — how to extract the first captured group from a regex match
- `f.read()` vs `f.readlines()` — difference between reading all text at once vs a list of lines
- `os.path.dirname(__file__)` and `os.path.join()` — finding files relative to the script, not the terminal

#### Decisions Made
- Keep regex simple for now — use separate `re.search()` calls for "Failed password" and IP extraction rather than one complex pattern
- Learner-friendly explanations preferred over concise/advanced code

#### Next Steps (Later TODOs)
- [ ] Extract IP from each matched line using `re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)`
- [ ] Count failures per IP using a dict
- [ ] Sort IPs by fail count descending with `sorted(..., reverse=True)`
- [ ] Output results to CSV with a timestamp column using the `csv` module

### Known Issues / TODOs
- `re.search(r"")` placeholder on line 21 needs to be completed with the actual pattern

---

## 🧠 How I Like to Work With Claude

- Explain concepts clearly — this is a learning project
- Show me what the code does, not just how to write it
- Suggest best practices and explain *why* they are best practices
- If I make a mistake, point it out kindly and explain the correct approach

---

## 📂 Project Structure
> Update this as your project grows

```
LogParser/
├── CLAUDE.md              ← You are here
├── log_parser.py          ← Main script
├── logFiles/
│   ├── sample_auth.log    ← Sample SSH auth log for testing
│   └── sample_syslog.log
└── README.md
```

---

## 🔧 Coding Preferences

- Use clear, readable variable names
- Add comments to explain non-obvious logic
- Prefer simple solutions over clever ones (learning project)
- Use f-strings for string formatting
- Follow PEP 8 style guidelines

---

## 📝 How to Update This File

After each session, add notes under **Session Notes** above:
- What was accomplished
- Any decisions made
- Bugs found or fixed
- Next steps planned
