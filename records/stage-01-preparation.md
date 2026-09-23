# 第 1 阶段备课与来源核验

## 状态

- 阶段：1. 初始化、类型与接口契约
- 备课状态：阶段启动、单元 1 与单元 2 已完成开讲所需来源核验；单元 3 在开讲前继续补读对应资料
- 语义基线：C++20
- 学习状态：本记录只证明教师备课，不代表学员已通过相应单元
- 更新日期：2026-09-23

## 实际读取的资料

| 资料 | 固定版本与直接入口 | 实际读取范围 | 用途与状态 |
| --- | --- | --- | --- |
| Stanford CS106L Spring 2026 官网 | [课程首页](https://web.stanford.edu/class/cs106l/)；[2026 Spring lectures 目录](https://web.stanford.edu/class/cs106l/lectures/) | 实际读取课程简介、Schedule、课件目录；确认 Lecture 2 为 Types & Structs，Lecture 3 为 Initialization & References | 固定课程骨架与学期版本 |
| CS106L 2026 Spring Lecture 2/3 仓库副本 | [备用入口](../materials/cs106l/2026-spring/README.md) | 单元 1 已读取相应提取文本与示例；单元 2 进一步读取 Lecture 2 PDF 第 44–47 页文本层、Lecture 3 第 33–55 页提取文本，并直接视觉核对 Lecture 3 PDF 第 40、41、42、55 页页面图 | Lecture 2 用于基础转换／重载示例；Lecture 3 用于 value/reference 与 lvalue/rvalue 入口。未把机器提取等同全文已读 |
| Stanford 官方 lecture-code | [固定提交 4842b102…](https://github.com/cs106l/cs106l-lecture-code/commit/4842b10272b2349412398281177482c525c40315)；[lecture02/main.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture02/main.cpp)；[lecture03/initialization.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/initialization.cpp)；[references.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/references.cpp)；[const.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/const.cpp)；[Reactor.cpp](https://github.com/cs106l/cs106l-lecture-code/blob/4842b10272b2349412398281177482c525c40315/lecture03/Reactor.cpp) | 实际读取 Lecture 2/3 README 和所列源码 | 2026 课程官方示例；部分文件故意包含编译错误，见下方勘误／使用说明 |
| Stanford 官方 textbook | [固定提交 a34f13c…](https://github.com/cs106l/textbook/commit/a34f13c879b34c4dbe95434273cefc378a1d8444)；[Types and Structs](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/src/02-cpp-fundamentals/02-types-and-structs.md)；[Initialization and References](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/src/02-cpp-fundamentals/03-initialization-and-references.md)；[Pointers and Memory](https://github.com/cs106l/textbook/blob/a34f13c879b34c4dbe95434273cefc378a1d8444/src/02-cpp-fundamentals/05-pointers-and-memory.md) | 单元 1 完整读取前两章相关正文；单元 2 读取 Pointers and Memory 的 stack/local lifetime 说明及 references 关系相关段落 | 用作教学组织和直觉说明；README 明示教材 WIP，语言细节继续按 N4861 核验 |
| C++20 公开工作草案 N4861 | [scope](https://timsong-cpp.github.io/cppwp/n4861/basic.scope)；[lifetime](https://timsong-cpp.github.io/cppwp/n4861/basic.life)；[value categories](https://timsong-cpp.github.io/cppwp/n4861/basic.lval)；[reference initialization](https://timsong-cpp.github.io/cppwp/n4861/dcl.init.ref)；[lvalue-to-rvalue](https://timsong-cpp.github.io/cppwp/n4861/conv.lval)；[floating-integral conversions](https://timsong-cpp.github.io/cppwp/n4861/conv.fpint)；[overload conversion ranking](https://timsong-cpp.github.io/cppwp/n4861/over.ics.rank) | 单元 2 实际读取 block scope、lifetime 起止基本规则、value category taxonomy、reference binding 主要分支、lvalue-to-rvalue、浮点/整数转换及 Exact Match > Promotion > Conversion 的重载排序规则 | 单元 2 的语言语义基准 |
| C++ Core Guidelines | [Interfaces](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-interfaces)；[Functions](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-functions) | 实际读取 I.1/I.5/I.7/I.11、F.15-F.17 及相关 ownership 说明 | 支撑接口契约、前置／后置条件和参数传递；不是语言标准 |

## 来源勘误与教学取舍

| 来源中的表述／示例 | 本课程采用的说明 |
| --- | --- |
| textbook 的 Initialization and References 把 `int x = 1` 与 `int x(1)` 都归为 direct initialization | 按 C++20 N4861 [dcl.init]：前者是 copy-initialization，后者是 direct-initialization；花括号还需区分 direct-list 与 copy-list。 |
| textbook 把 `std::string` 与 `int`、`double`、`bool` 一起称为 built-in types | `std::string` 是标准库类类型，不是 C++ 内置类型。 |
| textbook 的 `solveQuadratic` 声明返回嵌套 `pair`，但解释 `auto` 时又称等同 `optional` | 以实际声明为准：该处 `auto` 推导为嵌套 `pair`；`optional` 只能视为设计建议。 |
| lecture-code 目录中的示例文件 | 不假定所有文件可独立成功编译。`initialization.cpp`、`references.cpp`、`const.cpp` 均包含教学用预期失败路径。 |
| Lecture 3 第 40 页把 lvalue/rvalue 解释成“赋值号左／右”和“有地址／临时无地址” | 只作为历史直觉入口。C++20 中 value category 是**表达式**的属性；基本分类是 lvalue、xvalue、prvalue，rvalue = prvalue 或 xvalue。不能用“是否在等号左边”或“是否有地址”作为完整定义。 |
| Lecture 3 第 41、55 页称引用必须绑定 lvalue／“You can only reference L-values” | 只对常见的非 const lvalue reference 示例有帮助，不能当完整规则。`T&` 通常不能绑定普通 rvalue，但 `const T&` 可以绑定许多 rvalue，且 C++ 还有 `T&&`。引用绑定按 N4861 [dcl.init.ref] 判断。 |
| textbook 用 stack frame 解释“局部变量 lifetime 随函数结束” | 对普通函数局部自动对象是有效直觉，但 scope、storage duration、object lifetime 是不同概念；教学中不把“在不在栈上”当成一般 lifetime 规则。 |

## 阶段单元安排

| 单元 | 目标 | 主要来源 | 计划验收 |
| --- | --- | --- | --- |
| 1. 初始化、auto、引用、const 与基础接口契约 | 区分初始化形式；精确判断 auto/引用/const 推导；区分新对象、底层数据复制和资源所有权；从签名与文档形成基础契约 | CS106L Lecture 2/3 官方示例与 textbook（按勘误使用）；N4861；Core Guidelines | 少量类型／初始化判断 + 一个独立小实现，解释输入、修改、ownership、失败与边界 |
| 2. 作用域、生命周期、基础值类别与转换 | 判断名称可见范围与对象 lifetime；识别常见 dangling；理解基础 lvalue/xvalue/prvalue；理解常见隐式转换及重载选择边界 | CS106L Lecture 2 pp.44–47、Lecture 3 pp.38–42/55（按勘误使用）；textbook memory 相关段落；N4861 | 生命周期与值类别反例 + 转换/重载判断 + 小型修复或需求变更 |
| 3. API 阅读与阶段整合 | 把参数传递、返回值、失败语义和头文件／API 查询结合到真实小模块 | 开讲前补读对应资料 | 独立实现或需求变更、边界验证、关键语义解释；满足阶段验收要求 |

## 已核验的单元 1 语义要点

- list-initialization 与括号初始化不等价；initializer-list 构造函数有特殊重载选择规则，narrowing 可使程序 ill-formed。
- C++20 的 `auto` 按 placeholder type deduction 规则推导；`auto x = {1}` 与 `auto x{1}` 不同。
- 引用初始化后不能改绑；能否经引用修改对象取决于被引用类型的 cv 限定。
- 完整接口契约还需说明前置条件、失败、ownership、aliasing、lifetime 等。

## 已核验的单元 2 语义要点

- scope 主要讨论“名字在哪里可见”；object lifetime 是对象／引用的运行时属性，两者不能混为一谈。block-scope 名字通常从声明点到 block 末尾可见。
- 对象 lifetime 一般在合适存储获得且初始化完成后开始；在销毁、析构开始或存储被释放／复用等情况下结束。lifetime 结束后的引用／指针即使仍保存某个地址，也不能按活对象随意使用。
- C++20 value category 分类表达式：lvalue、xvalue、prvalue 是三个互斥的基础分类；glvalue = lvalue 或 xvalue，rvalue = prvalue 或 xvalue。
- “lvalue 在等号左边、rvalue 在右边”只是历史命名直觉，不是判定规则。例如赋值表达式本身可产生 lvalue，很多 lvalue 也常出现在右侧。
- 非 const lvalue reference 与 const lvalue reference 的绑定能力不同；`const T&` 可绑定到某些 rvalue，并可能涉及 temporary materialization／lifetime extension。
- 常见隐式转换会参与表达式和函数调用；浮点转整数会截去小数部分，并存在表示范围边界。重载决议中标准转换序列一般按 Exact Match 优于 Promotion、Promotion 优于 Conversion 排序。

## 当前缺口与使用边界

- Lecture 5/11 已入库，但与当前单元 2 无关，本轮未把它们记为已阅读。
- Lecture 2 文本层可能遗漏截图／图示；单元 2 使用的第 44–47 页内容来自文本层，未声称视觉核对这些页。
- Lecture 3 为图片型；本轮已直接视觉核对第 40、41、42、55 页，其他相关页主要通过仓库 OCR 文本读取。精确代码／图示仍以原页为准。
- 单元 2 的 scope/lifetime 内容 CS106L 当前课件覆盖有限，因此明确使用 textbook 与 N4861 补充；这部分不是声称来自 Lecture 3。
- 单元 3 的具体 CS106L 原始资料尚未读取；在相应单元开讲前补读。
- 教师自编例题／练习可以结合学员表现调整；不得把自编内容表述成 CS106L 原题或课程结论。
