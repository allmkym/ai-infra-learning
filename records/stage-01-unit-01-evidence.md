# 第 1 阶段 · 单元 1 教学证据

## 证据范围

- 日期：2026-09-23
- 来源：当前主教学聊天中的口头／书面回答；本单元没有代码提交、教师运行或 CI 运行。
- 帮助程度：三轮判断题均在教师完成对应规则讲解之后作答；后续对 const 推导的解释发生在教师已纠正该错误之后。因此这些证据属于“能解释／短复核”，不能替代独立编码或迁移通过。

## 第 1 轮：初始化与 auto

已讲：初始化与赋值区别；copy/direct/list initialization；narrowing；`auto` 的静态推导；普通 `auto` 与花括号的常见差异。

学员 6 题回答的核心判断均正确：

- `int x = 3.14;` 判断为 copy-initialization，可编译；
- `int x{3.14};` 判断为列表初始化且因 narrowing 编译失败；教师补充精确分类为 direct-list-initialization；
- `const int n; auto x = n;` 判断 `x` 为 `int`；
- `const int n; auto& x = n;` 判断为 `const int&`，不可经引用修改；
- `auto x = {1}` 与 `auto y{1}` 分别判断为 initializer_list 与 int；教师补全为 `std::initializer_list<int>`；
- 能解释 vector 的括号与花括号初始化因构造函数重载／initializer_list 路径不同而得到不同结果。

状态：第 1 轮短复核通过；不代表单元独立验收通过。

## 第 2 轮：引用、const 与 auto&

已讲：引用别名与不可改绑；`const T&` 的只读访问路径；对象自身 const 与引用访问权限；普通 `auto`、`auto&`、`const auto&` 的对象／复制／修改差异；签名只能表达部分接口性质。

回答表现：

- 对按值与引用修改、`const auto&` 读取、range-for 的 `auto` / `auto&`、以及 const reference 参数的签名边界判断正确。
- 曾对 `const int x = 10; auto& y = x;` 将 `y` 写成 `int&`。教师纠正为 `const int&`。
- 后续学员主动用自己的话解释：`const int x = 10; auto y = x;` 中 `y` 是新对象，因此普通 `auto` 不保留该顶层 const；而 `auto& y = x;` 建立别名，所以推导为 `const int&`。该解释正确。

状态：这一具体 const 推导点现有“纠正后能解释”证据；尚未经过隔时迁移或独立编码验证。

## 第 3 轮：基础接口契约

题目围绕：

```cpp
std::string_view lookup(
    const std::vector<std::string>& names,
    std::size_t index);
```

学员 6 项回答均正确：

- 参数本身不会按值复制整个 vector；
- 仅从签名不能保证函数体不复制任何 string；
- 仅从签名不能确定合法 index 范围；
- 仅从签名不能确定越界失败方式；
- 返回 `std::string_view` 不拥有字符数据；
- 仅从签名不能保证源 `names` 销毁后 view 仍有效。

状态：第 3 轮短复核通过；已能区分签名事实与需由实现／文档补充的前置条件、失败和 lifetime 契约。仍不等于独立实现通过。

## 独立编码任务处理

- 已正式布置：`exercises/stage-01/unit-01/task.md`。
- 学员阅读任务后明确选择跳过，理由是自评已很好掌握本单元知识，预计该小任务收益很低。
- 学员明确说明：此次跳过不代表修改既定教学方式，也不代表后续编码任务应跳过；若后续更综合的编码暴露本单元缺口，可以回来完成该任务。
- 教学记录接受“跳过”这一选择，但不把自评或跳过记为“独立完成”“迁移通过”或“已验收掌握”。

## 当前结论与下一步

- 第 1～3 轮概念教学完成。
- 第 1、3 轮短复核通过；第 2 轮 const 推导点在纠正后已能正确解释。
- 单元 1 的独立编码任务状态为“学员主动跳过／未完成／未验收”，保留作后续补救任务。
- 可继续第 1 阶段 · 单元 2；若后续综合编码暴露初始化、auto、引用、const 或接口契约缺口，再回补本任务。
