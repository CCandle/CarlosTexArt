\ProvidesClass{CarlosTexArt}[2026/06/05 v0.2.0-dev General LaTeX template for scientific papers by Carlos QU]
\NeedsTeXFormat{LaTeX2e}

\DeclareOption*{%
    \PassOptionsToClass{\CurrentOption}{ctexart}
}
\ProcessOptions\relax
\LoadClass{ctexart}

% Page geometry
\RequirePackage{geometry}
\geometry{left=3.0cm, right=2.50cm, top=2.80cm, bottom=2.50cm}

% Fonts and encoding
\RequirePackage{fontspec}
\RequirePackage{lmodern}
\RequirePackage{hologo}

% Math
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{mathtools}
\RequirePackage{bm}
\RequirePackage{esint}
\RequirePackage{cases}

% Figures and tables
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{array}
\RequirePackage{makecell}
\RequirePackage{multirow}

% Units
\RequirePackage{siunitx}
\sisetup{
    detect-all,
    separate-uncertainty = true,
    per-mode = symbol
}

% Lists
\RequirePackage{enumitem}
\setlist[itemize]{itemsep=0.2em, topsep=0.3em}
\setlist[enumerate]{itemsep=0.2em, topsep=0.3em}

% Graphics
\RequirePackage{tikz}
\usetikzlibrary{arrows.meta, positioning, calc, shapes.geometric}
\RequirePackage[american]{circuitikz}
\RequirePackage{pgfplots}
\pgfplotsset{compat=1.18}

% Code and colors
\RequirePackage{xcolor}
\RequirePackage{listings}

% PDF and bookmarks (loaded late)
\RequirePackage{xurl}
\RequirePackage[
    hidelinks,
    unicode,
    bookmarksnumbered=true
]{hyperref}
\RequirePackage{bookmark}
\urlstyle{same}

\pdfstringdefDisableCommands{%
    \def\\{, }%
}

\makeatletter
\AtBeginDocument{%
    \hypersetup{
        pdftitle={\@title},
        pdfauthor={\@author}
    }%
}
\makeatother

% Other utilities
\RequirePackage{pdfpages}
\RequirePackage{xpatch}
\RequirePackage{xifthen}
\RequirePackage{xargs}
\RequirePackage{xparse}
\RequirePackage{changepage}

% lstlisting settings
\renewcommand{\lstlistingname}{代码}
\renewcommand{\lstlistlistingname}{代码清单}
\def\lstlistingautorefname{代码}
\lstdefinestyle{CarlosCodeBase}{
    basicstyle          = \zihao{-5}\ttfamily,
    numberstyle         = \zihao{-5}\ttfamily,
    keywordstyle        = \color[RGB]{122, 62, 157},
    stringstyle         = \color[RGB]{68, 140, 39},
    commentstyle        = \color{gray}\ttfamily,
    showspaces          = false,
    showstringspaces    = false,
    numbers             = left,
    captionpos          = t,
    frame               = single,
    frameround          = tttt,
    breaklines          = true,
    columns             = fixed,
    basewidth           = 0.6em,
    tabsize             = 4
}
\lstdefinestyle{Python}{
    style               = CarlosCodeBase,
    language            = Python
}
\lstdefinestyle{C}{
    style               = CarlosCodeBase,
    language            = C
}
\lstdefinestyle{Cpp}{
    style               = CarlosCodeBase,
    language            = C++
}

\makeatletter
\providecommand*{\toclevel@lstlisting}{1}
\AtBeginDocument{%
    \@ifundefined{c@lstlisting}{}{%
        \numberwithin{lstlisting}{section}%
    }%
}
\makeatother

% 字体、段落格式设定
\ExplSyntaxOn
\xpatchcmd\__xeCJK_check_family:n{\__xeCJK_warning:nxx}{\__xeCJK_info:nxx}{}{}
\xpatchcmd \fontspec_new_script:nn
    { \__fontspec_warning:nxx }
    { \__fontspec_info:nxx }
    {}{}
\newfontscript{CJK}{hani}
\ExplSyntaxOff
\linespread{1.25}
\newcommand{\xiaosi}{\zihao{-4}\songti}
\captionsetup[table]{name = 表, font = small}
\captionsetup[figure]{name = 图, font = small}
\ctexset
{
    section         = {format = \zihao{-3} \heiti \bf},
    subsection      = {format = \zihao{4} \heiti \bf},
    subsubsection   = {format = \zihao{4} \songti \bf},
}

% 自动引用名称（中文）
\def\equationautorefname{式}
\def\footnoteautorefname{脚注}
\def\itemautorefname{问题}
\def\figureautorefname{图}
\def\tableautorefname{表}
\def\appendixautorefname{附录}
\def\sectionautorefname{章}
\def\subsectionautorefname{节}
\def\subsubsectionautorefname{小节}
\def\paragraphautorefname{段落}
\def\subparagraphautorefname{子段落}
\def\theoremautorefname{定理}

% 自动编号设置（带章号）
\numberwithin{equation}{section}
\numberwithin{table}{section}
\numberwithin{figure}{section}


% 调整页眉页脚样式
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0mm}
\renewcommand{\footrulewidth}{0mm}

% Matter control for formal reports
\newcommand{\cqtfrontmatter}{%
    \cleardoublepage
    \pagenumbering{Roman}
    \setcounter{page}{1}
}

\newcommand{\cqtmainmatter}{%
    \cleardoublepage
    \pagenumbering{arabic}
    \setcounter{page}{1}
}

% PDF 封面命令
\newcommand{\cqtpdfcover}[2][]{%
    \includepdf[
        pages=1,
        pagecommand={\thispagestyle{empty}},
        #1
    ]{#2}%
}

% 自定义 \maketitle 样式
\makeatletter
\renewcommand*\maketitle{
    \begin{center}
        {\zihao{3} \heiti \bfseries \@title \par}
        \vskip 1em
        {\zihao{-4} \bfseries \@author \par}
        \vskip 2em
    \end{center}%
    \xiaosi
}
\makeatother

% 中文摘要环境，支持最多 5 个关键词
\newenvironmentx{cqtabstract}[5][1,2,3,4,5]
{
    \newcommand{\cqtabstractkeywords}{
        \ifthenelse{\isempty{#1}}{}
        {
            {\bfseries 关键词：}
            \ifthenelse{\isempty{#2}}{#1}
            {
                \ifthenelse{\isempty{#3}}{#1；#2}
                {
                    \ifthenelse{\isempty{#4}}{#1；#2；#3}
                    {
                        \ifthenelse{\isempty{#5}}{#1；#2；#3；#4}
                        {#1；#2；#3；#4；#5}
                    }
                }
            }
        }
    }
    \begin{adjustwidth}{1.5em}{1.5em}
    \begin{center}
        \zihao{3}\heiti\bfseries 摘\hspace{1em}要
    \end{center}
    \vspace{0.5em}
    \zihao{-4}\songti
    \par
}
{
    \par
    \cqtabstractkeywords
    \par
    \end{adjustwidth}
}

% 英文摘要环境，支持最多 5 个关键词
\newenvironmentx{cqtenabstract}[5][1,2,3,4,5]
{
    \newcommand{\cqtenabstractkeywords}{
        \ifthenelse{\isempty{#1}}{}
        {
            {\bfseries Keywords: }
            \ifthenelse{\isempty{#2}}{#1}
            {
                \ifthenelse{\isempty{#3}}{#1; #2}
                {
                    \ifthenelse{\isempty{#4}}{#1; #2; #3}
                    {
                        \ifthenelse{\isempty{#5}}{#1; #2; #3; #4}
                        {#1; #2; #3; #4; #5}
                    }
                }
            }
        }
    }
    \begin{adjustwidth}{1.5em}{1.5em}
    \begin{center}
        \zihao{3}\bfseries Abstract
    \end{center}
    \vspace{0.5em}
    \zihao{-4}
    \par
}
{
    \par
    \cqtenabstractkeywords
    \par
    \end{adjustwidth}
}
