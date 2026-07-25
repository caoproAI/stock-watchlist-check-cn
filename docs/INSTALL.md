# 安装说明

## Codex

把整个 `stock-watchlist-check-cn` 文件夹复制到 Codex 的 Skills 目录，然后重新打开会话。

## WorkBuddy 或其他 Agent Skills 工具

选择“本地上传”或“安装 Skill”，上传整个文件夹或平台允许的 ZIP。核心文件必须保留名称：

`SKILL.md`

## 从 GitHub 安装

发布到 GitHub 后，使用工具提供的“从 GitHub 导入”，填写仓库地址。若平台不支持直接导入，请下载 ZIP 后本地上传。

## 能力差异

- 没有联网能力：只能解释用户上传的材料，不能声称已查最新信息；
- 没有图片识别：请用户改发股票名称或6位代码；
- 没有自动任务：只能在用户打开 Skill 时检查，不能后台提醒；
- 平台若跳过图片或文档，不影响核心 `SKILL.md` 运行。
