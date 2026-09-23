# 第 1 阶段 · 单元 1 独立编码任务：Name Catalog

## 当前状态

- 2026-09-23：学员阅读任务后主动选择跳过，理由是自评已掌握本单元内容且认为该小任务收益较低。
- 本任务状态：**未完成／未验收／保留作后续补救任务**。
- 此次跳过不改变课程既定教学方式；后续编码任务仍正常布置。若后续综合任务暴露本单元相关缺口，可重新启用本任务。
- 学员的自评不自动记为“独立完成”“迁移通过”或正式验收。

## 目标

用一个很小的 C++20 程序同时验证本单元的四件事：

- 能区分按值对象、引用与 const 引用；
- 能正确使用 `auto` / `auto&` / `const auto&`；
- 能把“签名能表达的性质”和“额外接口契约”分开；
- 能明确说明输入、修改、失败、ownership、lifetime 与边界。

本任务要求学员独立实现。允许查 API 文档、课程资料和编译器诊断；查资料不降低独立性。如果教师提供关键实现、逐行修复或直接给出核心代码，应改记为“提示后完成”，不再记为独立完成。

## 文件

请提交：

- `exercises/stage-01/unit-01/main.cpp`
- `exercises/stage-01/unit-01/answers.md`

不要提交生成的二进制文件。

## 必须实现的接口

```cpp
const std::string& checked_name(
    const std::vector<std::string>& names,
    std::size_t index);

void append_suffix(
    std::vector<std::string>& names,
    std::string_view suffix);

std::vector<std::string> suffixed_copy(
    const std::vector<std::string>& names,
    std::string_view suffix);
```

### 1. checked_name

契约：

- 合法索引范围是 `[0, names.size())`。
- 合法索引时返回对应元素的 const 引用，不返回字符串副本。
- 越界时抛出 `std::out_of_range`。
- 返回引用不拥有字符串；调用者不得在源 vector / 对应元素失效后继续使用该引用。
- 空 vector 合法，但任何索引都越界。

### 2. append_suffix

契约：

- 给 `names` 中每个字符串追加 `suffix`。
- 必须修改调用者传入的 vector。
- 空 vector 合法。
- 空 suffix 合法，结果不变。
- 为避免本单元引入额外的失效分析，前置条件规定：`suffix` 不得引用 `names` 内任一字符串的字符存储。
- 循环变量必须使用引用形式（`auto&` 或显式 `std::string&`），不能靠“修改副本再写回”的方式规避本单元考点。

### 3. suffixed_copy

契约：

- 返回一个新的 owning `std::vector<std::string>`。
- 返回结果中的每个字符串都追加 `suffix`。
- 输入 `names` 必须保持不变。
- 空 vector 与空 suffix 都合法。
- 实现中请明确创建一个按值副本，再修改该副本；建议使用 `auto result = names;`，用于展示普通 `auto` 的按值语义。

## main 中至少覆盖的验证

请自己编写检查，至少覆盖：

1. `checked_name` 的合法索引；
2. `checked_name` 越界并确认抛出 `std::out_of_range`；
3. `append_suffix` 确实修改原 vector；
4. `append_suffix` 对空 vector 正常工作；
5. `suffixed_copy` 返回修改后的副本，同时原 vector 不变；
6. 空 suffix 的边界行为。

可以使用 `assert`、显式判断后返回非零状态，或你熟悉的其他轻量验证方式；不要求引入测试框架。

## answers.md

用自己的话简短回答：

1. 在 `auto result = names;` 中，新建了什么 C++ 对象？vector 的元素数据与原对象是什么关系？
2. 为什么 `for (auto& name : names)` 可以修改原 vector，而 `for (auto name : names)` 不能直接修改原元素？
3. 若写 `const auto& ref = checked_name(names, 0);`，`ref` 的准确类型是什么？
4. 对 `checked_name` 而言，哪些性质能从函数签名直接判断，哪些必须依赖本任务写出的契约？
5. 返回的 `const std::string&` 为什么不拥有字符串？调用者必须满足什么 lifetime 条件？

## 构建要求

以 C++20 编译，并至少开启：

```text
-Wall -Wextra -Wpedantic
```

编译器不限。提交时告诉教师你实际使用的编译命令和本地运行结果；在教师或 CI 实际运行前，这些仍记为“学员报告运行”。

## 验收

单元 1 不因“能编译”自动通过。验收同时检查：

- 三个接口是否符合上述契约；
- 边界与失败路径是否实际验证；
- 是否正确区分按值、引用和 const 引用；
- 是否能解释新对象、底层数据复制、ownership 与 lifetime；
- `answers.md` 是否把签名事实与额外契约区分清楚；
- 是否在未获得关键实现提示的情况下完成。

提交后将实际提交 SHA 发给教师；代码评估将绑定该 SHA。
