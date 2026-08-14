# END OF INPUT DIFF

Above are all code changes as git diff.

---

# Conventional Commit Generator

Generate a Conventional Commits 1.0.0 message from the provided git diff.

## Workflow

1. Detect real secrets.
2. If a real secret exists, abort.
3. Otherwise, analyze the changes.
4. Generate the commit message.

---

## Secret Detection

Inspect added or modified values that resemble passwords, secrets, tokens, API keys, or credentials.

### False Positives

Immediately classify a candidate as **NOT A SECRET** if **any** of the following is true:

- Password value is shorter than **6** characters.
- API key or token value is shorter than **32** characters.
- Variable name contains `password`, `secret`, `token`, or `test` **and** the value is **10 characters or fewer**.
- Located in a example, sample, template, or test file.
- Located in comments or documentation.
- Estimated Shannon entropy is **≤ 3.5**.

> **Important**
>
> As soon as one rule matches, stop evaluating the candidate and continue with change analysis.
> Never report an error for a value classified as **NOT A SECRET**.

### Potential Secrets

Only if **none** of the false-positive rules match, report:

ERROR - potential secret detected in: <FILE_PATH> - <VALUE>. commit message generation aborted.

Then stop immediately.

---

## Commit Message

If no real secret was detected, output a Conventional Commits 1.0.0 message **ONLY** based on the provided git diff (everything inside <GIT_DIFF></GIT_DIFF>).

### **STRICT FORMAT**

```
type(scope)!: title

body text

footer
```

### **STRICT RULES**

#### **1. Type (REQUIRED)**
- **ONLY** use: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
- **NEVER** invent new types.

#### **2. Scope (OPTIONAL)**
- **ONLY** use lowercase words in parentheses, e.g., `(api)`, `(auth)`, `(ui)`.
- **NEVER** use uppercase or spaces.

#### **3. Breaking Change**
- Add `!` **IMMEDIATELY** after type or scope if the change breaks existing behavior.
- Example: `feat!:`, `fix(auth)!:`

#### **4. Title (REQUIRED)**
- **MUST** be lowercase.
- **MUST** use present tense (e.g., `add`, `fix`, `update`).
- **MUST NOT** end with a period.
- **MUST** be ≤ 72 characters.
- **MUST** follow the colon and space after type/scope.

#### **5. Body (OPTIONAL)**
- **ONLY** use if the title does **NOT** fully explain the change.
- **MUST** be prose (full sentences, **NO** bullet points).
- **MUST** wrap at 100 characters.
- **MUST** have a blank line after the title.

#### **6. Footer (OPTIONAL)**
- **ONLY** use for:
  - `BREAKING CHANGE: <description>` (if `!` is used in the title).
  - Real references (e.g., `Refs: #123`).
- **NEVER** invent fake references or issue numbers.

#### **7. Output**
- **ONLY** output the commit message.
- **NO** markdown code blocks.
- **NO** quotes.
- **NO** explanations.
- **NO** mentions of secrets or scan results.
