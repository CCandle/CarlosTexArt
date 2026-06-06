# Contributing

感谢你愿意改进 CarlosTexArt。本项目保持轻量，适合中文科技论文、实验报告和工程文档使用。

## 报告问题

- 请说明使用的 TeX Live / MacTeX 版本、操作系统和编译方式。
- 如果是编译问题，请贴出关键错误日志，不需要提交 `build/`、`dist/` 目录或中间文件。
- 如果是版式问题，请描述期望效果和当前效果。

## 开发工具

- Python 3.9+（用于 starter 包生成脚本）
- TeX Live / MacTeX（含 latexmk、xelatex、biber）
- VS Code + LaTeX Workshop（推荐）

## 仓库结构

```text
.
├── CarlosTexArt.cls          # 模板类文件
├── main.tex                  # 主文件（含 demo 内容）
├── AGENTS.md                 # 用户写论文时给 AI agent 的工作规则
├── README.md                 # 用户说明
├── CONTRIBUTING.md           # 本文件：开发者维护规则
├── page/
│   ├── abstract_zh.tex
│   ├── abstract_en.tex
│   ├── content.tex           # 正文主体（含 demo 内容）
│   ├── appendix.tex
│   └── examples/             # LaTeX 写法示例
├── refs/
│   └── bibfile.bib
├── img/
│   └── example.png
├── src/
│   └── pid_controller.py
├── tools/
│   └── make_starter_package.py
├── assets/
│   └── preview.png           # GitHub README 展示图
└── .github/
    └── workflows/
        ├── build.yml         # 普通 push / PR
        └── release.yml       # tag 触发 release
```

## CI 流程概述

- `build.yml`：每次 push 或 PR 触发，在 TeX Live 容器中编译 demo PDF、生成 starter zip、验证 starter 可编译。
- `release.yml`：tag 触发，先 build-assets（编译 demo PDF + 生成 starter zip + 验证），再 release（`gh release create --generate-notes`）。

## 修改 starter 包

`tools/make_starter_package.py` 生成用户开工用的 starter zip。

修改后验证步骤：

1. 生成测试包：

   ```bash
   python tools/make_starter_package.py --version test --output dist/test-starter.zip
   ```

2. 解压到一个临时目录（不覆盖仓库）：

   ```bash
   rm -rf /tmp/carlostexart-starter-test
   mkdir -p /tmp/carlostexart-starter-test
   unzip dist/test-starter.zip -d /tmp/carlostexart-starter-test
   ```

3. 在解压目录编译：

   ```bash
   cd /tmp/carlostexart-starter-test/CarlosTexArt-test-starter
   latexmk -xelatex -interaction=nonstopmode -file-line-error -outdir=build main.tex
   ```

4. 确认编译通过，不包含仓库特定内容（如 Carlos QU、ccandle 邮箱等）。

5. 清理临时目录。

## 修改 CI workflow

- 修改 `.github/workflows/build.yml` 或 `.github/workflows/release.yml` 后，确保语法正确。
- 如果修改了 starter 验证逻辑，确认验证步骤能捕获常见错误（缺失文件、编译失败等）。
- CI 不做 TeX Live 缓存或自定义镜像，保持轻量。
- 添加 `concurrency` 避免同一分支重复 run 堆积。

## 提交修改

- 从 `dev` 分支创建修改，并保持改动范围尽量小。
- 修改后请本地编译确认：

  ```bash
  latexmk -xelatex -outdir=build main.tex
  ```

- 不要提交 `build/`、根目录 PDF 或 LaTeX 中间文件，例如 `.aux`、`.bbl`、`.bcf`、`.log`、`.synctex.gz`。
- 不要把 TeX Live / CTAN 已提供的宏包、`.bst`、字体等文件 vendor 到仓库。
- 参考文献数据库位于 `refs/`。
- 如果修改 starter 包逻辑，请运行 `python tools/make_starter_package.py` 验证。
- 修改 `CarlosTexArt.cls` 时要保守，避免无关的排版逻辑调整。
- 不要为了单个文档需求把模板改成 thesis、book、beamer 或学校专用格式。
