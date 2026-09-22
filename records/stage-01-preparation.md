# 第 1 阶段备课与来源核验

## 状态

- 阶段：1. 初始化、类型与接口契约
- 备课状态：阶段启动与单元 1 已完成来源核验；后续单元在开讲前继续补读对应资料
- 语义基线：C++20
- 学习状态：本记录只证明教师备课，不代表学员已开始或通过第 1 阶段
- 更新日期：2026-09-22

## 实际读取的资料

| 资料 | 固定版本与直接入口 | 实际读取范围 | 用途与状态 |
| --- | --- | --- | --- |
| Stanford CS106L Spring 2026 官网 | [课程首页](https://web.stanford.edu/class/cs106l/)；[2026 Spring lectures 目录](https://web.stanford.edu/class/cs106l/lectures/) | 实际读取课程简介、Schedule、课件目录；确认 Lecture 2 为 Types & Structs，Lecture 3 为 Initialization & References | 固定课程骨架与学期版本 |
| CS106L 2026 Spring Lecture 2/3 PDF | [Types & Structs PDF](https://web.stanford.edu/class/cs106l/lectures/2026Spring-02-TypesAndStructs.pdf)；[Initialization & References PDF](https://web.stanford.edu/class/cs106l/lectures/2026Spring-03-InitializationAndReferences.pdf) | 已定位并尝试读取；网页工具分别因超时、文件过大未取得正文 | **未记为已读**；非阻塞缺口，工具允许时再补读 |
| Stanford 官方 lecture-code | [固定提交 4842b102…](https://github.com/cs106l/cs106l-lecture-code/commit/4842b10272b2349412398281177482c525c40315)；[lecture02/main.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture02/main.cpp)；[lecture03/initialization.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/initialization.cpp)；[references.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/references.cpp)；[const.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/const.cpp)；[Reactor.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/Reactor.cpp) | 实际读取 Lecture 2/3 README 和所列源码 | 2026 课程官方示例；部分文件故意包含编译错误，见下方勘误／使用说明 |
| Stanford 官方 textbook | [固定提交 a34f13c…](https://github.com/cs106l/textbook/commit/a34f13c879b34c4dbe95434273cefc378a1d8444)；[README](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/README.md)；[Types and Structs](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/src/02-cpp-fundamentals/02-types-and-structs.md)；[Initialization and References](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/src/02-cpp-fundamentals/03-initialization-and-references.md) | 完整读取 README 与两章正文 | Stanford 官方补充教材；README 明示仍为 WIP，具体错误按下方勘误处理 |
| C++20 公开工作草案 N4861 | [initialization 分类](https://timsong-cpp.github.io/cppwp/n4861/dcl.init#15)；[list-initialization](https://timsong-cpp.github.io/cppwp/n4861/dcl.init.list)；[auto deduction](https://timsong-cpp.github.io/cppwp/n4861/dcl.type.auto.deduct)；[reference initialization](https://timsong-cpp.github.io/cppwp/n4861/dcl.init.ref)；[references](https://timsong-cpp.github.io/cppwp/n4861/dcl.ref)；[cv qualifiers](https://timsong-cpp.github.io/cppwp/n4861/basic.type.qualifier) | 实际读取当前单元相关规则与示例 | 核验初始化分类、narrowing、auto、引用绑定与 const/cv；细节以此类版本匹配的规范文本为准 |
| C++ Core Guidelines | [Interfaces](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-interfaces)；[Functions](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-functions) | 实际读取 I.1/I.5/I.7/I.11、F.15-F.17 及相关 ownership 说明 | 支撑接口契约、前置／后置条件和参数传递的工程补充；不是语言标准 |

## 来源勘误与教学取舍

| 来源中的表述／示例 | 本课程采用的说明 |
| --- | --- |
| textbook 的 Initialization and References 把 `int x = 1` 与 `int x(1)` 都归为 direct initialization | 按 C++20 N4861 [dcl.init]：`int x = 1` 是 copy-initialization；`int x(1)` 是 direct-initialization。花括号还需区分 direct-list-initialization 与 copy-list-initialization。 |
| textbook 把 `std::string` 与 `int`、`double`、`bool` 一起称为 built-in types | `std::string` 是标准库提供的字符串类类型（`std::basic_string<char>` 的别名），不是 C++ 内置类型。教学时不沿用该分类。 |
| textbook 的 `solveQuadratic` 声明返回 `std::pair<bool, std::pair<double,double>>`，但解释 `auto soln = solveQuadratic(...)` 时又称其等同于显式写 `std::optional<...>` | 以实际声明为准：该表达式中的 `auto` 推导为声明的嵌套 `pair` 返回类型。教材关于 `optional` 的旁注可视为设计建议，但不能改变现有函数声明的推导结果。 |
| lecture-code 目录中的示例文件 | 不假定所有文件可独立成功编译。`lecture03/initialization.cpp` 故意展示 list-initialization narrowing；`references.cpp` 在 `WITH_REF=1` 时的 `squareN(5)` 不能绑定到 `int&`；`const.cpp` 故意对 const vector / const reference 调用修改操作。教学时明确标注“预期编译失败”的行及其教学目的。 |

## 阶段单元安排

| 单元 | 目标 | 主要来源 | 计划验收 |
| --- | --- | --- | --- |
| 1. 初始化、auto、引用、const 与基础接口契约 | 区分初始化形式；精确判断 auto/引用/const 推导；区分新对象、底层数据复制和资源所有权；从签名与文档形成基础契约 | CS106L Lecture 2/3 官方示例与 textbook（按勘误使用）；N4861；Core Guidelines | 少量类型／初始化判断 + 一个独立小实现，解释输入、修改、ownership、失败与边界 |
| 2. 作用域、生命周期、基础值类别与转换 | 判断对象／引用何时有效；识别常见 dangling；理解基础 lvalue/rvalue、隐式转换及重载选择边界 | 开讲前补读对应 CS106L 资料；必要时核对 N4861 | 生命周期与转换反例 + 小型修复／需求变更 |
| 3. API 阅读与阶段整合 | 把参数传递、返回值、失败语义和头文件／API 查询结合到真实小模块 | CS106L 对应资料 + 标准库参考 + Core Guidelines | 独立实现或需求变更、边界验证、关键语义解释；满足阶段验收要求 |

## 已核验的单元 1 语义要点

- list-initialization 不是“任何时候都与括号初始化等价”；类类型的 initializer-list 构造函数在 list-initialization 中有特殊优先级，且 narrowing conversion 会使程序 ill-formed。
- C++20 的 auto 按 placeholder type deduction 规则推导；copy-list-initialization 与 direct-list-initialization 的推导不同，例如 `auto x = {1}` 与 `auto x{1}`。
- 引用必须按规则绑定；引用初始化后不能改为引用另一对象。是否可经引用修改对象取决于所引用类型的 cv 限定，而不是“有 & 就可写”。
- const/cv 要精确区分对象本身的限定与复合类型中的限定，不能把“引用是 const”作为独立顶层 cv 的直觉规则。
- 接口契约不只来自函数签名；签名可表达绑定和部分修改权限，但前置条件、失败语义、ownership、aliasing、lifetime 等需要实现或文档补充。

## 当前缺口与使用边界

- 2026 Spring Lecture 2/3 PDF 正文尚未成功读取，因此不得声称已读这些幻灯片或引用具体页码。
- textbook 固定提交日期为 2025-04-30，且 README 明示仍在 WIP；不视为 2026 Spring 幻灯片的替代版本。使用时遵守本记录中的具体勘误。
- 单元 2、3 的具体 CS106L 原始资料尚未全部读取；在相应单元开讲前补读并更新本文件。
- 教师自编例题／练习可以结合学员诊断调整；不得把自编内容表述成 CS106L 原题或课程结论。
