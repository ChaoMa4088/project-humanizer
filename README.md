# Project Humanizer

一个用于整理项目文档、代码注释和冗余实现的 Codex 技能。支持项目目录、ZIP 包或指定文件，保留事实、来源、对外接口与功能，减少模板化表达和脱离项目语境的写法。

## 主要能力

- 润色中英文 Markdown、TXT 和技术说明，核对文档与实现。
- 精简过长、过细的讲解式注释与模板 docstring，删除装饰性 emoji、横幅及重复步骤说明。
- 保留设计理由、业务约束、工具指令、许可证和真实来源声明。
- 允许有明确收益的局部重构，例如简化无用包装、整理命名和重复逻辑。
- Word 修改后要求检查排版；PDF 默认审阅并输出可编辑改写稿，有源文件时优先处理源文件。
- 交付变更报告，明确跳过项、待确认事实及实际验证范围。

这是供 Codex 读取的工作流技能，不是自动改写程序；不会凭风格判定作者，也不保证 AI 检测分数。Word/PDF 处理需要运行环境具备相应工具。

## 安装

仓库根目录就是技能目录，`SKILL.md` 无需移动。

1. 下载本仓库 ZIP 并解压，或将仓库克隆到本地。
2. 将包含 `SKILL.md` 的整个目录复制到 `$CODEX_HOME/skills/project-humanizer`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills/project-humanizer`。
3. 如果同名技能已经存在，先备份再替换；不要覆盖其他技能。

Windows 的默认位置为 `%USERPROFILE%\.codex\skills\project-humanizer`。技能使用本身不需要安装 Python 依赖；下方仓库验证工具需要 Python 3.10 或更高版本。

## 使用

在能发现此技能的 Codex 会话中输入：

```text
使用 $project-humanizer 整理这个项目：<项目目录或 ZIP 路径>。
重点精简冗长注释并删除注释中的装饰性 emoji，允许局部重构，保持功能和对外接口，交付变更报告。
```

也可以指定部分文件或排除目录：

```text
使用 $project-humanizer 整理 README.md 和 src/，排除 src/vendor/。
保留必要的设计说明，只调整有明确问题的内容。
```

Git 项目默认原位修改并保留差异；无版本管理的材料及 ZIP 默认生成独立副本。第三方代码、依赖、构建产物、锁文件和自动生成文件默认跳过。字符串、界面文案和测试数据中的 emoji 不属于注释清理范围。

## 项目结构

```text
SKILL.md                  技能入口与处理流程
agents/openai.yaml        展示信息及默认提示
references/code.md        代码、注释及重构规则
references/documents.md   文档表达与 Word/PDF 规则
scripts/validate.py       无第三方依赖的仓库结构检查
.github/workflows/validate.yml  GitHub 自动检查
```

## 验证

```text
python scripts/validate.py
```

验证器检查必需文件、技能名称、元数据格式、引用路径和 UTF-8 编码。GitHub Actions 使用相同检查。它不证明实际改写质量、代码行为等价或 Word/PDF 排版正确；这些仍需在真实任务中验证。

## 上传 GitHub

在 GitHub 创建空仓库，上传本目录中的文件与文件夹，包括 `.github` 和 `.gitignore`。也可用 GitHub Desktop 添加本目录并发布。ZIP 外层目录无需作为额外的仓库子目录上传，确保仓库首页能直接看到 `SKILL.md` 和本说明。

本项目包没有预先绑定远程地址，也没有替你创建或发布 GitHub 仓库。

## 贡献与授权

修改规则时保留事实、功能和来源保护边界；运行验证工具，并用真实材料检查行为。不要把单一词语、注释长度或规范格式当作 AI 来源证据。

此包未附开源许可证。公开仓库不自动等于授予开源使用许可；发布者应在选择许可后添加相应的 `LICENSE` 文件。项目未虚构版权人或作者署名。
