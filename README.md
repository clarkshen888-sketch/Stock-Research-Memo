# Stock Research Memo

可迁移的股票研究工作流与 GitHub Pages 报告库。

## 在新 Mac 上恢复

    git clone https://github.com/clarkshen888-sketch/Stock-Research-Memo.git
    cd Stock-Research-Memo
    python3 scripts/validate_reports.py

让 Codex 打开此目录并读取根目录 AGENTS.md。研究方法、HTML 规范和发布检查清单位于 workflow/。

Obsidian 保存个人长期背景和投资知识索引；本仓库保存可执行的研报规则与公开 HTML。不要把密码、API Key、账户信息或精确资产数据提交到公开仓库。

## 目录

- reports/：公司 HTML 研报
- workflow/：研究方法、页面规范和检查清单
- scripts/：本地验证工具
- index.html：GitHub Pages 首页
- Investing_Glossary.html：投资概念速查

## 发布流程

1. 按 AGENTS.md 与 workflow/ 生成报告。
2. 保存为 reports/SYMBOL_Research_YYYYMMDD.html。
3. 更新 index.html。
4. 运行 python3 scripts/validate_reports.py。
5. 检查 Git diff，再提交并推送。
