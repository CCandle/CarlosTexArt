# 科技论文 LaTeX 模板

适用于 **VS Code + LaTeX Workshop + XeLaTeX + biblatex/biber + GB/T 7714-2025** 的通用中文科技/工程报告模板。

## 前置依赖

- TeX Live 2026 / MacTeX 2026，或较新的 TeX Live 发行版
- VS Code
- LaTeX Workshop
- latexmk
- biber

模板默认使用 `fontset=fandol`，依赖 TeX Live 自带的 Fandol 中文字体，避免绑定 Windows 或 macOS 专有字体。

## 快速上手

1. 用 VS Code 打开本文件夹
2. 打开 `main.tex`
3. 使用 LaTeX Workshop 的 `latexmk-xelatex` recipe 编译
4. 输出文件在 `build/main.pdf`

默认编译输出位于 `build/main.pdf`。模板分发包不应包含根目录 `main.pdf` 或 `build/` 等编译产物。

## Agent 使用说明

如果使用 OpenCode、Codex、Claude Code 等 agent 修改本模板，请先让 agent 阅读 `AGENTS.md`。

`README.md` 面向人类使用者，说明环境、目录结构和日常使用方式；`AGENTS.md` 面向 LLM agent，定义修改边界、禁止事项、验证要求和停止条件。

## 环境自检

```bash
xelatex --version
latexmk -v
biber --version
kpsewhich ctexart.cls
kpsewhich biblatex-gb7714-2015.sty
kpsewhich circuitikz.sty
kpsewhich siunitx.sty
kpsewhich pgfplots.sty
```

## Recipe 说明

| Recipe | 用途 |
|--------|------|
| latexmk-xelatex | 推荐默认方式，自动处理 XeLaTeX 和 biber |
| xelatex -> biber -> xelatex*2 | 手动全量编译方式，适合排查参考文献问题 |

## 目录结构

```
├── AGENTS.md                   # LLM agent 修改纪律
├── CarlosTexArt.cls            # 模板类文件（一般无需修改）
├── main.tex                    # 主文件（改标题、作者、加载 biblatex）
├── page/
│   ├── abstract.tex            # 摘要
│   ├── content.tex             # 正文入口，引入 examples
│   ├── appendix.tex            # 附录
│   └── examples/
│       ├── math.tex            # 公式示例
│       ├── figure_table.tex    # 图表与单位示例
│       ├── code.tex            # 代码清单示例
│       ├── tikz.tex            # TikZ 框图示例
│       └── circuitikz.tex      # CircuitikZ 电路图示例
├── doc/
│   └── bibfile.bib             # 参考文献数据库
├── img/                        # 图片文件夹
├── src/
│   └── pid_controller.py       # 代码引用示例
├── sty/                        # 仅用于项目自定义的小型宏包，不建议放入 TeX Live/CTAN 已提供的大型 `.sty`、`.bst` 或字体文件
└── .vscode/
    ├── settings.json           # LaTeX Workshop 配置
    └── latex.code-snippets     # 常用代码片段
```

## 自定义

- **标题/作者**：改 `main.tex` 中的 `\title{}` 和 `\author{}`
- **参考文献**：在 `doc/bibfile.bib` 中添加条目
- **添加章节**：在 `page/` 下新建 `.tex` 文件，并在 `main.tex` 中引入。小节、示例和局部片段推荐使用 `\input{}`；较大的章节可以使用 `\include{}`，它会自动分页，并支持 `\includeonly{}` 局部编译。
- **图片**：放在 `img/` 目录下
- **代码**：放在 `src/` 目录下
- **工程示例**：在 `page/examples/` 中参考
- **GB/T 7714 版本**：如果学校/期刊仍要求 GB/T 7714-2015，可以把 `main.tex` 里的 `style=gb7714-2025` 改成 `style=gb7714-2015`

## License

本模板基于 CCandle 个人多年使用的 LaTeX 配置整理而成，供参考使用。
