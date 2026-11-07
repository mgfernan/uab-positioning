#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


def run_git(*args: str) -> str:
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def get_commit_messages() -> list[str]:
    tags = run_git("tag", "--list", "--sort=-version:refname")
    latest_tag = None
    for line in tags.splitlines():
        candidate = line.strip()
        if candidate:
            latest_tag = candidate
            break

    range_spec = f"{latest_tag}..HEAD" if latest_tag else "HEAD"
    raw_log = run_git("log", range_spec, "--format=%B%x00", "--no-merges")
    messages = [message.strip() for message in raw_log.split("\x00") if message.strip()]
    return messages


def normalize_commit_message(message: str) -> str:
    return message.splitlines()[0].strip() if message.splitlines() else ""


def compute_version_from_messages(messages: list[str]) -> str:
    breaking = 0
    feat = 0
    fix = 0
    other = 0

    for message in messages:
        subject = normalize_commit_message(message)
        body = "\n".join(message.splitlines()[1:]).strip()
        lower_body = body.lower()
        match = re.match(
            r"^(?P<type>[a-zA-Z]+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<description>.*)$",
            subject,
        )

        if match:
            commit_type = match.group("type").lower()
            if match.group("breaking"):
                breaking += 1
            if commit_type == "feat":
                feat += 1
            elif commit_type == "fix":
                fix += 1
            else:
                other += 1
            continue

        if "breaking change" in lower_body or "breaking change:" in lower_body or "BREAKING CHANGE:" in body:
            breaking += 1
        other += 1

    return f"{breaking}.{feat}.{fix}-r{other}"


def is_release_version(messages: list[str]) -> bool:
    version = compute_version_from_messages(messages)
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)-r(\d+)$", version)
    if not match:
        return False
    breaking, feat, fix, _ = [int(part) for part in match.groups()]
    return (breaking + feat + fix) > 0


def base_version(version: str) -> str:
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)-r\d+$", version)
    if not match:
        raise ValueError(f"Unsupported version value: {version!r}")
    return ".".join(match.groups()[:3])


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute the slide version from conventional commits.")
    parser.add_argument("--print-version", action="store_true", help="Print the computed version.")
    parser.add_argument("--print-base-version", action="store_true", help="Print the base X.Y.Z without the release count.")
    parser.add_argument("--print-is-release", action="store_true", help="Print whether the current version should be released.")
    args = parser.parse_args()

    messages = get_commit_messages()
    version = compute_version_from_messages(messages)
    release = is_release_version(messages)

    if args.print_version:
        print(version)

    if args.print_base_version:
        print(base_version(version))

    if args.print_is_release:
        print("true" if release else "false")

    if not args.print_version and not args.print_base_version and not args.print_is_release:
        print(version)


if __name__ == "__main__":
    main()
