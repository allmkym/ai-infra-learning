# 第 1 阶段备课与来源核验

## 状态

- 阶段：1. 初始化、类型与接口契约
- 备课状态：阶段启动与单元 1 已完成来源核验；后续单元在开讲前继续补读对应资料
- 语义基线：C++20
- 学习状态：本记录只证明教师备课，不代表学员已开始或通过第 1 阶段
- 更新日期：2026-09-22

## 实际读取的资料

| 资料 | 版本／位置 | 实际读取范围 | 用途与状态 |
| --- | --- | --- | --- |
| Stanford CS106L Spring 2026 官网与 lectures 目录 | https://web.stanford.edu/class/cs106l/ 与 /lectures/ | 实际读取课程简介、Schedule、2026 Spring 课件目录；确认 Lecture 2 为 Types & Structs，Lecture 3 为 Initialization & References | 固定课程骨架与学期版本 |
| CS106L 2026 Spring Lecture 2/3 PDF | 2026Spring-02-TypesAndStructs.pdf；2026Spring-03-InitializationAndReferences.pdf | 已定位并尝试读取；网页工具分别因超时、文件过大未取得正文 | **未记为已读**；属于非阻塞缺口，后续可在工具允许时补读 |
| Stanford 官方 cs106l-lecture-code | main @ 4842b10272b2349412398281177482c525c40315 | lecture02/README.md、lecture02/main.cpp；lecture03/README.md、initialization.cpp、references.cpp、const.cpp、Reactor.cpp | 2026 课程官方示例；覆盖类型、auto、窄化、引用、const 等示例 |
| Stanford 官方 cs106l/textbook | main @ a34f13c879b34c4dbe95434273cefc378a1d8444 | 完整读取 src/02-cpp-fundamentals/02-types-and-structs.md 与 03-initialization-and-references.md | 官方补充讲义；用于组织概念，但其中简化表述需由 C++20 规则复核 |
| C++20 公开工作草案 N4861 | timsong-cpp.github.io/cppwp/n4861 | [dcl.init.list]、[dcl.type.auto.deduct]、[dcl.init.ref]、[dcl.ref]、[basic.type.qualifier] 的相关规则与示例 | 核验 list-initialization、narrowing、auto、引用绑定与 const/cv 语义 |
| C++ Core Guidelines | isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines | Interfaces；I.1/I.5/I.7/I.11；Functions 的 F.15-F.17、相关 ownership 说明 | 支撑接口契约、前置／后置条件和参数传递的工程补充；不是语言标准 |

## 阶段单元安排

| 单元 | 目标 | 主要来源 | 计划验收 |
| --- | --- | --- | --- |
| 1. 初始化、auto、引用、const 与基础接口契约 | 区分初始化形式；精确判断 auto/引用/const 推导；区分新对象、底层数据复制和资源所有权；从签名与文档形成基础契约 | CS106L Lecture 2/3 官方示例与 textbook；N4861；Core Guidelines | 少量类型／初始化判断 + 一个独立小实现，解释输入、修改、ownership、失败与边界 |
| 2. 作用域、生命周期、基础值类别与转换 | 判断对象／引用何时有效；识别常见 dangling；理解基础 lvalue/rvalue、隐式转换及重载选择边界 | 开讲前补读对应 CS106L 资料；必要时核对 N4861 | 生命周期与转换反例 + 小型修复／需求变更 |
| 3. API 阅读与阶段整合 | 把参数传递、返回值、失败语义和头文件／API 查询结合到真实小模块 | CS106L 对应资料 + 标准库参考 + Core Guidelines | 独立实现或需求变更、边界验证、关键语义解释；满足阶段验收要求 |

## 已核验的单元 1 语义要点

- list-initialization 不是“任何时候都与括号初始化等价”；类类型的 initializer-list 构造函数在 list-initialization 中具有特殊优先级，且 narrowing conversion 会使程序 ill-formed。
- C++20 的 auto 按 placeholder type deduction 规则推导；copy-list-initialization 与 direct-list-initialization 的推导不同，例如 `auto x = {1}` 与 `auto x{1}`。
- 引用必须按规则绑定；引用初始化后不能改为引用另一对象。是否可经引用修改对象取决于所引用类型的 cv 限定，而不是“有 & 就可写”。
- const/cv 要精确区分对象本身的限定与复合类型中的限定，不能把“引用是 const”作为独立顶层 cv 的直觉规则。
- 接口契约不只来自函数签名；签名可表达绑定和部分修改权限，但前置条件、失败语义、ownership、aliasing、lifetime 等需要实现或文档补充。

## 当前缺口与使用边界

- 2026 Spring Lecture 2/3 PDF 正文尚未成功读取，因此不得声称已读这些幻灯片或引用其具体页码。
- 官方 textbook 当前 main 最后提交为 2025-04-30，不视为 2026 Spring 幻灯片的替代版本；它只作为 Stanford 官方补充资料。2026 学期骨架由官网目录和 2026 更新的官方 lecture-code 锚定。
- 单元 2、3 的具体 CS106L 原始资料尚未全部读取；在相应单元开讲前补读并更新本文件。
- 教师自编例题／练习可以结合学员诊断调整；不得把自编内容表述成 CS106L 原题或课程结论。
