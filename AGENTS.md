# AGENTS.md

本文件是给 OpenCode、Codex、Claude Code 及其他 LLM coding agent 使用的工程纪律文件。  

任何 agent 修改本项目时，必须严格遵守本文档。不要猜测用户意图，不要扩展任务范围。

## 优先级

执行任务时遵循以下优先级：

1. 用户在当前任务中的明确指令
2. 本文件 `AGENTS.md`
3. `README.md`
4. 现有代码和文档风格

如果任务会导致 `build/`、`main.pdf` 或 LaTeX 中间文件被提交，必须先清理。

## 项目定位

本项目目标：

- 使用 VS Code + LaTeX Workshop 编写中文科技论文、实验报告和工程文档。
- 使用 XeLaTeX 编译。
- 使用 `biblatex` + `biber` 管理参考文献。
- 默认使用 GB/T 7714-2025 参考文献格式。
- 提供公式、图表、单位、代码清单、TikZ、CircuitikZ、附录和参考文献的最小可用示例。

本模板不是完整 thesis class，也不内置学校专用流程；但支持正式论文/报告常见结构，包括 PDF 封面、中英文摘要、前置页码、正文页码重置、附录和参考文献。

## 命名前缀规则

本项目的用户级自定义命令和环境必须使用 `cqt` 前缀。  
不要新增无前缀的全局用户命令。  
不要恢复 `\carlosfrontmatter`、`\carlosmainmatter`。  
本项目已进入公开发布阶段。除非用户明确要求，否则不要随意引入 breaking changes；如确需破坏兼容，应在 README、AGENTS.md 和 Release Notes 中明确说明。

## 硬性禁止事项

除非用户明确要求，否则禁止执行以下操作：

1. 不要改用 LuaLaTeX、pdfLaTeX 或 upLaTeX。
2. 不要改用 BibTeX、natbib、`.bst` 参考文献路线。
3. 不要引入 `minted`、`shell-escape` 或任何需要额外执行权限的代码高亮方案。
4. 不要把 TeX Live / CTAN 已提供的 `.sty`、`.bst`、字体文件复制进仓库。
5. 不要恢复或新增本地 `gbt7714.sty`、`gbt7714-numerical.bst` 等旧文件。
6. 不要把编译产物提交进仓库，包括 `main.pdf`、`build/`、`.aux`、`.bbl`、`.bcf`、`.log`、`.synctex.gz` 等。
7. 不要修改模板主结构为 thesis、book、beamer 或学校专用格式。
8. 不要重写整个 README、class 文件或示例目录。
9. 不要大规模格式化无关文件。
10. 不要为了消除 warning 做计划外重构。

## 允许修改的范围

常规任务只允许修改以下内容：

- `main.tex`：标题、作者、biblatex 配置、正文入口。
- `page/*.tex`：摘要、正文、附录。
- `page/examples/*.tex`：示例内容。
- `doc/bibfile.bib`：参考文献条目。
- `README.md`：人类使用说明。
- `AGENTS.md`：agent 执行纪律。
- `.vscode/settings.json`：LaTeX Workshop 编译配置。
- `.vscode/latex.code-snippets`：VS Code 片段。
- `.gitignore`：忽略规则。
- `CarlosTexArt.cls`：仅限模板基础配置、小范围宏包和格式修正。

修改 `CarlosTexArt.cls` 时必须非常保守。除非用户明确要求，不要调整页面尺寸、字号、标题样式、页眉页脚、摘要环境或参考文献路线。

## 编译路线

默认编译路线必须保持为：

```text
XeLaTeX + biblatex + biber + GB/T 7714-2025
```

`main.tex` 中必须保留类似配置：

```tex
\usepackage[
    backend=biber,
    style=gb7714-2025,
    sorting=none,
    gbnamefmt=uppercase,
    gbpub=false
]{biblatex}

\addbibresource{doc/bibfile.bib}
```

禁止恢复以下旧命令：

```tex
\bibliographystyle{...}
\bibliography{...}
```

## 文件组织规则

推荐结构如下：

```text
.
├── main.tex
├── CarlosTexArt.cls
├── README.md
├── AGENTS.md
├── doc/
│   └── bibfile.bib
├── cover/
│   └── .gitkeep
├── img/
├── page/
│   ├── abstract_zh.tex
│   ├── abstract_en.tex
│   ├── content.tex
│   ├── appendix.tex
│   └── examples/
├── src/
├── sty/
└── .vscode/
```

规则：

* 正文内容放在 `page/`。
* 示例内容放在 `page/examples/`。
* 图片放在 `img/`。
* 代码示例放在 `src/`。
* 参考文献放在 `doc/bibfile.bib`。
* `sty/` 只允许放项目自定义的小型宏包，不允许 vendor 大型第三方包。

## `\input{}` 与 `\include{}` 使用规则

不要机械替换 `\input{}` 与 `\include{}`。二者用途不同。

* `\input{}`：直接插入文件内容，不自动分页，适合示例、小节、局部片段。
* `\include{}`：插入文件前后会分页，并生成独立 `.aux`，适合较大的章/节文件，也方便使用 `\includeonly{}` 做局部编译。

本模板遵循以下约定：

* `main.tex` 中顶层文档单元（摘要、正文章节、附录）使用 `\include{}`。
* `page/content.tex` 内部引用示例时使用 `\input{}`。
* 不要机械互换，不要将 `page/content.tex` 内部的 `\input{}` 改为 `\include{}`。

## 修改前检查

执行任务前必须先检查：

```bash
pwd
find . -maxdepth 3 -type f | sort
```

然后阅读至少以下文件：

```text
main.tex
CarlosTexArt.cls
README.md
doc/bibfile.bib
.vscode/settings.json
```

如果用户任务涉及正文，还必须阅读相关 `page/*.tex` 文件。

如果实际结构与 README 或本文件明显不一致，立即停止并报告，不要猜测。

## 编译与验证

修改后优先执行：

```bash
latexmk -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -outdir=build main.tex
```

验证要求：

1. 必须生成 `build/main.pdf`。
2. 根目录不应生成 `main.pdf`。
3. 不应出现 `undefined references`。
4. 不应出现 `citation undefined`。
5. 不应出现 `empty bibliography`。
6. 不应引用本地旧版 `gbt7714.sty` 或 `.bst` 文件。
7. 不应引用 `sty/matlab.sty`。
8. 允许保留不影响 PDF 的普通 warning，但必须在报告中说明。

如果修改了参考文献配置，必须确认 `biber` 被正确调用。

## 清理规则

可以清理编译产物，但不得删除源码。

允许删除：

```text
build/
main.pdf
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.run.xml
*.synctex.gz
*.toc
*.xdv
.DS_Store
__MACOSX/
```

禁止删除：

```text
main.tex
CarlosTexArt.cls
README.md
AGENTS.md
LICENSE
doc/bibfile.bib
img/example.png
src/pid_controller.py
page/*.tex
page/examples/*.tex
```

## 遇到问题时的行为

遇到以下情况必须立即停止并报告，不要自行绕路：

1. 缺少 `xelatex`、`latexmk`、`biber`。
2. 缺少必要 TeX 包。
3. `gb7714-2025` 样式不存在。
4. 编译错误来自 TeX 环境缺失，而不是项目源码。
5. 需要联网、安装包、下载字体或复制外部文件。
6. 需要修改用户未授权的模板结构。
7. 需要引入新编译引擎或新参考文献系统。
8. 当前任务无法在小范围修改内完成。

报告格式：

```md
## 已停止

### 停止原因
- ...

### 已检查内容
- ...

### 未执行内容
- ...

### 建议用户确认
- ...
```

## 最终报告格式

每次修改完成后，必须按以下格式报告：

```md
## 修改完成

### 修改文件
- ...

### 新增文件
- ...

### 删除文件
- ...

### 关键变化
- ...

### 验证结果
- 编译命令：...
- PDF 输出：...
- undefined references：有 / 无
- citation undefined：有 / 无
- bibliography empty：有 / 无
- 剩余 warning：...

### 剩余问题
- 如果没有，写“无”
```

不要只说“已完成”。必须说明做了什么、验证了什么、还剩什么。
