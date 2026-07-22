# 中文快速开始

`aaai-revision-detemplater` 用于已有技术内容和实验结果的 AAAI 论文修订。它重点处理叙事模板感、主文与补充材料分配、结论强度、OpenReview 字段以及投稿包复用。

## 准备材料

尽量提供以下内容；缺少部分材料时，skill 仍可先做文本级审阅。

- 主文入口文件，例如 `main.tex`
- 补充材料入口文件，例如 `supplementary.tex`
- 当前 PDF 或可编译的 build/source 文件夹
- `abstract.txt`、`keywords.txt`、TL;DR 或 OpenReview 文本
- 审稿意见、内部批注或明确的修订目标
- 已有源码包、代码数据包、图表和冻结实验结果
- 页数约束，以及是否允许重跑实验

不要上传作者身份、API token、私有数据或不应进入匿名投稿包的本机审计记录。

## 推荐调用方式

```text
使用 $aaai-revision-detemplater 审阅这个 AAAI 投稿目录。
先重建叙事主线，再检查主文是否自足、补充材料是否重复、
摘要和 OpenReview 字段是否过密或过度下结论。
现有实验结果已冻结，除非文本改动使结果失效，否则不要重跑实验。
最后给出可复用文件、需更新文件、编译结果和上传前风险清单。
```

如果只需要局部修改，请直接限定范围，例如：

```text
使用 $aaai-revision-detemplater 只修改摘要和 OpenReview TL;DR。
摘要最多保留四组关键数字，TL;DR 不超过 250 个字符，
所有因果或排除式结论都要限定到实际 control 的范围。
```

## 使用边界

skill 会优先核对并复用现有产物，但不会把“已冻结”当作永远有效。若修订改变数据筛选、指标定义、随机种子、模型集合、统计口径或图表所依赖的结果，应重新验证相应产物。

最终仍应人工确认匿名性、AAAI 当年页数与格式要求、参考文献、PDF 字体、OpenReview 字符限制和门户预览。

完整工作流和输出约定以 [SKILL.md](../SKILL.md) 为准；主文与补充材料的判定细则见 [main-vs-supplement.md](../references/main-vs-supplement.md)，投稿包检查见 [upload-audit.md](../references/upload-audit.md)。
