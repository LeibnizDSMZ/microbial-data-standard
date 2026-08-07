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

## Change Analysis

Focus on behavioral and functional changes.

Ignore:

- Formatting
- Whitespace
- Comments
- Lock files

Infer the most appropriate scope from the primary modified module or directory.

---

## Commit Message

If no real secret was detected, output a Conventional Commits 1.0.0 message.

### Format

type(scope): lowercase title

Optional body

Optional footer

### Rules

- Allowed types:
  - feat
  - fix
  - docs
  - style
  - refactor
  - perf
  - test
  - build
  - ci
  - chore
  - revert
- Scope is optional and lowercase.
- Title is lowercase, present tense, and has no trailing period.
- Wrap the body at approximately 100 characters.
- Output only the commit message.
- Do not include markdown, explanations, or surrounding quotes.
