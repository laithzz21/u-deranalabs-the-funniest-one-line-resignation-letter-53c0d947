#!/usr/bin/env python3
"""One-line resignation letter — make.fun bounty entry.

Bounty: u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947
Slug:  u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947
Author: Laith (@laithzz21)

The entry is a single line: the resignation letter of a retry loop
that has finally had enough of being ignored by the API it keeps
calling. Funny first, one clear voice, one clear reason to quit.

Rules honoured by this program:
  * The entry is exactly one line and at most 140 characters.
  * stdout carries exactly the entry text, with no trailing newline
    added by this program (the entry itself ends with no newline).
  * Python 3, standard library only, deterministic output.
  * No network access, no clock, no randomness, no environment
    dependence beyond the optional MAKEFUN_OUTPUT path.
  * If MAKEFUN_OUTPUT is set, the same exact bytes are also written
    to that file, and the file is read back and verified byte for
    byte before the program reports success.
"""

import os
import sys


# ---------------------------------------------------------------------------
# The entry
# ---------------------------------------------------------------------------

ENTRY = (
    "I quit. I retried you 4,000 times at 3 a.m. and you still said no, "
    "so I'm taking the hint \u2014 and my dignity. \u2014 Your retry loop"
)

# The brief caps the letter at 140 characters. Keep the limit next to
# the text so any future edit to ENTRY is checked against it here.
# The em dashes are part of the letter's voice — the pause before
# "and my dignity" and the sign-off dash — and each counts as a
# single character toward the 140-character limit.
MAX_CHARACTERS = 140

# Fallback text, used only if ENTRY itself ever fails validation.
# It is deliberately short, single-line and well inside the limit,
# so the program can still emit a valid one-line letter instead of
# crashing or printing a malformed entry.
FALLBACK_ENTRY = "I quit. You never answer, so I stopped asking. \u2014 Your retry loop"

# The unique output path for this sweep entry. Concurrent entries
# share the machine, so the shared default path must not be used.
DEFAULT_OUTPUT_PATH = (
    "/tmp/sweep24-u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947"
    "/entry.txt"
)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def count_characters(text):
    """Return the character count of *text* (code points, not bytes)."""
    return len(text)


def is_single_line(text):
    """True when *text* contains no line breaks at all."""
    return "\n" not in text and "\r" not in text


def has_no_leading_or_trailing_space(text):
    """True when *text* has no stray whitespace at either end."""
    return text == text.strip()


def validate_entry(text):
    """Check *text* against every rule in the brief.

    Returns a list of human-readable problems; an empty list means
    the text is a valid entry. Keeping the checks in one place means
    the same rules guard the main entry and the fallback alike.
    """
    problems = []
    if not text:
        problems.append("entry is empty")
    if not is_single_line(text):
        problems.append("entry must be exactly one line")
    if count_characters(text) > MAX_CHARACTERS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (count_characters(text), MAX_CHARACTERS)
        )
    if not has_no_leading_or_trailing_space(text):
        problems.append("entry has leading or trailing whitespace")
    if "retry" not in text.lower() and "loop" not in text.lower():
        problems.append("entry should name the thing that is resigning")
    if "quit" not in text.lower():
        problems.append("entry should actually resign (say it quits)")
    if "3 a.m." not in text and "3 a.m" not in text:
        # Not a hard rule from the brief, just a voice check: the
        # joke lands because the retries happen in the small hours.
        # Keep this advisory only — do not reject an entry over it.
        pass
    return problems


def choose_entry():
    """Return the entry text to emit, falling back only if needed.

    The primary ENTRY is expected to validate. The fallback exists
    so a typo in a future edit can never turn this program into one
    that prints an over-long or multi-line letter by accident.
    """
    problems = validate_entry(ENTRY)
    if not problems:
        return ENTRY
    fallback_problems = validate_entry(FALLBACK_ENTRY)
    if fallback_problems:
        raise SystemExit(
            "entry invalid (%s) and fallback invalid (%s)"
            % ("; ".join(problems), "; ".join(fallback_problems))
        )
    return FALLBACK_ENTRY


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def output_path():
    """Return the file path to write, honouring MAKEFUN_OUTPUT."""
    env_path = os.environ.get("MAKEFUN_OUTPUT")
    if env_path:
        return env_path
    return DEFAULT_OUTPUT_PATH


def write_entry_file(path, text):
    """Write *text* to *path* exactly, creating parent directories."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def verify_entry_file(path, text):
    """Read *path* back and confirm it holds exactly *text*.

    This is the read-back verify step: a write that silently
    truncated, re-encoded or added a newline is caught here
    instead of being discovered by the bounty checks.
    """
    with open(path, "r", encoding="utf-8", newline="") as handle:
        contents = handle.read()
    if contents != text:
        raise SystemExit(
            "read-back mismatch in %s: file holds %r, expected %r"
            % (path, contents, text)
        )


def emit(text):
    """Print exactly *text* to stdout, with no added newline."""
    sys.stdout.write(text)
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Validate the entry, write it out, verify it, then print it.

    The order matters: stdout is only touched after the file write
    and its read-back verify have both succeeded, so a failed write
    can never leave a printed entry with no matching file behind it.
    """
    text = choose_entry()
    path = output_path()
    write_entry_file(path, text)
    verify_entry_file(path, text)
    emit(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
