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

### Session — 2026-03-23

#### Accomplished
- Expanded the failure match regex to also capture `"authentication failure"` and `"invalid user"` in addition to `"Failed password"`
- Added `re.IGNORECASE` flag so matches work regardless of letter case
- Added a null check (`if ip_match:`) to prevent crash when a matched line has no IP address
- Added a second capture group to the IP regex (`rhost=(\d+\.\d+\.\d+\.\d+)`) to catch `pam_unix` style log lines
- Fixed IP extraction to use `ip_match.group(1) or ip_match.group(2)` so both IP formats are handled
- Replaced `re.search()` in the loop with `re.compile()` — pattern is now compiled once outside the loop as `FAILURE_PATTERN`

#### Concepts Covered
- `re.IGNORECASE` — flag that makes regex match regardless of uppercase/lowercase
- `|` in regex — means "or", matches any one of multiple alternatives
- Multiple capture groups — each set of `()` is a numbered group; `.group(1)`, `.group(2)` etc.
- Why only one group matches when using `|` — the other group returns `None`
- `value1 or value2` — Python returns the first truthy value; used to pick whichever group matched
- `re.compile()` vs `re.search()` in a loop — compile parses the pattern once; search re-parses on every call
- `ALL_CAPS` naming convention for compiled patterns — signals it's a constant

#### Decisions Made
- Compiled pattern named `FAILURE_PATTERN` defined above the file open block, separate from loop logic
- Old `re.search()` line preserved as a comment with explanation of why to avoid it in loops
- `group(1) or group(2)` chosen over more complex alternatives — readable and appropriate for this stage

#### Next Steps / TODOs
- [ ] Apply `re.compile()` to the IP regex as well (`IP_PATTERN`)
- [ ] Explore named groups `(?P<name>...)` as a cleaner alternative to numbered groups
- [ ] Consider logging lines that matched but had no IP (currently silently skipped)

### Known Issues / TODOs
- ~~`re.search(r"")` placeholder needs to be completed~~ — resolved

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
