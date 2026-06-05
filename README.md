# 科技论文 LaTeX 模板

适用于 **Windows / macOS / Linux + VS Code + LaTeX Workshop + TeX Live** 环境的通用科技论文模板。

## 前置依赖

- [TeX Live](https://tug.org/texlive/)（推荐 2021 以上）
- [VS Code](https://code.visualstudio.com/)
- [LaTeX Workshop 插件](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

## 快速上手

1. 用 VS Code 打开本文件夹
2. 打开 `main.tex`，按下 `Ctrl+Alt+B` 编译
3. 按下 `Ctrl+Alt+V` 预览 PDF

## Recipe 选择

VS Code 左下角「BUILD」下拉菜单选择：

| Recipe | 用途 |
|--------|------|
| **xelatex**（默认） | 日常写内容，不改参考文献时用，单次编译很快 |
| **xebibitex** | 新增或修改了 `doc/bibfile.bib` 中的文献后，全量编译 |

本模板默认使用 `fontset=fandol`，依赖 TeX Live 自带的 Fandol 中文字体，避免绑定 Windows 或 macOS 专有字体。如需使用宋体、Times New Roman 等本机字体，可在个人论文中自行覆盖字体设置。

## 目录结构

```
├── CarlosTexArt.cls            # 模板类文件（一般无需修改）
├── main.tex                    # 主文件（改标题、作者在这里）
├── page/
│   ├── abstract.tex            # 摘要
│   ├── content.tex             # 正文（按章节拆文件）
│   └── appendix.tex            # 附录
├── doc/
│   └── bibfile.bib             # 参考文献数据库
├── img/                        # 图片文件夹
├── src/                        # 源码文件夹
├── sty/
│   └── matlab.sty              # MATLAB 代码高亮定义
├── gbt7714.sty                 # GB/T 7714 参考文献样式包
├── gbt7714-numerical.bst       # GB/T 7714 数字引用样式
└── .vscode/
    ├── settings.json           # LaTeX Workshop 配置
    └── latex.code-snippets     # 常用代码片段
```

## 自定义

- **标题/作者**：改 `main.tex` 中的 `\title{}` 和 `\author{}`
- **添加章节**：在 `page/` 下新建 `.tex` 文件，在 `main.tex` 中用 `\include{}` 引入
- **添加参考文献**：在 `doc/bibfile.bib` 中添加条目，编译时选 `xebibitex`
- **子图排版**：`main.tex` 中取消 `\usepackage{subcaption}` 的注释即可

## License

本模板基于 CCandle 个人多年使用的 LaTeX 配置整理而成，供参考使用。
