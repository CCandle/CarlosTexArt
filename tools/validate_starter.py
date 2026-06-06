#!/usr/bin/env python3
"""Validate a CarlosTexArt starter zip and optionally compile it."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


FORBIDDEN_ENTRIES = [
    ".git/",
    ".github/",
    ".gitignore",
    ".gitattributes",
    ".gitkeep",
    "CONTRIBUTING.md",
    "assets/",
    "docs/",
    "doc/",
    "build/",
    "dist/",
    "page/examples/",
    "img/example.png",
    "src/pid_controller.py",
]

REQUIRED_ENTRIES = [
    "CarlosTexArt.cls",
    "main.tex",
    "AGENTS.md",
    "README.md",
    "refs/bibfile.bib",
    "page/abstract_zh.tex",
    "page/abstract_en.tex",
    "page/content.tex",
    "page/appendix.tex",
    "img/",
    "src/",
    "cover/",
]

REQUIRED_MAIN_TOKENS = [
    r"\documentclass[UTF8,AutoFakeBold,twoside,fontset=fandol]{CarlosTexArt}",
    r"\addbibresource{refs/bibfile.bib}",
    r"\title{在这里填写标题}",
    r"\author{在这里填写作者}",
    r"\include{page/abstract_zh}",
    r"\include{page/abstract_en}",
    r"\tableofcontents",
    r"\include{page/content}",
    r"\include{page/appendix}",
    r"\printbibliography[heading=bibintoc,title={参考文献}]",
]

FORBIDDEN_MAIN_TOKENS = [
    "Carlos QU",
    "ccandle@foxmail.com",
    r"\title{科技论文模板}",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path, help="Starter zip to validate.")
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Extract the starter zip and compile main.tex with latexmk.",
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        help="Directory to use for extraction when --compile is enabled.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def normalize_name(name: str) -> str:
    return name.replace("\\", "/")


def has_suffix(names: list[str], suffix: str) -> bool:
    return any(name.endswith(suffix) for name in names)


def forbidden_matches(names: list[str]) -> list[str]:
    matches: list[str] = []
    for name in names:
        parts = name.rstrip("/").split("/")
        suffixes = ["/".join(parts[index:]) for index in range(len(parts))]
        for forbidden in FORBIDDEN_ENTRIES:
            target = forbidden.rstrip("/")
            if forbidden.endswith("/"):
                if any(suffix == target or suffix.startswith(f"{target}/") for suffix in suffixes):
                    matches.append(name)
                    break
            elif target in suffixes:
                matches.append(name)
                break
    return matches


def read_starter_main(zf: zipfile.ZipFile, names: list[str]) -> str:
    main_files = [name for name in names if name.endswith("main.tex")]
    if len(main_files) != 1:
        fail(f"Expected exactly one starter main.tex, found {len(main_files)}: {main_files}")
    try:
        return zf.read(main_files[0]).decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(f"starter main.tex is not valid UTF-8: {exc}")


def validate_zip(zip_path: Path) -> list[str]:
    if not zip_path.is_file():
        fail(f"Starter zip not found: {zip_path}")

    try:
        with zipfile.ZipFile(zip_path) as zf:
            names = [normalize_name(name) for name in zf.namelist()]

            bad_entries = forbidden_matches(names)
            if bad_entries:
                fail(f"Forbidden entries found in starter zip: {bad_entries}")

            missing = [entry for entry in REQUIRED_ENTRIES if not has_suffix(names, entry)]
            if missing:
                fail(f"Required entries missing from starter zip: {missing}")

            main_text = read_starter_main(zf, names)
            missing_tokens = [token for token in REQUIRED_MAIN_TOKENS if token not in main_text]
            if missing_tokens:
                fail(f"Required tokens missing from starter main.tex: {missing_tokens}")

            bad_tokens = [token for token in FORBIDDEN_MAIN_TOKENS if token in main_text]
            if bad_tokens:
                fail(f"Forbidden tokens found in starter main.tex: {bad_tokens}")

            return names
    except zipfile.BadZipFile as exc:
        fail(f"Invalid starter zip: {exc}")


def top_level_dirs(extract_dir: Path) -> list[Path]:
    return [path for path in extract_dir.iterdir() if path.is_dir()]


def compile_starter(zip_path: Path, workdir: Path | None) -> None:
    if workdir is None:
        with tempfile.TemporaryDirectory(prefix="carlostexart-starter-test-") as tmp:
            extract_and_compile(zip_path, Path(tmp))
        return

    if workdir.exists():
        shutil.rmtree(workdir)
    workdir.mkdir(parents=True)
    extract_and_compile(zip_path, workdir)


def extract_and_compile(zip_path: Path, extract_dir: Path) -> None:
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(extract_dir)
    except zipfile.BadZipFile as exc:
        fail(f"Invalid starter zip during extraction: {exc}")

    starter_dirs = top_level_dirs(extract_dir)
    if len(starter_dirs) != 1:
        fail(f"Expected exactly one top-level starter directory, found {len(starter_dirs)}: {starter_dirs}")

    starter_dir = starter_dirs[0]
    command = [
        "latexmk",
        "-xelatex",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-outdir=build",
        "main.tex",
    ]

    try:
        subprocess.run(command, cwd=starter_dir, check=True)
    except subprocess.CalledProcessError as exc:
        fail(f"Compile failed: {' '.join(command)}\nWorking directory: {starter_dir}\nExit code: {exc.returncode}")
    except FileNotFoundError:
        fail("Compile failed: latexmk command not found")

    pdf_path = starter_dir / "build" / "main.pdf"
    if not pdf_path.is_file():
        fail(f"Compiled PDF not found: {pdf_path}")

    print(f"Starter compile passed: {pdf_path}")


def main() -> None:
    args = parse_args()
    zip_path = args.zip_path.resolve()
    names = validate_zip(zip_path)
    print(f"Starter content validation passed: {zip_path}")
    print(f"Entries checked: {len(names)}")

    if args.compile:
        compile_starter(zip_path, args.workdir.resolve() if args.workdir else None)


if __name__ == "__main__":
    main()
