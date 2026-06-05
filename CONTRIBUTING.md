# Contributing

感谢你愿意改进 CarlosTexArt。这个项目保持轻量，适合中文科技论文、实验报告和工程文档使用。

## 报告问题

- 请说明使用的 TeX Live / MacTeX 版本、操作系统和编译方式。
- 如果是编译问题，请贴出关键错误日志，不需要提交 `build/` 目录或中间文件。
- 如果是版式问题，请描述期望效果和当前效果。

## 提交修改

- 从 `dev` 分支创建修改，并保持改动范围尽量小。
- 修改后请本地编译确认：

  ```bash
  latexmk -xelatex -outdir=build main.tex
  ```

- 不要提交 `build/`、根目录 PDF 或 LaTeX 中间文件，例如 `.aux`、`.bbl`、`.bcf`、`.log`、`.synctex.gz`。
- 不要把 TeX Live / CTAN 已提供的宏包、`.bst`、字体等文件 vendor 到仓库。
- 修改 `CarlosTexArt.cls` 时要保守，避免无关的排版逻辑调整。
- 不要为了单个文档需求把模板改成 thesis、book、beamer 或学校专用格式。
