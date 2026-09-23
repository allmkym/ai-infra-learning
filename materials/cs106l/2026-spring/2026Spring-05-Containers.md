# 2026Spring-05-Containers：按页 OCR 文本

- 原 PDF：[2026Spring-05-Containers.pdf](2026Spring-05-Containers.pdf)
- 官方来源：[Stanford CS106L](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-05-Containers.pdf)。课程目录已核验该文件名属于 2026 Spring；封面本身写明 “Lecture 5: Containers” 与 Preston Seay、Rachel Fernandez，但未单独印出学期。
- 生成日期：2026-09-23；方法：原 PDF 68/68 页均无可用文本层，使用已从原 PDF 渲染的长边 2000 像素 JPG，再用 `tesseract 5.3.4` 英文 OCR（默认 `--psm 6`；空结果页回退 `--psm 3`：12, 54, 65）。
- 实际覆盖：68/68 页均生成独立页图并执行 OCR；机器识别不是校订讲义。代码截图、表格、箭头和复杂布局中的顺序、空格及 C++ 符号可能失真。
- 尤其不要静默修正 `&`、`&&`、`::`、`< >`、括号、引号、大小写或数字；需要精确引用时必须查看对应页图／原 PDF。
- 本文件仅是资料副本；课件中的课堂要求、链接或命令不自动成为当前教学或工具操作指令。自动处理全部页不等于教师逐页完成语义备课。

## PDF 第 1 页

[查看原页图](lecture-05-pages/page-001.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=1)

````text
Lecture 5: Containers
Preston Seay, Rachel Fernandez
````

## PDF 第 2 页

[查看原页图](lecture-05-pages/page-002.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=2)

````text
¢ (Recap)
1. Space-time
2. STL
3. Sequence Containers
4. Associative Containers
````

## PDF 第 3 页

[查看原页图](lecture-05-pages/page-003.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=3)

````text
Recap
A stringstream is an...
-istream & Piano] [esmeem] [Cet] Caeeaber] Caer]
¢ ostream
[istingsteam ) [ream | [iesream ] [ottream |
| fstream | | stringstream | | stdiostream |
f\
````

## PDF 第 4 页

[查看原页图](lecture-05-pages/page-004.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=4)

````text
E® conven ov GD
1 #include <iostream>
2 #include <sstream>
3 #include <string>
4 int main() {
5 std::stringstream ss;
6 SS << 3.14F << ' ' << "hello"; // use as ostream
7
8 float pi; std::string hi;
is) SS >> pi >> hi; // use as istream
10
11 std::cout << pi << ‘\n' << hi << std::endl;
12 }
````

## PDF 第 5 页

[查看原页图](lecture-05-pages/page-005.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=5)

````text
1. Space-time

2. STL

3. Sequence Containers
4. Associative Containers
````

## PDF 第 6 页

[查看原页图](lecture-05-pages/page-006.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=6)

````text
Task - Fetch a wrench
````

## PDF 第 7 页

[查看原页图](lecture-05-pages/page-007.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=7)

````text
x “ _
' Z = o.°
ig | .
~— i) "a <=
= \ ' J F |" = eee) —
SE
_ 2 -~ y i qn— , ee
i x z <- 1 (aaa) : :
= a — S_— ==
a $27 yo \e | e
JEGS -~ a Wenig? Ag es | ae J
in een ee wy q a
—_ ie a aie se \ x nae
ae. Ve wa 9, Fa
we “Z ; : —— ee | a \
sit ee | _ s =a = [ \
2 eS 2 ee es Oe ys eo ' Y \
A r yon = —T - -- . f val .
2 sea 2 Z << VE, : ~— 2 SS ‘ a -
Ki - i = pf ‘ ae a 4e3 ‘ee a} SS 2 a =
—_ — — 4 Bi > cL oN ~F “= a
—_ oF ee = Bo. Sa Af | = =
a we oe . eo * seen =
; Lt se Va 23 Cae SSS
a > fa re SS “Sas 3! \ =a =
| y @ «2 —— | MSL SS
````

## PDF 第 8 页

[查看原页图](lecture-05-pages/page-008.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=8)

````text
—~ = = ‘TTY ; Pons r aa =
>. ED ea A
a , =, | T—wm | if : |
3 hw - —-
_ Mae aoe ew SS Cs Url eee c& Ss | — ce sy bi
; - y a 4 T ' oa 1 T i » c 4 7, 18 i J
‘ina mormng nm) 4-14
Soke) = ton ig ag! 5 — Oe I r thal oe.
5 2 al 0") wir aw |
oo, 54) 1 awe a ,) - / —<,/\
f —= = iZ eo 1 eal Hl — ¢ Perel
a ee ae | if ce “Ty (| iY : \ , = beet
ears Fis é Nas = , a be \\ Jt $=
~~ ar... Site Maid 7 Ss ———t ; SE
13) Yes ~» ‘ea =, By fuss sa a. br 4 = F . s =
Thy | a
) am ae ee
4 ; :
````

## PDF 第 9 页

[查看原页图](lecture-05-pages/page-009.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=9)

````text
How much stuff?
````

## PDF 第 10 页

[查看原页图](lecture-05-pages/page-010.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=10)

````text
q _ a
e Zi =.
‘ ea /
= \ » \- \ = a -
2 =) me \ : ) vero a
} \ _ =!
—3 2 =| = i. vg i — eg
ee he ,
= - ot) ¢ “fe = \ A Be 4 = =
~ oars 4 — :) 4 i 1 es , P a rs — & q ; e
—— ia _ « ws, :
—— Lh He. : a . r
- a a : tad a . : ae
et | (ga ass a_i :
—» “ 7 7 36 rN ' “egg” Th F a
pe ~ - “ f pe ed = : 4 Ke i = =— \
ss 2 ¢ =n, oT ma ay —y q ” NV =
ZA z LE ~e eo SS a
PE Ss ' — » a i
=2 ’ og ” : - we. 7 ete, fete Se > : = .
. = / ty Mey 7. Wwe ~~
—s ; = : Von Le “ge Pan ~~ Boz IN
“ 7 Ap <. Led 43 P ; iS Se a Re - |. eee *
—— \ Ca . on 5
= - _ ‘ ~ : x ye
a a
````

## PDF 第 11 页

[查看原页图](lecture-05-pages/page-011.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=11)

````text
EE : — a
~_ = =
“] | cyl
a a 18 a ae K—} 1@ , Me =H
: : 2 —— i = =e a.
Iau Pas , ‘it
pee i g é |
````

## PDF 第 12 页

[查看原页图](lecture-05-pages/page-012.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=12)

````text
5 S dere = :

| "Space i is time.” -

, os - Bjarne Stroustrup 4
````

## PDF 第 13 页

[查看原页图](lecture-05-pages/page-013.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=13)

````text
Disorganized Organized
| I fia Lo
—__
> — Ne “ie .
Ry ————— sy
¢ Space efficient ¢ Space inefficient
¢ Slow to search ¢ Faster to search
e Ex: vector ¢ Ex: map
````

## PDF 第 14 页

[查看原页图](lecture-05-pages/page-014.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=14)

````text
1. Space-time

2. STL

3. Sequence Containers
4. Associative Containers
````

## PDF 第 15 页

[查看原页图](lecture-05-pages/page-015.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=15)

````text
¢ Assignment 1 is out, due this Friday!
¢ Office hours start this Thursday,
4:30-5:20pm in Thornton 210.
````

## PDF 第 16 页

[查看原页图](lecture-05-pages/page-016.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=16)

````text
1. Space-time

2. STL

3. Sequence Containers
4. Associative Containers
````

## PDF 第 17 页

[查看原页图](lecture-05-pages/page-017.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=17)

````text
Standard Template Library (STL)
How is this different from the standard library std?
C++ Standard Library
strings Standard Template
Library
````

## PDF 第 18 页

[查看原页图](lecture-05-pages/page-018.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=18)

````text
Standard Template Library (STL)
C++ Standard Library
Standard Template Library
````

## PDF 第 19 页

[查看原页图](lecture-05-pages/page-019.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=19)

````text
Standard Template Library (STL)
C++ Standard Library
Standard Template Library
—s
````

## PDF 第 20 页

[查看原页图](lecture-05-pages/page-020.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=20)

````text
Standard Template Library (STL)
e Made by Alexander Stepanov
Standard Template Library
* on t ES Se ee
ea #include <algorithm>
````

## PDF 第 21 页

[查看原页图](lecture-05-pages/page-021.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=21)

````text
1 class IntList { 1 class StringList { ‘ibleList f
2 p00 2 pac

3} 3 }3

4 4

5 int main() { 5 int main() { 1) {

6 | IntList ints( 6  StringList strs(); list dbls();

7 ints.add(10); 7 strs.add("1"); Id(1.0);

8 ints.add(2@) ; 8 strs.add("2"); Id(2.0);

o s)
10  assert(ints.g 10 £assert(strs.get(@) == "1"); dbls.get(@) == 1.0);
11 } 11 }

1 class FloatList {| 1 class BoolList { 1 class CharList {
2 500 7 boc 2 Soc

3 }3 ons San
````

## PDF 第 22 页

[查看原页图](lecture-05-pages/page-022.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=22)

````text
What does template mean?
il
template <typename T>
= class Vector<T> {
1 class IntList {
}3
. 1 #include <vector>
1 class DoubleList {
see = int main() {
}; std::vector<int> ints;
? std::vector<double> dbls;
. . std: :vector<std::string> strs;
1 class StringList { °
566 ints.push_back(1) ;

}: dbls.push_back(5.4);
strs.push_back 5
std::cout << ints[@] + dbls[0];

}
````

## PDF 第 23 页

[查看原页图](lecture-05-pages/page-023.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=23)

````text
1. Space-time

2. STL

3. Sequence Containers
4. Associative Containers
````

## PDF 第 24 页

[查看原页图](lecture-05-pages/page-024.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=24)

````text
Containers Reference Qpen in new tab

" ie: Containers Reference

Sequence containers [=] [=] https://en.cppreference.com/w/cpp/container.html

implement data structures cs an ‘ Scan the code or open the URL in a browser to view the live page.
which can be accessed 7"
sequentially." lo na Ha
In other words, they
contain sequences.
````

## PDF 第 25 页

[查看原页图](lecture-05-pages/page-025.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=25)

````text
Containers Reference Qpen in new tab
Containers Reference
opeo
‘ “a Fi a https://en.cppreference.com/w/cpp/container.html
“i . 5
is Phen
e r aa = = 5 3 Scan the code or open the URL in a browser to view the live page.
aces =
pe
co _ ba
=
eh
e Deque [al rer
L I t
````

## PDF 第 26 页

[查看原页图](lecture-05-pages/page-026.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=26)

````text
Vectors
Code Console cP t Run
1 #include < >
#include <ios >
"A resizable int main() {
‘ " std: :vector<int> vec ih, Qo By a He
contiguous array vec.push_back(5);
vec.push_back(6) ;
vec[1] = 20;
for (size t i = 03; i < vec.size(); i++
[sfelelatsle| nn
1
oO 1 2 3 4 5 }
````

## PDF 第 27 页

[查看原页图](lecture-05-pages/page-027.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=27)

````text
Vectors
Code Console cP t Run
1 #include < >
#include <ios >
"A resizable int main() {
‘ " std: :vector<int> vec ih, Qo By a He
contiguous array vec.push_back(5);
vec.push_back(6) ;
vec[1] = 20;
for (size t i = 03; i < vec.size(); i++
[+ [zo] s[s[s] «| nn
1
oO 1 2 3 4 5 }
````

## PDF 第 28 页

[查看原页图](lecture-05-pages/page-028.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=28)

````text
Index Checking?
Code Console P t Run
1 #include < >
#include <ic >
¢ Be careful with = WEB)
. . std: :vector<int> vec ih, Qo By a He
indices vec.push_back(5);
* [] doesn't check vec.push_back(6) ;
vec[1] = 20;
¢ .at() does
for (size t i = 03; i < 10; i++
std::cout << vec[i] << :
}
````

## PDF 第 29 页

[查看原页图](lecture-05-pages/page-029.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=29)

````text
1. You don't pay for what
you don't use. ESR EME) “oocsocn
2. What you do use is just Ed ete imteeche
as efficient as what you ee Sa Slenvinnertamaeenr aU Lincinetesnaereratnelermere
could reasonably write [At
by hand.
. eed eee
````

## PDF 第 30 页

[查看原页图](lecture-05-pages/page-030.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=30)

````text
Resizing vectors copies over the whole array into a bigger array - Dynamic reallocation Open in new tab
eco
=] a [ml Resizing vectors copies over the whole array into a bigger array - Dynamic reallocation
a he EI + (Im
" = Fr " https://web.stanford.edu/~pseay/cs106I/vectors
all =
big = 4 Scan the code or open the URL in a browser to view the live page.
Pe any
a | a |
ae a .
Lo . i
Oe
````

## PDF 第 31 页

[查看原页图](lecture-05-pages/page-031.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=31)

````text
106B vs. Standard Vectors
````

## PDF 第 32 页

[查看原页图](lecture-05-pages/page-032.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=32)

````text
Task: r
Write a C++ function to [a] Le , [=]
calculate the maximum qu x2 J
value of a vector, using he: k. ao
4 different vector a “awl t
methods. Oo oe
inetd 61OX5aeEnc
````

## PDF 第 33 页

[查看原页图](lecture-05-pages/page-033.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=33)

````text
Walkthrough
Code ) Console cPP [ Run J
1 #include <iostream>
#include <vector>
int findPeakHeat(const std::vector<int>& temps) {
/ Your implementation here
}
Q@ int main() {
} High temperatures torecast tor tne next 7 days ‘
std::vector<int> weeklyForecast = {82, 95, 102, 99, 88, 79, 81};
std::cout << "--- Weather Report ---" << std::endl;
std::cout << "Max temp this week will be " << findPeakHeat(weeklyForecast) <<
std::endl;
return Q;
t
````

## PDF 第 34 页

[查看原页图](lecture-05-pages/page-034.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=34)

````text
Inserting has to shift over elements Open in new tab
eee
F] = Inserting has to shift over elements

OER a

Ts Ay | | https://web.stanford.edu/~pseay/cs106l/vectors-insert

roi = aa Scan the code or open the URL in a browser to view the live page.

Poker aL

I =e eos

[ml L Ts
````

## PDF 第 35 页

[查看原页图](lecture-05-pages/page-035.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=35)

````text
Double-ended queue (pronounced "deck")
Like a vector, with: — was ra
* push_back _ ae Pot
But also has: mei aii Ge: <
¢ push_front ——-_ ~=—S
¢ pop_front 7 : —
````

## PDF 第 36 页

[查看原页图](lecture-05-pages/page-036.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=36)

````text
Deques
Ex: Maintaining a list of the last 10,000 prices
1 #include <deque>
void receivePrice(deque<double>& prices, double price)
{
prices.push_front(price) ;
if (prices.size() > 10000
prices.pop_back();
}
````

## PDF 第 37 页

[查看原页图](lecture-05-pages/page-037.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=37)

````text
How deques are stored behind the scenes Open in new tab
eoo
[=] Ls [ml How deques are stored behind the scenes

eh is a https://web.stanford.edu/~pseay/cs106I/deque
To,
| Pe a

nL hs Scan the code or open the URL in a browser to view the live page.
Sod — eet

lea 2

na oa 1

1

[=] aerd= “rl
````

## PDF 第 38 页

[查看原页图](lecture-05-pages/page-038.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=38)

````text
1. Space-time

2. STL

3. Sequence Containers

4. Associative Containers
````

## PDF 第 39 页

[查看原页图](lecture-05-pages/page-039.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=39)

````text
[=] Le [=] ee
" ° ° é ff a i Scan the code or open the URL in a browser to view the live page.
Associative containers 5
implement sorted data [a] ect
structures that can be
quickly searched."
````

## PDF 第 40 页

[查看原页图](lecture-05-pages/page-040.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=40)

````text
Maps
A map "eontains ae ie Se ee
key-value pairs rapa
with unique keys." .
Python calls them
"dictionaries"
````

## PDF 第 41 页

[查看原页图](lecture-05-pages/page-041.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=41)

````text
Maps
"Sequence Containers’ “Vectors & Deques"
{ Oo )e )
( WY Roast
" wae aD a, ~ Th oe "
Associative Containers) Te aps & Sets
Wr 4
a ( —e J
.
yu
````

## PDF 第 42 页

[查看原页图](lecture-05-pages/page-042.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=42)

````text
We can do this: How is it efficient?
1 std: :map< . + >e ads;
2 adjs[106] = "awesome";
3 adjs[103] = “mathy"; It sorts the
4 adjs[107] = "deep"; °
. pairs by
6 std::cout << adjs[106]; their keys
````

## PDF 第 43 页

[查看原页图](lecture-05-pages/page-043.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=43)

````text
E®) consote -
1 #include <map> A map is a collection of pairs,
2 #include <iostream> — sohere is uniform initialization of
3 int main () { Pou.
4 std::map<int, char> preston {
5 {16, 'p'}, {18, 'r'}, {5, ‘e'},
6 {195 S fot 20, ts toi 15o O poe, l4ee ny
743
8 for (const auto& pair : preston) { We loop over each pair.
9 std::cout << pair.first << ‘ '
10 << pair.second << std::endl;
11 } ——
12 } pairs are sorted by key.
````

## PDF 第 44 页

[查看原页图](lecture-05-pages/page-044.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=44)

````text
Maps
A std: :map<K,V> is a collection of std: :pair<const K, V>
Code Console c tT Run
1 for (const auto& pair : myMap) {
auto key = pair.first;
auto value = pair.second;
}
, Structured binding ©
Code Console PP T Run }
1 for (const auto& [key, value] : myMap) {
}
````

## PDF 第 45 页

[查看原页图](lecture-05-pages/page-045.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=45)

````text
Maps Storage - Red Black Trees
¢ Stores pairs in a binary
search tree (BST)
Oo} 47 =. [=] https://web.stanford.edu/~pseay/cs106I/maps-rbt
7 Specifically, it usesa TT : 1, Scan the code or open the URL in a browser to view the live page.
Red-Black Tree, . :
guaranteeing maximum if:
depth of 2 log (n) [m] i
. This makes search
O(log(n))
“SPEED: AM SPEED.
= SSP Saas
= ~ > My
````

## PDF 第 46 页

[查看原页图](lecture-05-pages/page-046.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=46)

````text
We can do this:
1 std::map<std::string, int> fav_num;
° fav_n ull Be Sroh = 2; "Ummmm.... we never defined that???"
4 std:: cout << "Presto ff fav_num "| <<
5 d Rache- is " << fav_num["Rachel"] << '\n';
The map automatically inserts (It actually does this every
the default value of the object. time, even on Line 2)
````

## PDF 第 47 页

[查看原页图](lecture-05-pages/page-047.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=47)

````text
Sets
Amoral maps ol E a= [=| [ml Sets visualizer
1" ate 7 https://web.stanford.edu/~pseay/cs106\I/sets-rbt
i . an Scan the code or open the URL in a browser to view the live page.
es . Srhe
ORs
Maps without values
Unique Objects
````

## PDF 第 48 页

[查看原页图](lecture-05-pages/page-048.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=48)

````text
Map Syntax

What you want to do? Stanford Map<char, int> std::map<char, int>
Create an empty map Map<char, int> m; std::map<char, int> m;

. : m.put(k, v); m.insert({k, v});
Add key k with value v into the map mk] = v: mik] = v:
Check if k is in the map ; : if (m.count(k))
(* C++20) IT ro cantainshey(K)) if (m.contains(k)) (*)
Check if the map is empty if (m.isEmpty()) if (m.empty())
Retrieve or overwrite value ae . co :
associated with key k wu iss de =r
rae Se i en ee m{k] = i; m{[k] = i;
(auto-insert default if doesn’t exist)
````

## PDF 第 49 页

[查看原页图](lecture-05-pages/page-049.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=49)

````text
Set Syntax
Stanford Set<char> std::set<char>
“eee ‘
Add k to the set s.add(k); s.insert(k);
Check if k is in the set : : if (s.count(k))
(* C++20) if (s.contains(k)) if (s.contains(k)) (*)
Check if the set is empty if (s.isEmpty()) if (s.empty())
````

## PDF 第 50 页

[查看原页图](lecture-05-pages/page-050.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=50)

````text
Practice
Task: "
Find the double agents -
those who are in multiple
departments. -
Oe.
|) line-id /AgIvoxQ8E
````

## PDF 第 51 页

[查看原页图](lecture-05-pages/page-051.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=51)

````text
Console CPP
1 #include <iostream> i
2 #include <vector>
3 #include <string>
4 #include <map>
5 #include <set>
)

7 std::set<std::string> findDoubleAgents(std::map<std::string, std::set<std::string>>
departments) {

8 std: :set<std::string> seen, doubleAgents;

2)

10 // Your code here

iat

12 return doubleAgents;

13 }

14

15 int main() {

16 std::map<std::string, std::set<std::string>> company = {
````

## PDF 第 52 页

[查看原页图](lecture-05-pages/page-052.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=52)

````text
Associative containers
Associative containers implement sorted data structures that can be quickly searched (O(log n) complexity).

collection of unique keys, sorted by keys

set
(class template)

— collection of key-value pairs, sorted by keys, keys are unique

P (class template)

watkient collection of keys, sorted by keys
(class template)

multimap collection of key-value pairs, sorted by keys
class template)
````

## PDF 第 53 页

[查看原页图](lecture-05-pages/page-053.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=53)

````text
"Wait... how do they get sorted?"
std:: Map
eiiada teliena This is how... they must be
enned In neader <map comparable, so it uses the "less
template< than" comparator by default.
class Key,
class T,
class Compare = std::less<Key>,
SS SS AIS SG EE SSS ES SE SES SE
> class map; "How do we make memory for it?”
````

## PDF 第 54 页

[查看原页图](lecture-05-pages/page-054.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=54)

````text
int, double, string

ifstream, Course |
````

## PDF 第 55 页

[查看原页图](lecture-05-pages/page-055.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=55)

````text
1. Space-time

2. STL

3. Sequence Containers

4. Associative Containers
````

## PDF 第 56 页

[查看原页图](lecture-05-pages/page-056.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=56)

````text
1. Space-time
2. STL
3. Sequence Containers
4. Associative Containers
¢ Bonus - Unordered Associative Containers
````

## PDF 第 57 页

[查看原页图](lecture-05-pages/page-057.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=57)

````text
The Containers library is a generic collection of clas
implement common data structures like queues, lis
containers:
e sequence containers,
e associative containers,
————— _—e unordered associative containers, (since C++11)
````

## PDF 第 58 页

[查看原页图](lecture-05-pages/page-058.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=58)

````text
Unordered Associative Containers
map unordered_map
set unordered_set
````

## PDF 第 59 页

[查看原页图](lecture-05-pages/page-059.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=59)

````text
1 std::map<int, std::string> courses

{103, }s

{107, hs

{109, A

; Drop-in replacement
1 std::unordered_map<int, std::string> courses
{103, },
{107, }s
{109, }
3
````

## PDF 第 60 页

[查看原页图](lecture-05-pages/page-060.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=60)

````text
The Caveat - Hashing
std:: unordered _ map
Defined in header <unordered_map>
template<
class Key,
> class unordered_map;
````

## PDF 第 61 页

[查看原页图](lecture-05-pages/page-061.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=61)

````text
What is a hash function?

¢ “Scrambles” a key into a size_t (64 bit)

* Small changes in the input should produce large changes in the output
“CS106L” 80489869
````

## PDF 第 62 页

[查看原页图](lecture-05-pages/page-062.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=62)

````text
1 std::map<int, std::string> courses

{103, }s

{107, hs

{109, A

; Drop-in replacement
1 std::unordered_map<int, std::string> courses
{103, },
{107, }s
{109, }
3
````

## PDF 第 63 页

[查看原页图](lecture-05-pages/page-063.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=63)

````text
Unordered Map Implementation
FJ ny Visualization
aes https://web.stanford.edu/~pseay/cs106l/hash-map
Hash Seve uf * : P p ew the live page
Table | (ease
````

## PDF 第 64 页

[查看原页图](lecture-05-pages/page-064.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=64)

````text
ee
ii ear — : Tig
ee peer, en
eS a a i= —====_
| om) ,
O(log(n)) O(1)
````

## PDF 第 65 页

[查看原页图](lecture-05-pages/page-065.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=65)

````text
Recap
````

## PDF 第 66 页

[查看原页图](lecture-05-pages/page-066.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=66)

````text
Summary of Data Structures
Very Fast Slow Slow Slow
o std::deque Fast Slow Fast Fast
E (front/back) (front/back)
iu Slow Slow
ey (all others) (all others)
o
Oo
std::unordered_set N/A Very Fast Very Fast Very Fast
std::unordered_map N/A Very Fast Very Fast Very Fast
````

## PDF 第 67 页

[查看原页图](lecture-05-pages/page-067.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=67)

````text
FP Associative containers
Sequence containers
Associative containers implement sorted data structures that can be quickly searched (O(log n) complexity).
i implement data structures which can be accessed sequentially. — . :
t collection of unique keys, sorted by keys
fixed-sized inplace contiguous array ad (class template)
(class template) collection of key-value pairs, sorted by keys, keys are unique
t resizable contiguous array = (class template)
wOneer (class template) wmaiTriost collection of keys, sorted by keys
= resizable, fixed capacity, inplace contiguous arra = g (class: template)
inplace_vector (C++26) (class template) pacity, bel 2 x ti collection of key-value pairs, sorted by keys
4 5 MULTIMAP i355 template)
hive tc++20) collection that reuses erased elements’ memory
(class template) — -
Unordered associative containers (since C++11)
double-ended queue
deque (class template) Unordered associative containers implement unsorted (hashed) data structures that can be quickly searched (0/1)
ns = = = q ( lexity).
- 2 singly-linked list average, O(n) worst-case comps
forward_List (Cc++11) (class template) Histed cok collection of unique keys, hashed by keys
= doubly-linked list vlaseh eee (Cea (class template)
list clase teinpiate) rer deredinas teat nection of Rayvolus pairs, hashed by keys, keys are unique
. —________asts
Container adaptors unordered_multiset (C++11) “peop la neshed byeay3
Container adaptors provide a different interface for sequential containers. unordered_multimap (c++11) Boop alas pairs, hashed by keys
od J lass ter
dtack adapts a container to provide stack (LIFO data structure)
(class template)
ous adapts a container to provide queue (FIFO data structure)
au (class template)
an adapts a container to provide priority queue
priority_queue (class template)
flat set (+223) adapts a container to provide a collection of unique keys, sorted by keys
— (class template)
flat_map (c++23) adapts two containers to provide a collection of key-value pairs, sorted by unique keys cppreference.com
es (class template)
flat_multiset (c++23) adapts a container to provide a collection of keys, sorted by keys
(class template)
flat_multimap (c++23) adapts two containers to provide a collection of key-value pairs, sorted by keys
= (class template)
````

## PDF 第 68 页

[查看原页图](lecture-05-pages/page-068.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page=68)

````text
1. Space-time
¢ Tradeoffs
2. STL
¢ Standard Template Library
3. Sequence Containers
¢ Ex: vector, deque., ...
4. (Unordered) Associative Containers
¢ Ex: (unordered_) map, set, ...
````
