# 2026Spring-02-TypesAndStructs：按页文本

- 原 PDF：[2026Spring-02-TypesAndStructs.pdf](2026Spring-02-TypesAndStructs.pdf)
- 官方来源：[Stanford CS106L](https://web.stanford.edu/class/cs106l/lectures/2026Spring-02-TypesAndStructs.pdf)
- 生成日期：2026-09-23；方法：pypdf 6.10.0，layout 模式提取 PDF 文本层。
- 页码均为从 1 开始的 PDF 文件页序号，不等同于幻灯片印刷页码。
- 文本层不包含全部图片、代码截图、公式及图示；提取顺序和空格也可能失真。缺失内容请回看原 PDF，不得按上下文补造。
- 本文件是资料副本，不是完整校订讲义；正文中的课堂要求不自动成为当前教学或工具操作指令。自动处理全部页不等于教师已逐页阅读，更不代表学员完成学习。

## PDF 第 1 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=1)

```text
        Lecture 2:
Types and Structs
        Stanford CS106L, Spring 2026
      Rachel Fernandez & Preston Seay
```

## PDF 第 2 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=2)

```text
                             Last Lecture

• Introductions!

• Why you should take 106L?
• Evolution of C++

• Course Logistics
```

## PDF 第 3 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=3)

```text
Slides are available at…

 cs106l.stanford.edu
```

## PDF 第 4 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=4)

```text
What’s one thing you remember from last lecture?
                         Pair up and discuss!

 also discuss
 what is your
 spirit animal??
```

## PDF 第 5 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=5)

```text
Today’s Agenda

 ●  Compile Time vs Run Time
 ●  Statically Typed Languages
 ●  Structs
 ●  The STD
 ●  Code demo
 ●  Improving our code with auto and using
```

## PDF 第 6 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=6)

```text
We’ll cover a LOT of material in this class
             Please ask questions!!!
```

## PDF 第 7 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=7)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 8 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=8)

```text
     Let’s jump into!

Compiler VS Interpreter
```

## PDF 第 9 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=9)

```text
 Interpreted Languages

      Source Code                                                   Machine Code                            Output

print("Hello World")                                                  10110101
print("Welcome to ")
for ch in "CS106L":                        Interpreter
    print(ch)
```

## PDF 第 10 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=10)

```text
 Interpreted Languages

      Source Code                                                   Machine Code                             Output

print("Hello World")                                                  10110101
print("Welcome to ")                                                  01011010
for ch in "CS106L":                         Interpreter
    print(ch)
```

## PDF 第 11 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=11)

```text
 Interpreted Languages

      Source Code                                                    Machine Code                            Output

print("Hello World")                                                  10110101
print("Welcome to ")                                                  01011010
for ch in "CS106L":                         Interpreter               10011101
     print(ch)
```

## PDF 第 12 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=12)

```text
 Interpreted Languages

      Source Code                                                     Machine Code                            Output

print("Hello World")                                                   10110101
print("Welcome to ")                                                   01011010
for ch in "CS106L":                         Interpreter                10011101
     print(ch)                                                         10110001
```

## PDF 第 13 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=13)

```text
 Interpreted Languages

     Source Code                                          Machine Code                       Output

print("Hello World")                                        10110101
print("Welcome to ")                                        01011010
for ch in "CS106L":                  Interpreter            10011101
    print(ch)                                               10110001

                                       🧠 THE BIG IDEA 🧠
                   The interpreted languages read each line of code
               line-by-line, translate each line, and then execute it
```

## PDF 第 14 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=14)

```text
Compiled Languages

              Source Code                                                                  Machine Code

std::cout << "Hello World" << std::endl;                                                      10110101
std::cout << "Welcome to " << std::endl;
for (char ch : "CS106L")                                                                      01011010
{                                                               Compiler                      10011101
     std::cout << ch << std::endl;                                                            10110001
}
```

## PDF 第 15 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=15)

```text
Compiled Languages

              Source Code                                                                   Machine Code                  Executable
                                                                                                                               File

std::cout << "Hello World" << std::endl;                                                      10110101
std::cout << "Welcome to " << std::endl;
for (char ch : "CS106L")                                                                      01011010
{                                                               Compiler                      10011101
     std::cout << ch << std::endl;                                                            10110001
}
```

## PDF 第 16 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=16)

```text
Compiled Languages

              Source Code                                                                  Machine Code                   Executable
                                                                                                                               File

std::cout << "Hello World" << std::endl;                                                      10110101
std::cout << "Welcome to " << std::endl;
for (char ch : "CS106L")                                                                      01011010
{                                                               Compiler                      10011101
     std::cout << ch << std::endl;                                                            10110001
}

                                     Executable                                 Output
                                          File
```

## PDF 第 17 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=17)

```text
Compiled Languages

                            🧠 THE BIG IDEA 🧠
        The compiler translates the ENTIRE program, packages it
               into an executable ﬁle, and then executes it
```

## PDF 第 18 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=18)

```text
Compiled Languages: Compile Time V.S. Run Time

                      🖥 Compile Time 🖥                                                        🏃 Run Time 🏃

                Source Code                                             Machine Code         Executable               Output
                                                                                                File

      std::cout << "Hello World" << std::endl;                           10110101
      std::cout << "Welcome to " << std::endl;
      for (char ch : "CS106L")                                           01011010
      {                                             Compiler             10011101
            std::cout << ch << std::endl;                                10110001
      }
```

## PDF 第 19 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=19)

```text
Interpreted Languages: Compile Time V.S. Run Time

                                           🏃 Run Time 🏃

               Source Code                                       Machine Code              Output

         print("Hello World")                                      10110101
         print("Welcome to ")                                      01011010
         for ch in "CS106L":                 Interpreter           10011101
              print(ch)                                            10110001
```

## PDF 第 20 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=20)

```text
Interpreted Languages: Compile Time V.S. Run Time

                                      🏃 Run Time 🏃

             Source Code                                  Machine Code           Output

        print("Hello World")                               10110101
        print("Welcome to ")                               01011010
        for ch in "CS106L":             Interpreter        10011101
            print(ch)                                      10110001

                                    🧠 THE BIG IDEA 🧠
                     Interpreted languages all run in run time!
        Compiled Languages run in ﬁrst compile time then run time
```

## PDF 第 21 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=21)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 22 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=22)

```text
C++ is a compiled language
```

## PDF 第 23 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=23)

```text
Q1: So we know the process of how C++ runs our
                        code…

        But when do we deal with errors?
```

## PDF 第 24 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=24)

```text
Python                                                                              C++

  print("Running...")                                                                 int main() {
  hello = "Hello ";                                                                         std::cout << "Running..." << std::endl;
  world = "World!";                                                                         std::string hello = "Hello ";
                                                                                            std::string world = "World!";
  print(hello * world)                                                                      std::cout << hello * world << std::endl;

                                                                                            return 0;
                                                                                      }

  $ python3 program.py                                                                $ g++ main.cpp

  Running...                                                                          error: no match for 'operator*' (operand types are
  TypeError: can't multiply sequence by                                               'std::string’ and ‘std::string’)
  non-int of type 'str'
```

## PDF 第 25 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=25)

```text
Python

 print("Running...")                                 10110101                     Running…
 hello = "Hello"                                     01011010
 world = "World!"                                    10011101
 print(hello * world)                                10110001
```

## PDF 第 26 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=26)

```text
Python

 print("Running...")                                 10110101                     Running…
 hello = "Hello"                                     01011010
 world = "World!"                                    10011101
 print(hello * world)                                10110001
```

## PDF 第 27 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=27)

```text
Python

 print("Running...")                                 10110101                     Running…
 hello = "Hello"                                     01011010
 world = "World!"                                    10011101
 print(hello * world)                                10110001
```

## PDF 第 28 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=28)

```text
Python

 print("Running...")                            10110101                 Running…
 hello = "Hello"                                01011010
 world = "World!"                               10011101
 print(hello * world)                           10110001                 TypeError:
                                                                         can’t
                                                                         multiply
                                                                         sequence
                                                                         by non-int
                                                                         of type
                                                                         ‘str’
```

## PDF 第 29 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=29)

```text
Python

 print("Running...")
 hello = "Hello ";
 world = "World!";
 print(hello * world)

                  Run Time Error

 $ python3 program.py

 Running...
 TypeError: can't multiply sequence by
 non-int of type 'str'
```

## PDF 第 30 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=30)

```text
                                              C++

Any guesses for when                            int main() {
this error occurs? Run                                std::cout << "Running..." << std::endl;
time or compile time?                                 std::string hello = "Hello ";

                                                      std::string world = "World!";
                                                      std::cout << hello * world << std::endl;
                                                      return 0;
                                                }

                                                $ g++ main.cpp
```

## PDF 第 31 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=31)

```text
                                                                C++
          🧠 THE BIG IDEA 🧠
                                                                  int main() {
       This error occurs during                                        std::cout << "Running..." << std::endl;
                                                                       std::string hello = "Hello ";
               compile time!                                           std::string world = "World!";
                                                                       std::cout << hello * world << std::endl;
                                                                       return 0;
When we are translating, we see                                   }
                                                                             Compile Time Error
     that we try to multiply two                                  $ g++ main.cpp
  strings and the compiler goes
                                                                  error: no match for 'operator*' (operand types are
      “hey that’s not allowed!!”                                  'std::string’ and ‘std::string’)
```

## PDF 第 32 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=32)

```text
Python                                                                        C++

  print("Running...")                                                           int main() {
  hello = "Hello ";                                                                   std::cout << "Running..." << std::endl;
  world = "World!";                                                                   std::string hello = "Hello ";
                                                                                      std::string world = "World!";
  print(hello * world)                                                                std::cout << hello * world << std::endl;

                                                                                      return 0;
                                                                                }
                    Run Time Error                                                            Compile Time Error

  $ python3 program.py                                                          $ g++ main.cpp

  Running...                                                                    error: no match for 'operator*' (operand types are
  TypeError: can't multiply sequence by                                         'std::string’ and ‘std::string’)
  non-int of type 'str'
```

## PDF 第 33 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=33)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 34 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=34)

```text
Types are super important!!
```

## PDF 第 35 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=35)

```text
Types
•  A type refers to the “category” of a variable
•  C++ comes with built-in types
    •  int            106
    •  double        71.4
    •  string        “Welcome to CS106L!”                            Hopefully this
                                                                    sounds familiar :D
    •  bool          true / false
    •  size_t        12               // Non-negative
```

## PDF 第 36 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=36)

```text
We know that the compiler checks for types before
              generating machine code.

                      This means…

         C++ is a statically typed language
```

## PDF 第 37 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=37)

```text
Dynamic Typing

Python (Dynamic Typing)

  a = 3
  b = "test"

  def foo(c):
      d = 106
      d = "hello world!"

The interpreter assigns variables a The interpreter assigns variables a type at type
runtime based on the variable’s value at at runtime based on the variable’s value
that timeat that time
```

## PDF 第 38 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=38)

```text
Dynamic Typing                                                                  Oh you are just switching
                                                                             things up with me! That’s okay!
Python (Dynamic Typing)                                                                 I’ll catch on!

  a = 3                                                                      So d was originally an integer,
                                                                                 and now it’s a string :D
  b = "test"
                                                                                       No problemo!
  def foo(c):
      d = 106
      d = "hello world!"

The interpreter assigns variables a The interpreter assigns variables a type at type
runtime based on the variable’s value at at runtime based on the variable’s value
that timeat that time
```

## PDF 第 39 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=39)

```text
Dynamic Typing                                              Static Typing

Python (Dynamic Typing)                                     C++ (Static Typing)

  a = 3                                                       int a = 3;
  b = "test"                                                  string b = "test";

  def foo(c):                                                 void foo(string c)
                                                              {
      d = 106                                                     int d = 106;
      d = "hello world!"                                          d = "hello world!"; ❌
                                                              }

The interpreter assigns variables a type                      •  Every variable must declare a type
at runtime based on the variable’s value                      •  Once declared, the type cannot change
at that time
```

## PDF 第 40 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=40)

```text
Why static typing?
• More eﬃcient
• Easier to understand and reason about
• Better error checking
```

## PDF 第 41 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=41)

```text
Better error checking

 def add_3(x):
     return x + 3

 add_3("CS106L") # Oops, that's a string. Runtime error!
```

## PDF 第 42 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=42)

```text
Better error checking

 def add_3(x):
      return x + 3

 add_3("CS106L") # Oops, that's a string. Runtime error!

 int add_3(int x) {
      return x + 3;
 }

 add_3("CS106L"); // Can't pass a string when int expected. Compile time error!
```

## PDF 第 43 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=43)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 44 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=44)

```text
Your turn 🫵🫵💪💪
 • TODO: Fill in the blanks underneath with the correct type
 • NOTE:    (int) x       casts   x to an int by dropping decimals
     •  E.g. (int) 5.7 = 5

 ______        a = “test”;
 ______        b = 3.2 * 5 - 1;
 ______      c = 5 / 2;
 ______      d(int foo) { return foo / 2; }
 ______        e(double foo) { return foo / 2; }
 ______        f(double foo) { return (int)(foo + 0.5); }
 ______        g(double c) { std::cout << c << std::endl; }
```

## PDF 第 45 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=45)

```text
Your turn

 ______std::string  a = “test”;
 ______double    b = 3.2 * 5 - 1;
 ______int   c = 5 / 2; // What does this equal?
 ______int   d(int foo) { return foo / 2; }
 ______double    e(double foo) { return foo / 2; }
 ______int    f(double foo) { return (int)(foo + 0.5); } // What's this?
 ______void        g(double c) { std::cout << c << std::endl; }
```

## PDF 第 46 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=46)

```text
Aside: Function Overloading

Deﬁning two functions with the same name but diﬀerent parameters

 double axolotl(int x) {            // (1)
     return (double) x + 3;         // typecast: int → double
 }

 double axolotl(double x) {         // (2)
     return x * 3;
 }

 axolotl(2);        // uses version ___, returns ______
 axolotl(2.0);   // uses version ___, returns ______
```

## PDF 第 47 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=47)

```text
Aside: Function Overloading

Deﬁning two functions with the same name but diﬀerent parameters

 double axolotl(int x) {              // (1)
     return (double) x + 3;           // typecast: int → double
 }

 double axolotl(double x) {           // (2)
     return x * 3;
 }
 axolotl(2);         // uses version ___(1) , returns ______               5.0
 axolotl(2.0);   // uses version ___(2) , returns ______               6.0
```

## PDF 第 48 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=48)

```text
C++ is a compiled, statically typed language
```

## PDF 第 49 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=49)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 50 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=50)

```text
Structs
```

## PDF 第 51 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=51)

```text
Keeping track of students
• Every student ID has a few properties
    • A name (string)
    • A SUNet (string)
    • An ID # (int)                     THE stanford tree
                                        0000000
```

## PDF 第 52 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=52)

```text
Okay let’s make generating IDs into a function!!

 return type issueNewID() {
    yada yada code yada yada

    return our ID stuff (ID #, name, sunet)
 }

this looks like the most legit function I’ve ever seen 😎😎 (jk..)
```

## PDF 第 53 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=53)

```text
A fundamental problem

 return type issueNewID() {
    // How can we return all three things?
    // What should our return type be? 😟😟

    // In Python this would look like…
    // return "Stanford Tree", "theTREE", 0000002
 }

How do we return more than one value? :OO
```

## PDF 第 54 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=54)

```text
Introducing… structs!
```

## PDF 第 55 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=55)

```text
Structs bundle data together

 struct StanfordID {
    string name;               // These are called fields
    string sunet;               // Each has a name and type
    int idNumber;
 };

 StanfordID id;                               // Initialize struct
 id.name = "THE Stanford Tree";         // Access field with ‘.’
 id.sunet = "theTREE";
 id.idNumber = 0000002;
```

## PDF 第 56 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=56)

```text
Returning multiple values

 StanfordID issueNewID() {
    StanfordID id;

                                                   THE stanford tree
    id.name = "THE Stanford Tree";                 0000000
    id.sunet = "theTREE";
    id.idNumber = 0000002;

    return id;
 }
```

## PDF 第 57 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=57)

```text
Uniform Initialization

 StanfordID id;
 id.name = "THE Stanford Tree";
 id.sunet = "theTREE";
 id.idNumber = 0000002;
```

## PDF 第 58 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=58)

```text
Uniform Initialization

 StanfordID id;
 id.name = "THE Stanford Tree";
 id.sunet = "theTREE";                                             We’ll learn more
                                                                 about this next time!
 id.idNumber = 0000002;

 // Order depends on field order in struct. ‘=‘ is optional
 StanfordID tree = { "THE Stanford Tree", "theTREE", 0000002 };
 StanfordID lelandjr { ”Leland Stanford Jr", ”thejunior", 5430282 };
```

## PDF 第 59 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=59)

```text
Using list initialization

 StanfordID issueNewID() {
     StanfordID id;
     id.name = "THE Stanford Tree";
     id.sunet = "theTREE";
     id.idNumber = 0000002;
     return id;
 }

 StanfordID issueNewID() {
     StanfordID id = { "THE Stanford Tree", "theTREE", 0000002 };
     return id;
 }
```

## PDF 第 60 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=60)

```text
                 🧠 THE BIG IDEA 🧠
A struct bundles named variables into a new type
```

## PDF 第 61 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=61)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 62 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=62)

```text
Many Possible Structs

 struct Name {
     string first;
     string last;
 };

 Name rf = { "Rachel", "Fernandez" };
```

## PDF 第 63 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=63)

```text
Many Possible Structs

 structstruct  NameName { {                                        struct Order {
      stringstring first; first;                                        string item;
      stringstring last; last;                                          int quantity;
 };};                                                              };

 NameName jrb  rf == {  { "Rachel"Rachel", ", "Fernandez"Fernandez" };" };Order dozen = { "Eggs", 12 };
```

## PDF 第 64 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=64)

```text
Many Possible Structs

 structstruct  NameName { {                                         struct Order {
      stringstring first; first;                                         string item;
      stringstring last; last;                                           int quantity;
 };};                                                               };

 NameName jrb  rf == {  { "Rachel"Rachel", ", "Fernandez"Fernandez" };" };Order dozen = { "Eggs", 12 };

 struct Point {
      double x;
      double y;
 };

 Point origin { 0.0, 0.0 };
```

## PDF 第 65 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=65)

```text
Many Possible Structs

 structstruct  NameName { {                                          struct Order {
      stringstring first; first;                                          string item;
      stringstring last; last;                                            int quantity;
 };};                                                                };

 NameName jrb  rf == {  { "Rachel"Rachel", ", "Fernandez"Fernandez" };" };Order dozen = { "Eggs", 12 };

 struct Point {                                                      struct Circle {
      double x;                                                           Point center;
      double y;                                                           double radius;
 };                                                                  };

 Point origin { 0.0, 0.0 };                                          Circle circle { {0, 0} , 50000000 };
```

## PDF 第 66 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=66)

```text
Many Possible Structs

 structstruct  NameName { {                                         struct Order {
      stringstring first; first;                                         string item;
      stringstring last; last;                                           int quantity;
 };};                                                               };

 NameName jrb  rf == {  { "Rachel"Rachel", ", "Fernandez"Fernandez" };" };Order dozen = { "Eggs", 12 };
                                                 Notice anything?

 struct Point {                                                     struct Circle {
      double x;                                                          Point center;
      double y;                                                          double radius;
 };                                                                 };

 Point origin { 0.0, 0.0 };                                         Circle circle { {0, 0} , 50000000 };
```

## PDF 第 67 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=67)

```text
Erm these all look a
     bit similar!!
```

## PDF 第 68 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=68)

```text
We can use std::pair!
```

## PDF 第 69 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=69)

```text
std::pair

 struct Order {
      std::string item;
      int quantity;
 };

 Order dozen = { "Eggs", 12 };
```

## PDF 第 70 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=70)

```text
std::pair

 struct Order {
      std::string item;
      int quantity;
 };

 Order dozen = { "Eggs", 12 };

 std::pair<std::string, int> dozen { "Eggs", 12 };
 std::string item = dozen.first;                                                  // "Eggs"
 int quantity = dozen.second;                                                   // 12
```

## PDF 第 71 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=71)

```text
          std::pair is a template
         (We’ll learn more about this later)

template <typename T1, typename T2>
struct pair {
   T1 first;
   T2 second;
};
std::pair<std::string, int>
```

## PDF 第 72 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=72)

```text
          std::pair is a template
          (We’ll learn more about this later)

struct pair {
   std::string first;
   int second;
};
```

## PDF 第 73 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=73)

```text
There’s something we need to discuss…
```

## PDF 第 74 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=74)

```text
What is an std !!? 🦠😷
```

## PDF 第 75 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=75)

```text
std ― The C++ Standard Library
• Built-in types, functions, and
  more provided by C++
• You need to #include the
  relevant ﬁle
    • #include <string> → std::string
    • #include <utility> → std::pair
    • #include <iostream> → std::cout,
      std::endl
```

## PDF 第 76 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=76)

```text
std ― The C++ Standard Library
•  Built-in types, functions, and more provided by C++
•  You need to #include the relevant ﬁle
    •  #include <string> → std::string
    •  #include <utility> → std::pair
    •  #include <iostream> → std::cout, std::endl
•  We preﬁx standard library names with std::
    •  If we write using namespace std; we don’t have to, but this is considered bad
       style as it can introduce ambiguity
        •  (What would happen if we deﬁned our own sort?)
```

## PDF 第 77 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=77)

```text
std ― The C++ Standard Library

     •  We preﬁx standard
        library names with std::
    •  If we write using
       namespace std; we don’t
       have to, but this is
       considered bad style as
       it can introduce
       ambiguity
        •  (What would happen if we
           deﬁned our own sort?)
```

## PDF 第 78 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=78)

```text
std ― The C++ Standard Library
• See the oﬃcial standard at cppreference.com!
• Avoid cplusplus.com…
   • It is outdated and ﬁlled with ads 😭
```

## PDF 第 79 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=79)

```text
To use std::pair, you must #include it

std::pair is deﬁned in a header ﬁle called utility

 #include <utility>

 // Now we can use `std::pair` in our code.

 std::pair<double, double> point { 1.0, 2.0 };
```

## PDF 第 80 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=80)

```text
                                                                  utility
What does #include do?
                                                                   namespace std {

 #include <utility>                                                     template
 std::pair<double, double> p { 1.0, 2.0 };                              <typename T1, typename T2>
                                                                        struct pair {
                                                                            T1 first;
                                                                            T2 second;
                                                                        };

                                                                        // Other utility code...
                                                                   }
```

## PDF 第 81 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=81)

```text
What does #include do?

 namespace std {

     template <typename T1, typename T2>
     struct pair {
          T1 first;
          T2 second;
     };

     // Other utility code...
 }

 std::pair<double, double> p { 1.0, 2.0 };
```

## PDF 第 82 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=82)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 83 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=83)

```text
Code Demo
```

## PDF 第 84 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=84)

```text
Solving a Quadratic Equation
```

## PDF 第 85 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=85)

```text
Solving a Quadratic Equation
```

## PDF 第 86 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=86)

```text
                   What are the solutions
                             (if any)?
Return Value

std::pair<bool, std::pair<double, double>> solveQuadratic(double a, double b, double c);

                                                                      Coefficients
     Is there a
     solution?
```

## PDF 第 87 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=87)

```text
std::pair<bool, std::pair<double, double>>

                  { true, { 1.0, 2.0 }}                               { false, doesnt_matter }
                                                                      e.g. { false, { 0.0, 0.0 }}
```

## PDF 第 88 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=88)

```text
Solving a Quadratic Equation
•

 std::pair<bool, std::pair<double, double>> solveQuadratic(double a, double b, double c);

📝 The sqrt function from the <cmath> header can calculate the square root
```

## PDF 第 89 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=89)

```text
Let’s code this together 👫

https://106b.vercel.app/rooms/cs106l
```

## PDF 第 90 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=90)

```text
Improving Our Code
```

## PDF 第 91 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=91)

```text
The using keyword
```

## PDF 第 92 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=92)

```text
The using keyword
•  Typing out long type names gets tiring
•  We can create type aliases with the using keyword

 std::pair<bool, std::pair<double, double>> solveQuadratic(double a, double b, double c);

 using Zeros = std::pair<double, double>;
 using Solution = std::pair<bool, Zeros>;
 Solution solveQuadratic(double a, double b, double c);
```

## PDF 第 93 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=93)

```text
using is kind of like a variable for types!
```

## PDF 第 94 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=94)

```text
The auto keyword
```

## PDF 第 95 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=95)

```text
The auto keyword
•  The auto keyword tells the compiler to infer the type

 std::pair<bool, std::pair<double, double>> result = solveQuadratic(a, b, c);

                                                                               The compiler checks for
                                                                               the declared return
 auto result = solveQuadratic(a, b, c);                                        type of solveQuadratic
                                                                               and ﬁlls it in for auto :O

 // This is exactly the same as the above!
 // result still has type std::pair<bool, std::pair<double, double>>
 // We just told the compiler to figure this out for us!
```

## PDF 第 96 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=96)

```text
   auto is still statically typed!

auto i = 1;   // int inferred
i = "hello!"; // ❌ Doesn't compile
```

## PDF 第 97 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=97)

```text
         Which one is clearer?

std::pair<bool, std::pair<double, double>> result = ...;
                     auto result = ...;
```

## PDF 第 98 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=98)

```text
Which one is clearer?

           auto i = 1;
            int i = 1;
```

## PDF 第 99 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=99)

```text
What questions do you have?

                bjarne_about_to_raise_hand
```

## PDF 第 100 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=100)

```text
Recap
```

## PDF 第 101 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=101)

```text
Recap
• C++ is a compiled, statically typed language
• Structs bundle data together into a single object
• std::pair is a general purpose struct with two ﬁelds
• #include from the C++ Standard Library to use built-in types
    • And use the std:: preﬁx too!
• Quality of life features to improve your code
    • using creates type aliases
    • auto infers the type of a variable
```

## PDF 第 102 页

[查看原 PDF](2026Spring-02-TypesAndStructs.pdf#page=102)

```text
See you all on Tuesday!! :)

Have a great weekend :D
```
