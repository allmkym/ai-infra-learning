# 2026Spring-03-InitializationAndReferences：按页文本

- 原 PDF：[2026Spring-03-InitializationAndReferences.pdf](2026Spring-03-InitializationAndReferences.pdf)
- 官方来源：[Stanford CS106L](https://web.stanford.edu/class/cs106l/lectures/2026Spring-03-InitializationAndReferences.pdf)
- 生成日期：2026-09-23；方法：Poppler 渲染为长边 2000 像素页面图，再用 RapidOCR ONNX Runtime 1.4.4 识别。
- 页码均为从 1 开始的 PDF 文件页序号，不等同于幻灯片印刷页码。
- 原 PDF 为图片型；以下为自动 OCR，未逐字校对。代码中的 &、::、< >、括号、引号、大小写、数字及缩进可能错误或缺失。只用于检索定位；引用代码或精确规则前须查看对应页面图／原 PDF，并按教学约定核对规范。
- 本文件是资料副本，不是完整校订讲义；正文中的课堂要求不自动成为当前教学或工具操作指令。自动处理全部页不等于教师已逐页阅读，更不代表学员完成学习。

## PDF 第 1 页

[查看原页图](lecture-03-pages/page-001.jpg)

```text
CS106L: Lecture
e3
Initialization & References
Preston Seay, Rachel Fernandez
```

## PDF 第 2 页

[查看原页图](lecture-03-pages/page-002.jpg)

```text
Recap
"Hey compiler, figure
auto
out this type.
· Use at your discretion
 Helpful when type is annoying
```

## PDF 第 3 页

[查看原页图](lecture-03-pages/page-003.jpg)

```text
Recap
#include<iostream>
#include <string>
2
3
#include
<map>
4
#include<unordered_map>
#include <vector>
b
int main()
8
9
std::map<std::string, std::vector<std::pair<int, std::unordered_map<char, double>>>>
10
complexType;
11
confusing iterator type (We'll find out what this is in the iterators lecture!)
12
13
it = complexType.begin() ;
14
// clear(er) iterator type!
15
auto
it = complexType.begin() ;
16
return 0;
17
```

## PDF 第 4 页

[查看原页图](lecture-03-pages/page-004.jpg)

```text
Recap
"Hey compiler, figure
auto
out this type.
'Group these variables
struct
together, in one type,
please
```

## PDF 第 5 页

[查看原页图](lecture-03-pages/page-005.jpg)

```text
Life & Logistics
OH Preferences
口
https://forms.gle/JZ3kKbBKjS3ejq4N8
```

## PDF 第 6 页

[查看原页图](lecture-03-pages/page-006.jpg)

```text
Plan
1. Initialization
2. References
3. L-values vs R-values
4. const
5. Compiling C++ programs
```

## PDF 第 7 页

[查看原页图](lecture-03-pages/page-007.jpg)

```text
Initialization
C++ReferenceDefinition
Openinnewtab
What it is...
C++ReferenceDefinition
https://en.cppreference.com/w/cpp/language/initi
alization.html
'Provides initial values at
Scan the codeoropen the URL in a browser toview the
livepage.
the time of construction'
```

## PDF 第 8 页

[查看原页图](lecture-03-pages/page-008.jpg)

```text
Initialization
What it is...
How to...
'Provides initial
1. Direct initialization
values at the time
2. Uniform
of construction'
initialization
C+riiat.ir> Dirdina
```

## PDF 第 9 页

[查看原页图](lecture-03-pages/page-009.jpg)

```text
(1) Direct Initialization
Code
Console
CPP
Run
#include <iostream>
12.0 not an int...
int main() {
does this work?
int numOne = 12.0;
int numTwo(12.0);
std::cout << "numOne is: " << numOne << std::endl;
std::cout << "numTwo is: " << numTwo << std::endl;
YES
return 0;
```

## PDF 第 10 页

[查看原页图](lecture-03-pages/page-010.jpg)

```text
(1) Direct Initialization
Code
Console
CPP
Run
1
#include <iostream>
2
void checkCool(float temperature) {
3
4
if
(temperature > 100.0) {
std::cout << "Emergency cooling activated!" << std::endl;
else {
std::cout << "Temperature normal. No emergency cooling required.";
8
9
10
Critical? Yes
11
int main() {
12
float temperatureReading(100.8);
13
int temperature = temperatureReading;
14
checkCool(temperature) ;
15
return 0;
16
```

## PDF 第 11 页

[查看原页图](lecture-03-pages/page-011.jpg)

```text
(1) Direct Initialization
Code
Console
CPP
Run
1
#include <iostream>
2
void checkCool(float temperature) {
3
4
if
(temperature > 100.0) {
std::cout << "Emergency cooling activated!" << std::endl;
else {
std::cout << "Temperature normal. No emergency cooling required.";
8
9
C++ does not care
10
"You want 100.8 to be an
11
int main() {
integer? Okay
-compiler
12
float
temperatureReading(100.8);
13
int temperature = temperatureReading;
Narrowing Conversion
14
checkCool(temperature) ;
15
return 0;
16
```

## PDF 第 12 页

[查看原页图](lecture-03-pages/page-012.jpg)

```text
Initialization
What it is...
How to...
'Provides initial
1. Direct initialization
2. Uniform initialization
values at the time
3. Structured Binding
of construction'
```

## PDF 第 13 页

[查看原页图](lecture-03-pages/page-013.jpg)

```text
(2) Uniform Initialization
Notice the curlybrackets!
Code
Console
CPP
Run
#include <iostream>
12.0 not an int...
int main() {
does this work?
int numOne = {12.0};
int numTwo{12.0};
std::cout << "numOne is: " << numOne << std::endl;
std::cout << "numTwo is: " << numTwo << std::endl;
NO
return 0;
```

## PDF 第 14 页

[查看原页图](lecture-03-pages/page-014.jpg)

```text
(2) Uniform Initialization
Benefits:
1. Safe
No narrowing conversion.
2.Ubiquitous
Can use with vectors, maps, custom classes, etc.
```

## PDF 第 15 页

[查看原页图](lecture-03-pages/page-015.jpg)

```text
(2) Uniform Initialization
Code
Console
CPP
Run
#include <iostream>
#include <map>
3
int main(){
4
// Uniform initialization of a map.
5
std::map<std::string, int> ages{
{"Alice", 25},
{"Bob",30},
8
9
{"Charlie", 35}
10
};
11213 14
// Accessing map elements.
std::cout << "Alice's age:
" << ages["Alice"] << std::endl;
std::cout << "Bob's age: " << ages.at("Bob") << std::endl;
return 0;
15
```

## PDF 第 16 页

[查看原页图](lecture-03-pages/page-016.jpg)

```text
(2) Uniform Initialization
Code
Console
CPP
Run
#include <iostream>
#include <vector>
int main() {
3
// Uniform initialization of a vector.
std::vector<int> numbers{1, 2, 3, 4, 5};
5
Accessing
 vector elements.
for
(int num : numbers) {
8
std::cout << num <<
9
10
std::cout << std::endl;
11
return
：0
12
```

## PDF 第 17 页

[查看原页图](lecture-03-pages/page-017.jpg)

```text
Recall
StanfordID issueID() {
2
StanfordID id;
3
id.name = "THE Stanford Tree";
4
id.sunet = "theTREE";
id.idNumber = 0000002;
return id;
StanfordID issueID() {
1
StanfordID id = {"THE Stanford Tree", "theTREE", 0000002};
2
3
return id;
4
```

## PDF 第 18 页

[查看原页图](lecture-03-pages/page-018.jpg)

```text
Initialization
What it is...
How to...
'Provides initial
1. Direct initialization
values at the time
2. Uniform initialization
of construction'
3. Structured Binding
```

## PDF 第 19 页

[查看原页图](lecture-03-pages/page-019.jpg)

```text
(3) Structured Initialization
Initializes multiple variables from fixed-size
data structures.
Access multiple values returned by a function.
```

## PDF 第 20 页

[查看原页图](lecture-03-pages/page-020.jpg)

```text
(3) Structured Binding
Code
Console
CPP
Run
1
#include <iostream>
#include <tuple>
#include <string>
3
std::tuple<std::string, std::string, std::string> getclassInfo() {
std::string className = "CS106L";
std::string buildingName = "Thornton 110";
std::string language = "C++"
What do we call this?
return
{className, buildingName, language};
9
Uniforminitialization
10
11
What do we call this?
12
int main() {
Structured Binding
13
auto
[className, buildingName, language]
 = getClassInfo();
14
std::cout << "Come to "<< buildingName << "
and join us for " << className
15
<< " to learn " << language << "!" << std::endl;
16
return 0;
17
```

## PDF 第 21 页

[查看原页图](lecture-03-pages/page-021.jpg)

```text
(3) Structured Binding
auto classInfo = getClassInfo();
std::string className = std::get<0>(classInfo);
std::string buildingName = std::get<1>(classInfo);
std::string
 language = std::get<2>(classInfo);
auto [className, buildingName, language] = getClassInfo();
```

## PDF 第 22 页

[查看原页图](lecture-03-pages/page-022.jpg)

```text
(3) Structured Binding
Initializes multiple variables from fixed-size data
structures.
Access multiple values returned by a function.
Size must be known at compile time.
```

## PDF 第 23 页

[查看原页图](lecture-03-pages/page-023.jpg)

```text
Plan
1. Initialization
2. References
3. L-values vs R-values
4. const
5. Compiling C++ programs
```

## PDF 第 24 页

[查看原页图](lecture-03-pages/page-024.jpg)

```text
References
C++ReferenceDefinition
Qpen in new tab
What they are...
C++ReferenceDefinition
https://en.cppreference.com/w/cpp/language/ref
erence.html
Scan the code or open the URL ina browser toview the
'An alias to an
live page.
already-existing
object or function.
```

## PDF 第 25 页

[查看原页图](lecture-03-pages/page-025.jpg)

```text
References
What they are...
How to...
'An alias to an
&
already-existing
object or function.
```

## PDF 第 26 页

[查看原页图](lecture-03-pages/page-026.jpg)

```text
References
Example
Code
Console
CPP
Run
1
#include <iostream>
2
int main() {
3
int miToMoon = 238855; // That's how far the moon is.
pua::ps >> "'<eme tw, >> uoowoitu >>  st uoow. >> 4noo::ps
5
int& ISS = miToMoon;
ISS -= 254; // That's how high the ISS is.
X
9
10
std::cout << "ISS is " << ISS << "mi to moon." << std::endl;
11
std::cout << "Moon is " << miToMoon << "mi away." << std::endl;
12
return
0;
13
```

## PDF 第 27 页

[查看原页图](lecture-03-pages/page-027.jpg)

```text
References E
Example
Memory
miToMoon
238855
 1 int miToMoon = 238855;
 int& ISS = miToMoon;
3 ISS -= 254;
```

## PDF 第 28 页

[查看原页图](lecture-03-pages/page-028.jpg)

```text
References
Example
Memory
miToMoon
238855
1 int miToMoon = 238855;
 int& ISS = miToMoon;
3 ISS -= 254;
```

## PDF 第 29 页

[查看原页图](lecture-03-pages/page-029.jpg)

```text
References
Example
Memory
ISS / miToMoon
238855
1 int miToMoon = 238855;
 int& ISS = miToMoon;
3 ISS -= 254;
```

## PDF 第 30 页

[查看原页图](lecture-03-pages/page-030.jpg)

```text
References
Example
Memory
ISS / miToMoon
238601
 int miToMoon = 238855;
int& ISS = miToMoon;
 ISS -= 254;
3
```

## PDF 第 31 页

[查看原页图](lecture-03-pages/page-031.jpg)

```text
Pass by Reference
Code
Console
CPP
Run
Note the ampersand!
#include <iostream>
#include <math.h>
2
3
4
void squareN(int& n)
5
n = pow(n, 2);
6
n is a reference to num.
int main() {
8
int num = 5;
9
10
squareN(num) ;
11
std::cout << num << std::endl
So num gets updated to 25.
12
return
13
```

## PDF 第 32 页

[查看原页图](lecture-03-pages/page-032.jpg)

```text
Recall: Pass by Value
Code
Console
CPP
Run
#include <iostream>
#include <math.h>
2
3
4
void squareN(int n) {
5
n = pow(n, 2);
6
n is a copy of num.
int main() {
8
int num = 5;
9
10
squareN(num) ;
11
std::cout << num << std::endl
So num does not get updated.
12
return
13
```

## PDF 第 33 页

[查看原页图](lecture-03-pages/page-033.jpg)

```text
Recall: Pass by Value
Code
Console
CPP
Run
Memory
#include <iostream>
#include <math.h>
3
5
num
void squareN(int n) {
4
5
n=
pow(n，2):
25
6
7
int main(){
8
9
int num = 5;
10
squareN(num) ;
11
std::cout << num << std::endl;
12
return
:0
13
```

## PDF 第 34 页

[查看原页图](lecture-03-pages/page-034.jpg)

```text
Value
Reference
VS
void squareN(int n) {
1
1
void squareN(int&
}(u
2
n = pow(n, 2);
2
n = pow(n, 2);
3
3
7
Copies the variable!
Uses the same variable
(Can be expensive.)
& memory!
(Can modify it!)
```

## PDF 第 35 页

[查看原页图](lecture-03-pages/page-035.jpg)

```text
A Classic Reference
 Copy Bug
#include <iostream>
#include
<math.h>
Pass by Reference!
#include
<vector>
void shift(std::vector<std::pair<int, int>>
&nums) {
5
for
auto
[num1, num2]
nums
LOTS OFNOTHING DONE
num1++;
C
Structured Binding!
num2++;
8
9
Does not modify nums
TIMETO GOHOME
mgflip.com
```

## PDF 第 36 页

[查看原页图](lecture-03-pages/page-036.jpg)

```text
A Classic Reference
e Copy Bug
 #include <iostream>
#include <math.h>
#include <vector>
void shift(std::vector<std::pair<int, int>> &nums) 1
5
for
auto
[num1, num2
nums
num1++;
Each pair gets copied!
num2++;
8
9
```

## PDF 第 37 页

[查看原页图](lecture-03-pages/page-037.jpg)

```text
A Classic Reference
e Copy Bug
1 #include <iostream>
#include <math.h>
#include <vector>
void shift(std::vector<std::pair<int, int>> &nums) 1
5
for
(auto&
 num1, num2]
: nums
3
6
num1++;
Fixed!
num2++;
8
9
```

## PDF 第 38 页

[查看原页图](lecture-03-pages/page-038.jpg)

```text
Plan
1. Initialization
2. References
3. L-values vs R-values
4. const
5. Compiling C++ programs
```

## PDF 第 39 页

[查看原页图](lecture-03-pages/page-039.jpg)

```text
Yay or nay?
1 int
5;
X
"Variables" can
appear on left or right.
"Values" can appear
1 int
5
= x;
on the right.
"Values" cannot
1 int y
x;
apear on left.
```

## PDF 第 40 页

[查看原页图](lecture-03-pages/page-040.jpg)

```text
L-values & R-values
I-value
r-value
Full Name
Locator Value
Read Value
Where with respect
left or right
right
to equal sign?
Temporary value (No
Memory
Has a memory address
memory address)
int x = 10;
int x = 10;
Example
int y = x;
int y = x;
```

## PDF 第 41 页

[查看原页图](lecture-03-pages/page-041.jpg)

```text
L-values & R-values
Code
Console
CPP
Run
1
#include <iostream>
& / reference
#include <math.h>
L or R?
 note the ampersa
 Means it must be a
3
non-temporary value
4
void squareN(int& n) {
(an L-value).
calculates n to the power of 2
n = pow(n, 2);
int main(
3
So, we must
int num = 5;
10
squareN(num) ;
pass an L-value.
11
std::cout << num << std::endl;
12
return
13
```

## PDF 第 42 页

[查看原页图](lecture-03-pages/page-042.jpg)

```text
L-values & R-values
Code
Console
CPP
Run
#include <iostream>
2
 #include <math.h>
3
note the ampersay
4
void squareN(int& n) {
calculates n to the power of 2
n = pow(n, 2);
int main(
3
squareN(5);
10
return
0;
TAKE THEL
11
R
```

## PDF 第 43 页

[查看原页图](lecture-03-pages/page-043.jpg)

```text
Plan
1. Initialization
2. References
3. L-values vs R-values
4. const
5. Compiling C++ programs
```

## PDF 第 44 页

[查看原页图](lecture-03-pages/page-044.jpg)

```text
Const
C++ReferenceDefinition
Qpen in new tab
What it is...
C++ReferenceDefinition
https://en.cppreference.com/w/cpp/language/cv.
html
Scan the code or open the URL ina browser toview the
Such object cannot
live page.
be modified.
```

## PDF 第 45 页

[查看原页图](lecture-03-pages/page-045.jpg)

```text
Const & Reference
#include <iostream>
int main() {
4
std::vector<int> vec{ 1, 2, 3 };
const std::vector<int> const_vec{ 1, 2, 3 };
std::vector<int>& ref_vec{ vec };
const std::vector<int>& const_ref{ vec };
vec.push_back(3);<
10
const_vec.push_back(3) ;
11
ref_vec.push_back(3);
12
const_ref.push_back(3);
13
return 0;
14
```

## PDF 第 46 页

[查看原页图](lecture-03-pages/page-046.jpg)

```text
Const & Reference
Code
Console
CPP
Run
1 #include <iostream>
Z
int main() {
3
4
const int a = 5;
int& b = a;
b++;
std::cout << a << std::endl;
1
10
return
11
```

## PDF 第 47 页

[查看原页图](lecture-03-pages/page-047.jpg)

```text
Const & Reference
5
int
const
a
int& b
const
(compiler)
THAT IS NOT
ALLOWED
```

## PDF 第 48 页

[查看原页图](lecture-03-pages/page-048.jpg)

```text
Const & Reference
Code
Console
CPP
Run
1 #include <iostream>
Z
int main() {
3
4
const int a = 5;
const int& b = a;
/ /b++;
std::cout << a << std::endl;
10
return
11
```

## PDF 第 49 页

[查看原页图](lecture-03-pages/page-049.jpg)

```text
Plan
1. Initialization
2. References
3. L-values vs R-values
4. const
5. Compiling C++ programs
```

## PDF 第 50 页

[查看原页图](lecture-03-pages/page-050.jpg)

```text
Compiling
source.cpp
machine.exe
1
#include <iostream>
00110001
Compiling
2
int main(){
00110000
std::cout << "hello";
return
00110110
6
8
01101100
```

## PDF 第 51 页

[查看原页图](lecture-03-pages/page-051.jpg)

```text
Compiling
 C++ is compiled.
It cannot be "interpreted" or run as it is, like
Python.
 C++ needs a compiler.
· A program that converts it from source code.
 clang and g++ are popular.
How to compile:
We specify we want
We specify our input
g++ is our
c++ version 23.
file(s) are main.cpp
be named main.
compiler program.
```

## PDF 第 52 页

[查看原页图](lecture-03-pages/page-052.jpg)

```text
What you need to know...
main.cpp
main
#include <iostream>
00110001
2
3
int main() {
00110000
4
std::cout << "hello";
return 0;
00110110
Compile:
$ g++ --std=c++23
 main.cpp -o main
Run:
$./main
$.\main.exe
or on Windows:
```

## PDF 第 53 页

[查看原页图](lecture-03-pages/page-053.jpg)

```text
nVIDIA
CUDA
AOR
DEShaw&Co
CITADEL
DRIL
TWOSIGMA
Point72
```

## PDF 第 54 页

[查看原页图](lecture-03-pages/page-054.jpg)

```text
1F
TensorFlow
python
3.10|3.11|3.12|3.13
pypi package
2.21.0
DOI
10.5281/zenodo.4724125
openssfbestpractices
passing
openssf scorecard
oss-fuzz
build failing
oss-fuzz
build failing
custom badge
inaccessible
Contributor Covenant
v1.4adopted
Documentation
api
reference
TensorFlowisanend-to-endopensourceplatformformachinelearning.It hasacomprehensive,flexibleecosystemof
tools,libraries,andcommunityresourcesthatletsresearcherspushthestate-of-the-artinMLanddeveloperseasily
build and deploy ML-powered applications.
The TensorFlow Core is written largely in C++ and it is
composed of 2,0o0+ source files.
```

## PDF 第 55 页

[查看原页图](lecture-03-pages/page-055.jpg)

```text
Recap
1. Use uniform initialization!
2. References can alias variables
3. You can only reference L-values
4. const ensures you can't modify a variable
```
