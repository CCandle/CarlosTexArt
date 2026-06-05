# CarlosTexArt

轻量、现代、工程友好的中文 LaTeX 论文/报告模板。

适用于中文科技论文、课程报告、实验报告、工程文档和项目阶段报告。默认使用 XeLaTeX、biblatex/biber、GB/T 7714-2025，并提供 VS Code + LaTeX Workshop 开箱配置。

## 特性

- 中文友好：基于 `ctexart` 与 XeLaTeX
- 参考文献：`biblatex` + `biber` + GB/T 7714-2025
- 工程写作：内置 `siunitx`、`booktabs`、`listings`、TikZ、CircuitikZ 示例
- VS Code 友好：提供 LaTeX Workshop recipe 与 snippets
- Agent 友好：提供 `AGENTS.md`，约束 LLM coding agent 的修改边界
- 轻量可迁移：不 vendor CTAN 包，不绑定系统专有字体

## 适用场景

- 中文课程论文
- 中文实验报告
- 工程项目报告
- 阶段性技术文档
- 需要 GB/T 7714 参考文献的轻量论文/报告

## 不适用场景

- 已有强制学校模板的毕业论文
- 需要严格出版社版式的论文
- beamer 幻灯片
- 需要复杂封面、原创性声明、学位论文评审表等完整 thesis 流程

## 预览

示例 PDF 建议通过 GitHub Releases 发布，避免将编译产物提交到主分支。

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

## 常用模板命令

| 命令/环境 | 用途 |
|---|---|
| `\cqtfrontmatter` | 开始前置部分，使用 Roman 页码 |
| `\cqtmainmatter` | 开始正文部分，页码从 1 重新开始 |
| `\cqtpdfcover{...}` | 插入外部 PDF 封面 |
| `cqtabstract` | 中文摘要环境 |
| `cqtenabstract` | 英文摘要环境 |

模板支持以下正式结构：
- PDF 封面
- 中文摘要（Roman 页码）
- 英文摘要（Roman 页码）
- 目录（Roman 页码）
- 正文（Arabic 页码）
- 附录
- 参考文献

## 单栏与双栏

默认单栏。若需要期刊/会议风格双栏，可在文档类选项中加入 `twocolumn`：

```tex
\documentclass[UTF8,AutoFakeBold,twoside,twocolumn,fontset=fandol]{CarlosTexArt}
```

双栏文档中的通栏图表可以使用 `figure*` 和 `table*`。

## PDF 封面

- 用户可以用 Word/docx 填写学校或课程封面
- 导出为 PDF
- 放到 `cover/cover.pdf`
- 在 `main.tex` 中使用：

  ```tex
  \cqtpdfcover{cover/cover.pdf}
  ```

## 目录结构

```text
├── AGENTS.md                   # LLM agent 修改纪律
├── CarlosTexArt.cls            # 模板类文件（一般无需修改）
├── main.tex                    # 主文件（改标题、作者、加载 biblatex）
├── cover/                      # 外部 PDF 封面目录
│   └── .gitkeep
├── page/
│   ├── abstract_zh.tex         # 中文摘要
│   ├── abstract_en.tex         # 英文摘要
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
├── sty/                        # 仅用于项目自定义的小型宏包
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

本项目使用 MIT License 开源。详见 [LICENSE](LICENSE)。
