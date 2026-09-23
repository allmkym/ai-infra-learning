# 第 1 阶段 · 单元 2 教学证据

## 证据范围

- 日期：2026-09-23
- 当前轮次：单元 2 · 第 1 轮（scope、lifetime、dangling）
- 来源：当前主教学聊天中的书面回答；尚无本单元编码提交、教师运行或 CI 运行。
- 帮助程度：学员在教师完成对应规则讲解后作答，属于“能解释／短复核”证据，不等于独立编码或迁移通过。

## 第 1 轮表现

学员对 5 组判断的核心结论均正确：

- 能区分内外层 block 中名字的 scope 与对象 lifetime：外层 `x` 仍可见且存活，内层 `y` 离开 block 后名字不可见且对象已析构。
- 对 dangling pointer 例子判断 `p` 自身仍活着、但所指对象已结束 lifetime，因此 `p` dangling。
- 对 `std::string_view` 例子判断 `v` 对象仍活着但借用已 dangling；局部 `std::string s` 已析构，其字符数据不能继续通过 view 使用。
- 对按值返回 `std::string` 能说明安全性的关键是返回 owning value，而非返回引用／地址；教师补充该安全性不依赖 NRVO。
- 对 shadowing 例子判断输出为 1，并正确指出创建了两个独立的 `int` 对象。

## 需要精确化的点

- 学员把 dangling pointer 解引用表述为“最后一行不合法”。教师纠正为：该表达式通常仍是 well-formed、可通过编译；在对象 lifetime 已结束后解引用 dangling pointer 会导致 undefined behavior。需继续保持“编译错误 / ill-formed”与“well-formed 但 UB”的区分。

## 当前状态

- 单元 2 第 1 轮短复核通过。
- scope 与 lifetime 的基本区分、dangling 的所有权／借用模型已有“能解释”证据。
- 下一步进入第 2 轮：C++20 value categories（lvalue / xvalue / prvalue）与基础引用绑定。
