# 第 1 阶段 · 单元 2 教学证据

## 证据范围

- 日期：2026-09-23
- 当前轮次：单元 2 · 第 2 轮（value categories 与基础引用绑定）
- 来源：当前主教学聊天中的书面回答；尚无本单元编码提交、教师运行或 CI 运行。
- 帮助程度：学员在教师完成对应规则讲解后作答，属于“能解释／短复核”证据，不等于独立编码或迁移通过。

## 第 1 轮：scope、lifetime、dangling

学员对 5 组判断的核心结论均正确：

- 能区分内外层 block 中名字的 scope 与对象 lifetime。
- 能识别 dangling pointer / `std::string_view`：借用句柄本身可仍存活，而被借用对象／字符数据 lifetime 已结束。
- 能说明按值返回 owning `std::string` 的安全性不依赖返回局部对象引用。
- 能识别 shadowing 创建两个独立对象。

需要精确化的一点：

- 学员把 dangling pointer 解引用表述为“最后一行不合法”。教师纠正为：该表达式通常仍是 well-formed、可通过编译；在被指对象 lifetime 已结束后解引用会导致 undefined behavior。

状态：第 1 轮短复核通过。

## 第 2 轮：lvalue / xvalue / prvalue 与引用绑定

学员对 10 组判断的核心结论均正确：

- `x` 判断为 lvalue；
- 字面量 `10` 判断为 prvalue；
- `x + 1` 判断为 prvalue；
- `std::move(x)` 判断为 xvalue；
- `*p` 判断为 lvalue；
- 返回 `T` 的调用表达式判断为 prvalue；
- 返回 `T&` 的调用表达式判断为 lvalue；
- 返回 `T&&` 的调用表达式判断为 xvalue；
- 对 `int&& r = 5;` 后的命名表达式 `r` 判断为 lvalue；
- 能正确判断 `int& a = 5;` 不可绑定、`const int& b = 5;` 可绑定并延长该临时对象在此引用初始化场景中的 lifetime、`int&& c = x;` 不可直接绑定 lvalue `x`。

需要精确化的一点：

- 对命名 rvalue reference 的理由写成“prvalue 有身份后变成 lvalue”。教师纠正：`r` 的声明类型是 `int&&`，但**表达式 `r` 本身是 lvalue**；value category 属于表达式，不应描述为“原 prvalue 变成 lvalue”。`std::move(r)` 才把该表达式显式转换为 xvalue。

状态：第 2 轮短复核通过；value category 与声明类型的区分已有“能解释”证据。

## 当前状态

- 单元 2 第 1、2 轮短复核均通过。
- 下一步进入第 3 轮：常见隐式转换、conversion rank 与 overload resolution。
- 当前仍无单元 2 独立编码或迁移通过证据。
