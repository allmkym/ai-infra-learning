# 第 1 阶段 · 单元 1 教学证据

## 证据范围

- 日期：2026-09-23
- 来源：当前主教学聊天中的口头／书面回答；尚无本单元代码提交、教师运行或 CI 运行。
- 帮助程度：三轮判断题均在教师完成对应规则讲解之后作答，因此只能作为“能解释／短复核”证据，不能替代独立编码验收。

## 第 1 轮：初始化与 auto

已讲：初始化与赋值区别；copy/direct/list initialization；narrowing；`auto` 的静态推导；普通 `auto` 与花括号的常见差异。

学员 6 题回答的核心判断均正确：

- `int x = 3.14;` 判断为 copy-initialization，可编译；
- `int x{3.14};` 判断为列表初始化且因 narrowing 编译失败；教师补充精确分类为 direct-list-initialization；
- `const int n; auto x = n;` 判断 `x` 为 `int`；
- `const int n; auto& x = n;` 判断为 `const int&`，不可经引用修改；
- `auto x = {1}` 与 `auto y{1}` 分别判断为 initializer_list 与 int；教师补全为 `std::initializer_list<int>`；
- 能解释 vector 的括号与花括号初始化因构造函数重载／initializer_list 路径不同而得到不同结果。

状态：第 1 轮短复核通过；不代表单元通过。

## 第 2 轮：引用、const 与 auto&

已讲：引用别名与不可改绑；`const T&` 的只读访问路径；对象自身 const 与引用访问权限；普通 `auto`、`auto&`、`const auto&` 的对象／复制／修改差异；签名只能表达部分接口性质。

回答表现：

- 对按值与引用修改、`const auto&` 读取、range-for 的 `auto` / `auto&`、以及 const reference 参数的签名边界判断正确。
- 唯一明确错误：对
  `const int x = 10; auto& y = x;`
  将 `y` 写成 `int&`。教师已纠正：准确类型为 `const int&`；`auto&` 不会去掉被绑定对象的 const。
- 该纠正尚未通过新的独立同类题复核。

状态：已回答并完成讲解纠正；此点仍保留为待后续迁移确认，不记为独立通过。

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

状态：第 3 轮短复核通过；说明已能区分签名事实与需由实现／文档补充的前置条件、失败和 lifetime 契约。仍不等于单元独立实现通过。

## 当前结论与下一步

- 第 1～3 轮概念讲解已完成。
- 第 1、3 轮短复核通过。
- 第 2 轮有一次 const 推导错误，已讲解纠正，尚待后续迁移题再次独立确认。
- 单元 1 尚未通过：需要完成 `exercises/stage-01/unit-01/task.md` 的独立编码任务并接受代码、边界和语义验收。
