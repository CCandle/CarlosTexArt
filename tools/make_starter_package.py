#!/usr/bin/env python3
"""Build a clean CarlosTexArt starter zip."""

from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "CarlosTexArt-starter.zip"

STARTER_README = """# CarlosTexArt Starter

这是 CarlosTexArt 的干净开工版，适合直接用于中文科技论文、实验报告和工程文档。

## 环境要求

- TeX Live / MacTeX
- XeLaTeX
- latexmk
- biber
- VS Code + LaTeX Workshop（可选）

## VS Code 编译

用 VS Code 打开本文件夹，打开 `main.tex`，使用 LaTeX Workshop 的 `latexmk-xelatex` recipe 编译。

## 命令行编译

```bash
latexmk -xelatex -outdir=build main.tex
```

## 文件结构

```text
CarlosTexArt.cls
main.tex
refs/bibfile.bib
page/
img/
src/
cover/
.vscode/
```

## 写正文

正文入口是 `page/content.tex`。摘要在 `page/abstract_zh.tex` 和 `page/abstract_en.tex`，附录在 `page/appendix.tex`。

## 参考文献

参考文献数据库位于 `refs/bibfile.bib`。正文中使用 `\\cite{...}` 引用条目，文末会自动打印参考文献。

## PDF 封面

如需外部封面，可自行把 Word/docx 导出的 PDF 放到 `cover/cover.pdf`，并在 `main.tex` 中启用 `\\cqtpdfcover{cover/cover.pdf}`。

## 空目录

`img/`、`src/`、`cover/` 是空目录，分别用于正文图片、代码文件和外部 PDF 封面。
"""

STARTER_FILES = {
    "page/abstract_zh.tex": r"""\begin{cqtabstract}[中文论文][LaTeX][模板]
这里填写中文摘要。摘要应简要说明研究背景、方法、结果和结论。
\end{cqtabstract}
""",
    "page/abstract_en.tex": r"""\begin{cqtenabstract}[Chinese paper][LaTeX][template]
Write the English abstract here. Summarize the background, method, results, and conclusion.
\end{cqtenabstract}
""",
    "page/content.tex": r"""\section{引言}

这里填写引言内容。示例参考文献引用：\cite{latex-intro}。

\section{正文}

这里填写正文内容。

\section{结论}

这里填写结论内容。
""",
    "page/appendix.tex": r"""\appendix

\section{附录}

这里填写附录内容。
""",
    "refs/bibfile.bib": """@book{latex-intro,
  author    = {刘海洋},
  title     = {LaTeX入门},
  publisher = {电子工业出版社},
  year      = {2013},
  address   = {北京}
}
""",
    "README.md": STARTER_README,
}

COPY_FILES = [
    "CarlosTexArt.cls",
    "main.tex",
    "LICENSE",
    ".vscode/settings.json",
    ".vscode/latex.code-snippets",
]

EMPTY_DIRS = ["img", "src", "cover"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Version label for the starter directory name.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output zip path. Default: dist/CarlosTexArt-starter.zip",
    )
    return parser.parse_args()


def starter_name(version: str | None) -> str:
    if version:
        return f"CarlosTexArt-{version}-starter"
    return "CarlosTexArt-starter"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def prepare_tree(destination: Path) -> None:
    for relative in COPY_FILES:
        source = ROOT / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    for relative, content in STARTER_FILES.items():
        write_text(destination / relative, content)

    for relative in EMPTY_DIRS:
        (destination / relative).mkdir(parents=True, exist_ok=True)


def add_directory(zf: zipfile.ZipFile, directory_name: str) -> None:
    info = zipfile.ZipInfo(directory_name.rstrip("/") + "/")
    info.external_attr = 0o755 << 16
    zf.writestr(info, b"")


def make_zip(source_dir: Path, output: Path, top_name: str) -> list[str]:
    output.parent.mkdir(parents=True, exist_ok=True)
    entries: list[str] = []
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        add_directory(zf, f"{top_name}/")
        entries.append(f"{top_name}/")

        for relative in EMPTY_DIRS:
            arcname = f"{top_name}/{relative}/"
            add_directory(zf, arcname)
            entries.append(arcname)

        for path in sorted(source_dir.rglob("*")):
            if path.is_dir():
                continue
            relative = path.relative_to(source_dir)
            arcname = f"{top_name}/{relative.as_posix()}"
            zf.write(path, arcname)
            entries.append(arcname)
    return entries


def main() -> None:
    args = parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    top_name = starter_name(args.version)

    with tempfile.TemporaryDirectory(prefix="carlostexart-starter-") as tmp:
        starter_root = Path(tmp) / top_name
        prepare_tree(starter_root)
        entries = make_zip(starter_root, output, top_name)

    try:
        display_output = output.relative_to(ROOT)
    except ValueError:
        display_output = output

    print(f"Created {display_output}")
    for entry in entries:
        if entry.endswith("/") or entry.endswith(("CarlosTexArt.cls", "main.tex", "refs/bibfile.bib", "page/content.tex", "README.md")):
            print(f"  {entry}")


if __name__ == "__main__":
    main()
