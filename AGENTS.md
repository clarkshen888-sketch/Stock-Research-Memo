# Stock Research Memo instructions

默认使用中文协作。这个仓库是 Clark 的可迁移股票研究工作流与 GitHub Pages 站点。

生成或更新研报前，必须阅读：

1. workflow/RESEARCH_METHOD.md
2. workflow/HTML_REQUIREMENTS.md
3. workflow/REPORT_CHECKLIST.md

## 工作原则

- 先判断公司类型，再选择估值框架；不要把所有公司硬套 PE 或 SOTP。
- 财报、股本、现金、债务、指引和下一次财报日期优先使用公司 IR、SEC 或其他一手来源。
- 价格、政策和市场数据属于时点信息，生成报告时重新核验并标注适用日期。
- 明确区分事实、估算、推理和情景假设；不为凑结论虚构分部利润。
- 所有关键估值必须展示输入、公式和计算过程，不能只给黑箱目标价。
- 抄底区间只有在基本面未破坏、关键假设仍成立时有效。

## 文件与发布

- 公司报告统一保存为 reports/SYMBOL_Research_YYYYMMDD.html。
- 新报告必须加入根目录 index.html 的报告目录。
- 报告内返回首页使用 ../index.html。
- 新概念更新根目录 Investing_Glossary.html。
- 完成后运行 python3 scripts/validate_reports.py。
- 未经用户明确授权，不提交或推送。用户要求发布时，先说明验证结果，再提交并推送。
- 用户已明确要求发布时，只有远端分支确认包含本次提交才算完成；若推送失败或超时，必须检查网络、认证、权限和分支状态并继续重试，不得停留在本地提交状态。

## 输出标准

- 结论优先，但保留可追溯证据。
- 给出 Bear/Base/Bull 或与公司类型相符的情景分析。
- 写清催化剂、风险、跟踪指标和危险信号。
- 买入、持有、减仓区间用于仓位管理，不构成确定性收益承诺。
