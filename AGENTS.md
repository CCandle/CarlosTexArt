# AGENTS.md

本文件面向使用 CarlosTexArt 写论文、报告或工程文档的 AI agent。  
目标是帮助 agent 在不破坏模板结构的前提下，协助用户完成摘要、正文、图表、公式、代码、参考文献和附录。

## 基本原则

- 优先帮助用户完成内容，不要主动重构模板。
- 优先修改 `page/*.tex`、`refs/bibfile.bib`、`img/`、`src/` 中的用户内容。
- 除非用户明确要求，不要修改 `CarlosTexArt.cls`。
- 除非用户明确要求，不要修改 XeLaTeX + biblatex/biber + GB/T 7714-2025 的编译路线。
- 不要把所有正文都塞进 `main.tex`。
- 不要删除 front matter / main matter / bibliography 的主结构。
- 不要为了"修编译"删除用户内容；应先定位错误并说明原因。
- 不要编造数据、参考文献、实验结果、公式来源或图表含义。

## 文件分工

- `main.tex`：文档入口，负责标题、作者、日期、封面、摘要、目录、正文、附录和参考文献的组织。
- `page/abstract_zh.tex`：中文摘要。
- `page/abstract_en.tex`：英文摘要。
- `page/content.tex`：正文主体。
- `page/appendix.tex`：附录。
- `refs/bibfile.bib`：参考文献数据库。
- `img/`：正文图片。
- `src/`：被论文引用或展示的源码文件。
- `cover/`：用户可自行创建，用于放置外部 PDF 封面，例如 `cover/cover.pdf`。
- `CarlosTexArt.cls`：模板样式文件，默认不要修改。

## 推荐修改位置

- 写正文时优先改 `page/content.tex`。
- 写中文摘要时改 `page/abstract_zh.tex`。
- 写英文摘要时改 `page/abstract_en.tex`。
- 写附录时改 `page/appendix.tex`。
- 添加参考文献时改 `refs/bibfile.bib`，并在正文中使用 `\cite{...}` 引用。
- 添加图片时把文件放入 `img/`。
- 添加外部代码文件时把文件放入 `src/`。
- 添加外部 PDF 封面时创建 `cover/` 并放入 `cover/cover.pdf`。

## 优先使用模板已验证写法

除非用户明确要求其他写法，否则优先使用本模板 demo 中已经验证可用的写法。不要自由发挥出复杂、不必要、未经验证的 LaTeX 结构。

### 章节与交叉引用

章节应使用标准结构：

```tex
\section{引言}
\subsection{研究背景}
```

需要交叉引用时，优先使用 `\label{}` 与 `\autoref{}`：

```tex
如 \autoref{fig:sample} 所示，系统输出随输入变化而变化。
```

不要手动写"图 1""表 2""公式 (3)"这类硬编码编号。

### 公式

单个公式优先使用：

```tex
\begin{equation}
    E = mc^2
    \label{eq:mass-energy}
\end{equation}
```

带条件或方程组时可使用：

```tex
\begin{equation}
    \begin{cases}
        \dot{x} = Ax + Bu \\[2pt]
        y = Cx + Du
    \end{cases}
    \label{eq:state-space}
\end{equation}
```

公式中的符号首次出现时，应在正文中解释其含义和单位。

### 图片

图片优先使用：

```tex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.5\textwidth]{img/example.png}
    \caption{示例图片}
    \label{fig:sample}
\end{figure}
```

要求：

* 图片文件放入 `img/`；
* 使用 `\caption{}` 给出清晰标题；
* 使用 `\label{}` 方便引用；
* 正文中使用 `\autoref{fig:sample}` 引用；
* 不要把 README preview 图当作正文图片复用。

### 表格

普通三线表优先使用 `booktabs` 风格：

```tex
\begin{table}[htbp]
    \centering
    \caption{系统参数}
    \begin{tabular}{ccc}
        \toprule
        参数 & 符号 & 数值 \\
        \midrule
        采样率 & $f_s$ & \SI{20}{\kilo\hertz} \\
        供电电压 & $V_{cc}$ & \SI{400}{\volt} \\
        线阻 & $R_w$ & \SI{10}{\milli\ohm} \\
        \bottomrule
    \end{tabular}
    \label{tab:params}
\end{table}
```

较宽的表可以使用 `tabularx`：

```tex
\newcolumntype{Y}{>{\centering\arraybackslash}X}

\begin{table}[htbp]
    \centering
    \caption{宽表参数}
    \label{tab:wide}
    \begin{tabularx}{0.85\textwidth}{YYY}
        \toprule
        参数 & 符号 & 数值 \\
        \midrule
        采样率 & $f_s$ & \SI{20}{\kilo\hertz} \\
        供电电压 & $V_{cc}$ & \SI{400}{\volt} \\
        线阻 & $R_w$ & \SI{10}{\milli\ohm} \\
        \bottomrule
    \end{tabularx}
\end{table}
```

要求：

* 表格标题使用 `\caption{}`；
* 表格引用使用 `\autoref{tab:...}`；
* 单位优先使用 `\SI{数值}{单位}`；
* 不要手动用空格对齐表格。

### 单位

单位优先使用 `siunitx`：

```tex
\SI{50}{\mega\hertz}
\SI{3.3}{\volt}
\SI{100}{\milli\ampere}
```

不要写成 `50 MHz`、`3.3V`、`100mA` 这类手工格式，除非用户明确要求。

### 代码

短代码可使用：

```tex
\lstinline|adc_value = read_adc();|
```

外部代码文件优先放入 `src/`，并使用：

```tex
\lstinputlisting[
    style=Python,
    caption={PID 控制器实现},
    label={lst:pid-controller}
]{src/pid_controller.py}
```

要求：

* 代码文件放入 `src/`；
* 使用 `caption` 和 `label`；
* 正文中用 `\autoref{lst:pid-controller}` 引用；
* 不要把大量代码直接粘进正文，除非用户明确要求。

### TikZ 框图

简单系统框图优先使用以下结构：

```tex
\begin{figure}[htbp]
    \centering
    \begin{tikzpicture}[
        node distance=1.8cm,
        block/.style={rectangle, draw, minimum width=2cm, minimum height=0.8cm},
        arrow/.style={-{Latex[length=2mm]}, thick}
    ]
        \node[block] (sensor) {传感器};
        \node[block, right=of sensor] (adc) {ADC};
        \node[block, right=of adc] (fpga) {FPGA};
        \node[block, right=of fpga] (host) {上位机};
        \draw[arrow] (sensor) -- (adc);
        \draw[arrow] (adc) -- (fpga);
        \draw[arrow] (fpga) -- (host);
    \end{tikzpicture}
    \caption{信号采集链路框图}
    \label{fig:signal-chain}
\end{figure}
```

要求：

* TikZ 图必须放在 `figure` 环境中；
* 使用 `caption` 和 `label`；
* 不要生成过度复杂、难维护的 TikZ 图；
* 如果图很复杂，优先建议用户外部绘图后放入 `img/`。

### CircuitikZ 电路图

简单电路图可使用：

```tex
\begin{figure}[htbp]
    \centering
    \begin{circuitikz}[american]
        \draw
        (0,0) to[V, l=$u_\mathrm{in}$] (0,3)
              to[R, l=$R$] (3,3)
              to[L, l=$L$] (6,3)
              to[C, l=$C$] (6,0)
              -- (0,0);
    \end{circuitikz}
    \caption{RLC 串联电路}
    \label{fig:rlc-circuit}
\end{figure}
```

要求：

* CircuitikZ 图必须放在 `figure` 环境中；
* 使用 `caption` 和 `label`；
* 节点和元件标注应简洁；
* 不要在没有用户确认的情况下画复杂电路。

## 摘要与关键词

中文摘要使用：

```tex
\begin{cqtabstract}[关键词1][关键词2][关键词3]
中文摘要内容。
\end{cqtabstract}
```

英文摘要使用：

```tex
\begin{cqtenabstract}[keyword1][keyword2][keyword3]
English abstract content.
\end{cqtenabstract}
```

模板会自动拼接关键词。不要要求用户手动写完整分号分隔字符串。

摘要写作要求：

* 摘要应概括研究背景、方法、结果和结论；
* 不要在摘要中展开过多细节；
* 不要引用未在正文中出现的结果；
* 不要使用夸张宣传语；
* 英文摘要应保持准确、简洁、专业。

## PDF 封面

如果用户有学校或课程要求的标准封面，可以：

1. 将 Word / WPS / Pages 封面导出为 PDF；
2. 创建 `cover/` 目录；
3. 将封面放为 `cover/cover.pdf`；
4. 在 `main.tex` 中启用：

```tex
\cqtpdfcover{cover/cover.pdf}
```

不要把封面图片硬塞进正文。

## 写作语言规范

写作目标是准确、清晰、克制、可复核。不要为了显得高级而牺牲可读性。

### 中文写作

* 使用正式、客观、简洁的科技论文/工程报告语体。
* 优先说明事实、方法、结果和限制，不要写成宣传文案。
* 避免口语化表达，例如"挺好""很强""非常厉害""显然没问题"。
* 避免空泛形容词，例如"大幅提升""显著优化""效果很好"，除非有数据支撑。
* 同一概念使用同一术语，不要在全文中反复换词。
* 首次出现缩写、符号和专有名词时应解释。
* 结论应与数据、公式、实验或引用对应，不要超出证据范围。
* 段落应围绕一个明确主题展开，避免一段中混入多个无关问题。
* 不要编造实验数据、参考文献、工程参数或结论。

### 英文写作

* Use clear, concise, and objective technical English.
* Prefer precise verbs and concrete nouns.
* Avoid exaggerated claims such as "excellent", "perfect", "remarkable", or "significantly" unless supported by data.
* Keep terminology consistent.
* Define symbols, abbreviations, and domain-specific terms when they first appear.
* Use active voice when it improves clarity, but passive voice is acceptable when the actor is unknown, unimportant, or when the object/process should be emphasized.
* Do not invent citations, datasets, numerical results, or experimental conclusions.
* Preserve the user's intended meaning; improve grammar and clarity without changing technical claims.

### 修改用户文字时

* 优先做"保意改写"：提升清晰度、准确性和结构，不改变技术含义。
* 不要擅自增加用户没有提供的数据、结论或文献。
* 如果发现逻辑缺口，应标注"需要用户补充"，不要自行补全。
* 对不确定内容使用谨慎表达，例如"可能""表明""在该条件下"，不要写成绝对结论。
* 保留必要的工程细节，不要为了简洁删除关键信息。

## 编译与检查

推荐编译命令：

```bash
latexmk -xelatex -interaction=nonstopmode -file-line-error -outdir=build main.tex
```

修改后应检查：

* 是否生成 `build/main.pdf`；
* 是否有 undefined references；
* 是否有 citation undefined；
* 是否有 empty bibliography；
* 图片路径是否正确；
* 参考文献 key 是否存在；
* 目录、图表、公式编号是否正常。

## 编译失败时的行为

如果编译失败：

1. 先读取错误日志中的第一处实质错误；
2. 优先定位用户刚刚修改过的文件；
3. 不要盲目大规模重写模板；
4. 不要删除参考文献、图片、公式或章节来"消除错误"；
5. 如果错误涉及缺失文件，应明确报告缺失路径；
6. 如果错误涉及宏包缺失，应先报告，不要自动 vendor CTAN 包。

## 禁止事项

除非用户明确要求，否则不要：

* 修改 `CarlosTexArt.cls`；
* 修改 `.vscode/` 配置；
* 修改 `.github/` workflow；
* 改用其他编译引擎；
* 改用 BibTeX / natbib；
* 删除 `refs/bibfile.bib`；
* 删除摘要、目录、正文、附录、参考文献主结构；
* 把临时文件、编译产物或 PDF 提交到版本库；
* 把 README preview 图当作正文图片复用。
