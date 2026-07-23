# 中文快速使用

`aaai-paper-architect` 用于 AAAI 论文的规划、重写、收紧和 revision package 重构。

它适合处理这几类问题：

- 叙事主线不清，贡献像并排罗列；
- 文字太防御、太模板化、太像自动生成；
- 主文信息不足，补充材料承担了太多审稿判断；
- 摘要、TL;DR、OpenReview 字段数字过密或结论过强；
- 现有实验结果已经冻结，希望优先复用而不是重跑。

## 建议输入

尽量提供以下材料中的相关部分：

- 主文入口文件，例如 `main.tex`
- 当前 build 目录或 PDF
- 补充材料入口文件，如果有
- 审稿意见、内部批注或 revision 目标
- 标题、摘要、关键词、TL;DR、OpenReview 文本，如果要一起改
- 页数约束，以及哪些实验结果已经冻结

## 推荐调用

```text
使用 $aaai-paper-architect 审阅这个 AAAI 论文目录。
先重建 identity sentence、贡献主线和 claim-evidence map，
再判断主文和补充材料的分配是否合理，
并修改摘要、TL;DR 和 OpenReview 文本。
如果现有实验结果和图表仍然有效，优先复用，不要重跑。
```

如果只想改局部，也可以直接限定范围，例如：

```text
使用 $aaai-paper-architect 只重写摘要和 introduction。
要求减少模板化表达，弱化超范围结论，并保持所有 claim 都能回指到现有证据。
```

## 输出预期

常见输出包括：

- 一句话论文定位和叙事主线
- 贡献点与证据映射
- 分节重写建议或直接改写文本
- 主文/补充材料迁移建议
- metadata 文本修改
- 剩余风险与证据边界

完整工作流以 [SKILL.md](../SKILL.md) 为准。
