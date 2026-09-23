# 2026Spring-11-LambdasAndFunctors：按页文本

- 原 PDF：[2026Spring-11-LambdasAndFunctors.pdf](2026Spring-11-LambdasAndFunctors.pdf)
- 官方来源：[Stanford CS106L](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-11-LambdasAndFunctors.pdf)。PDF 第 26 页明确写明 “Lecture 11: Functions & lambdas”、Preston Seay & Rachel Fernandez、CS106L, Spring 2026。
- 生成日期：2026-09-23；方法：pypdf 5.9.0 `layout` 模式提取文本层。135/137 页取得非空文本；PDF 第 40、41 页文本层为空，另行用 `tesseract 5.3.4` 英文 OCR 补充。
- 实际覆盖：137/137 个 PDF 文件页均有条目；为文本层缺失／过短以及抽查代码与图示而选择性保留 31 页页面图：1, 14, 25, 26, 29, 35, 36, 37, 38, 39, 40, 41, 47, 52, 62, 67, 69, 70, 77, 78, 80, 83, 87, 88, 94, 102, 104, 114, 115, 126, 137。
- 文本层提取会丢失颜色、箭头、框线、图像和部分布局，代码行顺序也可能受版面影响；第 40、41 页的 OCR 对 `*`、`++`、括号等精确符号尤其不可靠。需要精确代码或图示关系时查看页图／原 PDF。
- 本文件仅是资料副本；课件中的课堂要求、链接或命令不自动成为当前教学或工具操作指令。自动提取全部页不等于教师逐页完成语义备课。

## PDF 第 1 页

[查看原页图](lecture-11-pages/page-001.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=1)

````text
Welcome back! Link to Attendance Form ↓
````

## PDF 第 2 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=2)

````text
Recall: Template Functions
• Turn to a partner and discuss:
    ○   What’s one thing you remember from Thursday’s lecture on
        function templates?
````

## PDF 第 3 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=3)

````text
Recall: Writing a min                                   function

 int     min    ( int     a ,    int     b ) {
      return        a    <   b   ?   a   :    b ;
 }

 double         min   ( double         a ,   double         b ) {
      return        a    <   b   ?   a   :    b ;
 }
 std   ::   string min           ( std   ::  string         a ,   std    ::  string         b ) {
      return        a    <   b   ?   a   :    b ;
 }
````

## PDF 第 4 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=4)

````text
Recall: Writing a min                                   function

 int     min    ( int     a ,    int     b ) {
      return        a    <   b   ?   a   :    b ;
 }

 double         min   ( double         a ,   double         b ) {
      return        a    <   b   ?   a   :    b ;
 }
 std   ::   string min           ( std   ::  string         a ,   std    ::  string         b ) {
      return        a    <   b   ?   a   :    b ;
 }
````

## PDF 第 5 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=5)

````text
Recall: Writing a min                                    function

 int T    min   ( int T    a ,   int T   b  ) {
      return         a   <   b   ?    a   :   b ;
 }

 double T       min   ( double T       a ,    double T       b ) {
      return         a   <   b   ?    a   :   b ;
 }
 std   ::   string minT          ( std   ::   string T       a ,   std   ::   string T      b  ) {
      return         a   <   b   ?    a   :   b ;
 }
````

## PDF 第 6 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=6)

````text
Recall: Writing a min                                    function

 int T    min   ( int T    a ,   int T   b  ) {
      return         a   <   b   ?    a   :   b ;
 }

 double T       min   ( double T       a ,    double T       b ) {
      return         a   <   b   ?    a   :   b ;
 }
 std   ::   string minT          ( std   ::   string T       a ,   std   ::   string T      b  ) {
      return         a   <   b   ?    a   :   b ;
 }
````

## PDF 第 7 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=7)

````text
Recall: Writing a min                                     function

 int T    min   ( int T    a ,   int T    b ) {
      return         a   <   b    ?   a   :    b ;
 }template <typename                       T >

 double T       min    ( double T       a ,   double T       b  ) {
      return         a   <   b    ?   a   :    b ;
 }
 std    ::  string minT          (  std   ::  string T       a  ,   std   ::   string T       b ) {
      return         a   <   b    ?   a   :    b ;
 }
````

## PDF 第 8 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=8)

````text
Recall: Writing a templated min                                                function




   This is a      template                                                 T  gets replaced with a
                                                                           specific type

                              template         < typename          T>
                              T min     ( T   a,   T   b ) {
                                   return       a   <   b  ?   a   :   b ;
                              }
````

## PDF 第 9 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=9)

````text
Recall: explicit instantiation

Template functions cause the compiler to generate code for us


 int     min  ( int     a,   int     b ) {                            // Compiler generated
       return       a   <   b   ?   a   :   b;                        //    Compiler          generated
 }                                                                    //    Compiler          generated

 double       min   ( double       a ,  double       b ) {            // Compiler generated
       return       a   <   b   ?   a   :   b;                        //    Compiler          generated
 }                                                                    //    Compiler          generated

 min   < int  >(  106   ,  107   );                    //    Returns        106
 min   < double     >(  1.2  ,   3.4  );               //    Returns        1.2
````

## PDF 第 10 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=10)

````text
Recall: explicit instantiation

Template functions cause the compiler to generate code for us


 int     min  ( int     a,   int     b ) {                            // Compiler generated
       return       a   <   b   ?   a   :   b;                        //    Compiler          generated
 }                                                                    //    Compiler          generated

 double       min   ( double       a ,  double       b ) {            // Compiler generated
       return       a   <   b   ?   a   :   b;                        //    Compiler          generated
 }                                                                    //    Compiler          generated

 min   < int  >(  106   ,  107   );                    //    Returns        106
 min   < double     >(  1.2  ,   3.4  );               //    Returns        1.2
````

## PDF 第 11 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=11)

````text
Recall: Implicit instantiation is kind of like auto


                                int   m  =  min  (106  ,  107 );


                               It’s exactly as if we
                                             wrote
                                  min  <int  >(  106  ,  107  )
````

## PDF 第 12 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=12)

````text
Recall: Writing a templated find                                              function

This find function generalizes across all iterator types!

 template         < typename          It ,   typename          T >
 It find      ( It    begin     ,   It   end   ,   const       T &  value     ) {
   for       ( auto      it   =   begin; it           !=   end;      ++  it) {
           if    ( * it    ==   value)        return       it;
     }
     return        end;
 }
````

## PDF 第 13 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=13)

````text
Recall: Writing a templated find                                                               function

Our find           function works for other vectors, or even other containers

 std   ::   vector      < std    ::  string      >    v {     "run"      ,   "forrest"            };
 auto       it    =   find     (v.   begin     (), v.       end   (),      "run"     );
 // It = vector<std::string>::iterator
 // T = std::string

 std   ::set      < std   ::   string      >   s {      "run"     ,   "forrest"            };
 auto       it    =   find     (s.   begin     (), s.       end   (),      "run"     );
 // It = std::set<std::string>::iterator                                                Implicit Instantiation!
 // T = std::string                                                                     Compiler deduces
                                                                                        template types by
                                                                                        looking at arguments
````

## PDF 第 14 页

[查看原页图](lecture-11-pages/page-014.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=14)

````text
Wait… why pass in iterators to find           ?
````

## PDF 第 15 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=15)

````text
Recall: Writing a templated find                                                   function

Our find        function works for other vectors, or even other containers

 std  ::  vector     < std  ::  string     >   c {    "run"    ,   "forrest"         };
 auto     it    =  find    (c.  begin    (), c.     end   (),    "run"    );


 std  ::  set   <std   ::  string     >  c {     "run"    ,   "forrest"         };
 auto     it    =  find    (c.  begin    (), c.     end   (),    "run"    );
````

## PDF 第 16 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=16)

````text
Recall: Writing a templated find                                                   function

Our find        function works for other vectors, or even other containers

 std  ::  vector     < std  ::  string     >   c {    "run"    ,   "forrest"         };
 auto     it    =  find    (c.  begin    (), c.     end   (),    "run"    );


 std  ::  set   <std   ::  string     >  c {     "run"    ,   "forrest"         };
 auto     it    =  find    (c.  begin    (), c.     end   (),    "run"    );
````

## PDF 第 17 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=17)

````text
Recall: Writing a templated find                                                function

Our find        function works for other vectors, or even other containers

 std  ::  vector     <std   :: string     >  c {     "run"   ,   "forrest"         };
 auto     it   =   find   (c.  begin    (), c.     end  (),    "run"    );


 std  ::  set  < std  ::  string     >  c {    "run"    ,   "forrest"        };
 auto     it   =   find   (c.  begin    (), c.     end  (),    "run"    );



                                    They’re the same code
````

## PDF 第 18 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=18)

````text
An alternative find                                               function

We can pass the whole container.


 template           < typename           Container          ,   typename           T >
 auto       find    ( const        Container          &   c ,   const        T &   value      ) {     for
       ( auto       it    =   c.begin(); it                 !=    c.end();           ++  it) {
             if     ( * it    ==    value)         return         it;                                     Advantage:             Now the
       }                                                                                                  caller doesn’t have
       return         end;                                                                                to worry about begin
 }                                                                                                        and end!

 std    ::vector         < std   ::string         >   v {     "run"      ,   "forrest"            };
 auto       it    =   find     (v,     "run"      );
                                                                      Container           = std::vector<std::string>
                                                                      T   = std::string
````

## PDF 第 19 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=19)

````text
An alternative find                                 function

Using iterators instead allows us to search only part of a container

 std   ::   vector      <int>        v {     106    ,   107   ,   106    ,   143   ,   149    ,   106     };

 // Search for 106L, skipping first and last elements
 auto       it    =   find     (v.   begin     ()     +   1 , v.    end    ()    -   1 ,    106   );

 // Get index of iterator using std::distancestd::cout<<std::distance(v.begin(),  it);

 // Prints            2,     not 0
````

## PDF 第 20 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=20)

````text
We defined our find        function
in a general way!
````

## PDF 第 21 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=21)

````text
What questions do you have?







                  bjarne_about_to_raise_hand
````

## PDF 第 22 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=22)

````text
How can we make find                              even more general!?
• Instead of find       searching for value        in a container…
• What if we could ask arbitrary questions?
    • A vowel in a string  ?
    • A prime number in a vector<int>     ?
    • A number divisible by 5 in a set<int>  ?


 •   More generally, what if we could perform arbitrary operations?
````

## PDF 第 23 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=23)

````text
An even better find                                            function?

How else could we generalize this?


 template          < typename          Container        ,   typename          T >
 auto      find    ( const       Container        &   c ,   const       T &   value     ) {    for
       ( auto     it    =   c.begin(); it               !=    c.end();         ++  it) {
            if    ( * it    ==    value)        return       it;
       }
       return        end;
 }

 std   ::vector        < std   ::string       >   trail_lens = {                "6mi"     ,   "20ft", "5km"              };
 auto      it    =   find    (trail_lens,             "3mi"     );
````

## PDF 第 24 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=24)

````text
An even better find                                              function?

How else could we generalize this?


 template           < typename          Container         ,   typename          Q >
 auto      find     ( const       Container         &   c ,                   ) {Question
        for     ( auto      it    =   c.begin(); it               !=    c.end();          ++  it) {
             if    (Question??*it == value)      return        it;
       }
       return        end;
 }

 std   ::vector         < std   ::string        >   trail_lens = {                "6mi"     ,   "20ft", "5km"               };
 auto      it     =   find    (trail_lens,                             );Is it a good length?
````

## PDF 第 25 页

[查看原页图](lecture-11-pages/page-025.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=25)

````text
(He knew about lambdas.)
````

## PDF 第 26 页

[查看原页图](lecture-11-pages/page-026.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=26)

````text
Lecture 11:
Functions & lambdas


           Preston Seay & Rachel Fernandez
               CS106L, Spring 2026
````

## PDF 第 27 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=27)

````text
Today’s Agenda
• Functions and Lambdas
    • How can we represent functions as variables in C++?
• Algorithms
    • Tackling a popular algorithm with modern C++
• Ranges and Views
    • A brand new (C++26), functional approach to C++ algorithms
````

## PDF 第 28 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=28)

````text
Announcements

●   We want to make this class easier
      •  We’ll be going over the first half of A4 in class
      •  You can now skip 1 assignment for the rest of the quarter
●   Assignments
      •  A4 is out… you can complete it after today
      •  A2 grades are out
●   Office hours
      •  Thursdays 4:30-5:20 (after class) in Thornt 210
      •  Fridays 1:30-2:20 in 160-315
````

## PDF 第 29 页

[查看原页图](lecture-11-pages/page-029.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=29)

````text
Functions and Lambdas
````

## PDF 第 30 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=30)

````text
Definition: A predicate is a boolean              -valued function
````

## PDF 第 31 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=31)

````text
Does the trail have a waterfall?




Definition: A predicate is a boolean                        -valued function




                                         Is this trail longer than that one?
````

## PDF 第 32 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=32)

````text
Predicate Examples

Unary                                                                                      Binary
  bool        isVowel        ( char        c ) {                                           bool bool   isDivisibleisLessThan   ((int int  xn, , int int  yd ) ) {
       c   =    toupper        ( c  );                                                              {   return          x   <    y ;
       return         c    ==   'A'       ||     c    ==   'E'       ||                              return          n   %   d    ==     0 ;
           c    ==   'I'       ||     c   ==    'O'       ||   c   ==    'U';                }
  }                                                                                        }
  bool       wouldPrestonApproveOf                          (  Trail        t )            bool bool   isLongerThanisDivisible   ((int Trail n,  xint , Trail d)     y  ){
         {                                                                                          { return return  x .n len > y% d == .  len0;  ;
         return t.           hasWaterfall               ();
  }                                                                                        } }
````

## PDF 第 33 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=33)

````text
Using predicates
•  How can we use isVowel               to find the first vowel in a
   string     ?
•  Or wouldPrestonApproveOf                    to find a trail with a waterfall
   in a vector<Trail>           ?
•  Or isDivisible            to find a number divisible by 5?
````

## PDF 第 34 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=34)

````text
Key Idea: We need to pass a predicate to a
function
````

## PDF 第 35 页

[查看原页图](lecture-11-pages/page-035.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=35)

````text
Modifying our find        function
````

## PDF 第 36 页

[查看原页图](lecture-11-pages/page-036.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=36)

````text
Modifying our find        function
````

## PDF 第 37 页

[查看原页图](lecture-11-pages/page-037.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=37)

````text
Modifying our find        function
````

## PDF 第 38 页

[查看原页图](lecture-11-pages/page-038.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=38)

````text
Modifying our find        function
````

## PDF 第 39 页

[查看原页图](lecture-11-pages/page-039.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=39)

````text
Modifying our find        function
````

## PDF 第 40 页

[查看原页图](lecture-11-pages/page-040.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=40)

> 本页文本层为空；以下为机器 OCR，仅供定位。精确代码／符号须查看原页图。

````text
Answer: Templates plus predicates | 7°0: the type
predicate.
Compiler will
figure this out
for us using
template <typename It, typename Pred> = | ini vejear
It find(It first, It last, Pred pred) { | instantiation!
for (auto it = first; it != last; ++1
if (pred (it) ) return 1t; pred: our predicate,
} passed as a parameter
return last; Hey Look! We’re calling
} our predicate on each
element. As soon as we
find one that matches,
we return
````

## PDF 第 41 页

[查看原页图](lecture-11-pages/page-041.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=41)

> 本页文本层为空；以下为机器 OCR，仅供定位。精确代码／符号须查看原页图。

````text
Answer: Templates plus predicates | 5700; the type
predicate.
Compiler will
figure this out
template <typename It, typename Pred> aide
It find_if(It first, It last, Pred pred)| instantiation!
fora(auto it = first; it != last; ++1
(pred(x*xit)) return it; wails wen epee,
} passed as a parameter
retirn last; Hey look! We’re calling
Let’s give this our predicate on each
function a new element. As soon as we
name so it doesn’t find one that matches,
get confused with we return
old one!
````

## PDF 第 42 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=42)

````text
What questions do you have?







                 bjarne_about_to_raise_hand
````

## PDF 第 43 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=43)

````text
Using our find_if                                          function

 bool        isVowel         ( char       c  ) {
       c   =    toupper         ( c  );                                                                       You:      ”What type
       return          c   ==     'A'      ||     c    ==     'E'      ||     c   ==     'I’      ||          is this?”
                        c    ==    'O'       ||    c    ==     'U’    ;                                       Compiler:          “Don’t
 }                                                                                                            worry about it!”


 std    ::   string          flower          =   "rose"        ;
 auto        it    =    find_if         (flower.          begin       (), flower.              end    (),      isVowel         );
 * it     =    'i'    ;   // “rise”
````

## PDF 第 44 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=44)

````text
Using our find_if                                          function
                                                                                                              You:     ”What type
 bool        isGood        ( Trail       t) { // Would I Approve?                                             is this!!?”
        return          t.   hasWaterfall               ();                                                   Compiler:          “I
 }                                                                                                            gottttchuuu man”


 std    ::   vector        <Trail>           trails          =   getNearbyTrails                    ();
 auto        it     =   find_if         (trails.           begin      (), trails.              end    (),        isGood        );
 assert(it->hasWaterfall() == true);
````

## PDF 第 45 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=45)

````text
Passing functions allows us to generalize an
  algorithm with user-defined behaviour
````

## PDF 第 46 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=46)

````text
Aside: Seriously though, what is the type of Pred              ?
````

## PDF 第 47 页

[查看原页图](lecture-11-pages/page-047.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=47)

````text
Pred           is a function pointer

  find_if(flower.                        begin        (), flower.                 end     (), isVowel);
  //      Pred         =    bool      (  * )(    char      )

  find_if(t.                begin        (), t.         end     (), isGood);
  //      Pred         =    bool      (  * )(    Trail       )



My function                        I’m a                And I take in a
returns a       bool               function             single      Trail     as
                                   pointer              a parameter
As we’ll see shortly, a function pointer is just one of the types we can pass to find_if
````

## PDF 第 48 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=48)

````text
Get some practice with
function pointers!


Code is here:
online-ide.com/2mwjsthYoN
````

## PDF 第 49 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=49)

````text
Function pointers generalize poorly

Consider that we want to find a number less than N                        in a vector

 bool     lessThan5         (int     x )   {  return        x  <   5 ;   }
 bool     lessThan6         (int     x )   {  return        x  <   6 ;   }
 bool     lessThan7         (int     x )   {  return        x  <   7 ;   }

 find_if      (begin,        end,     lessThan5);
 find_if      (begin,        end,     lessThan6);
 find_if      (begin,        end,     lessThan7);
````

## PDF 第 50 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=50)

````text
Function pointers generalize poorly

                                                         What if we want
                                                         to find a number
                                                         less than N, but
                                                         we don’t know
                                                         what N is until
                                                         runtime?
 int      n;
 std    ::cin        >>    n;
 find_if(begin, end,                        /* lessThan... Haelpp... */                                )
````

## PDF 第 51 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=51)

````text
We can’t just add another parameter

Turn to someone next to you and talk about why this wouldn’t work!




 bool    isLessThan     ( int   elem   ,  int   n ) {
     return      elem   <   n;
 }
````

## PDF 第 52 页

[查看原页图](lecture-11-pages/page-052.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=52)

````text
We can’t add another parameter to pred!
````

## PDF 第 53 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=53)

````text
We want to give our function extra state…

    …without introducing another parameter
````

## PDF 第 54 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=54)

````text
Introducing… lambda functions

Lambda functions are functions that capture state from an enclosing scope.

 int    n;
 std   ::cin      >>    n;

 auto     lessThanN          =   [n](    int    x ) {     return       x   <   n; };

 find_if(begin, end, lessThanN);                             //
````

## PDF 第 55 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=55)

````text
Lambda Syntax


I don’t know the                           Capture clause                                  Parameters
type! But the                              lets us use                                     Function parameters,
compiler does.                             outside variables                               exactly like a normal
                                                                                           function
          auto              lessThanN                           =      [n](           int           x   ) {
                      return                   x      <      n;
          };                                                                      Function body

                                                                                  Exactly as a normal function,
                                                                                  except only parameters and
                                                                                  captures are in-scope
````

## PDF 第 56 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=56)

````text
A note on captures


  auto       lambda         =    [ capture-values                 ](  arguments           ) {
        return         expression;
  }

  [ x ](  arguments           )               // captures x by value (makes a copy)
  [ x&  ](   arguments           )            // captures x by reference
  [x, y](        arguments           )        // captures x, y by value
  [&](    arguments           )               // captures               everything               by reference
  [&, x](        arguments           )        // captures               everything except x                           by reference
  [=](    arguments           )               // captures everything by value
````

## PDF 第 57 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=57)

````text
We don’t have to use captures!

Lambdas are good for making functions on the fly
````

## PDF 第 58 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=58)

````text
We don’t have to use captures!

Lambdas are good for making functions on the fly
````

## PDF 第 59 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=59)

````text
auto           parameters are shorthand for templates

   auto        lessThanN               =    [n](      auto        x ) {
        return           x    <    n;
   };                                                                           This is true wherever you see

                                                                                an   auto    parameter, not just
                                                                                in lambda functions!
   template              < typename              T >                            Uses    implicit instantiation                !
   auto        lessThanN               =    [n](      T    x ) {                Compiler figures out types
        return           x    <    n;                                           when function is called
   };
````

## PDF 第 60 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=60)

````text
Get some practice with
lambdas!


Code is here:
online-ide.com/Zgnickm1lI
````

## PDF 第 61 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=61)

````text
What questions do you have?







                 bjarne_about_to_raise_hand
````

## PDF 第 62 页

[查看原页图](lecture-11-pages/page-062.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=62)

````text
How do lambdas work?
````

## PDF 第 63 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=63)

````text
Recall: The Standard Template Library (STL)




     Containers                                                       Iterators
     How do we store groups of                                        How do we traverse
     things?                                                          containers?


     Functors                                                         Algorithms
     How can we represent functions                                   How do we transform and modify
     as objects?                                                      containers in a generic way?
````

## PDF 第 64 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=64)

````text
Definition: A functor is any object that defines an operator()

                 In English: an object that acts like a function
````

## PDF 第 65 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=65)

````text
An example of a functor: std                                               ::    greater             <  T  >

 template           < typename            T >
 struct         std   ::   greater          {
      bool      operator()            ( const        T &   a ,    const       T  &   b )   const        {
           return        a    >   b ;
      }
 };
                                                                  Hmm.. Seems like a function
 std   ::   greater        <int>        g;
 g(  1 ,    2 );    // false
````

## PDF 第 66 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=66)

````text
Another STL functor: std                                                              ::      hash           <   T   >

  template            <>                                                                                              Aside: This syntax
                                                                                                                    is called a              template
  struct         std    ::   hash    <  MyType       > {                                                              specialization                  for
        size_t operator()                     ( const         MyType       &    v )   const         {                        type MyType
              // Crazy, theoretically rigorous hash function
              // approved by 7 PhDs and Donald Knuth goes here
              return          ...;
        }
  };                                                                                                    Hint hint:              This is
                                                                                                      also       one     of the ways
  MyType         m;     std    ::  hash     < MyType        >                                             to create a hash
  hash_fn;                                                                                                  function for a
  hash_fn        (  m ) ;    // 125123201 (for example)                                                         custom type
````

## PDF 第 67 页

[查看原页图](lecture-11-pages/page-067.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=67)

````text
Since a functor is an object, it can have state
````

## PDF 第 68 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=68)

````text
Functors can have state!

 struct       my_functor           {
      int    operator()         ( int     a )   const      {
          return        a   *  value;
      }

      int    value;
 };

 my_functor           f;
 f.value        =   5 ;
 f(  10  );   // 50
````

## PDF 第 69 页

[查看原页图](lecture-11-pages/page-069.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=69)

````text
Time for a dark secret
````

## PDF 第 70 页

[查看原页图](lecture-11-pages/page-070.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=70)

````text
When you use a lambda,
a functor type is generated
````

## PDF 第 71 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=71)

````text
This code…





 int      n   =   10  ;
 auto       lessThanN            =   [n](     int     x ) {      return         x   <   n; };
 find_if        (begin, end, lessThanN);
````

## PDF 第 72 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=72)

````text
…is equivalent to this code!

  class           lambda_6_18                Random name that                                                   Recall: functor call
  {                                         only the compiler                                                                operator
  public:                                            will see!

        bool      operator()           ( int      x )   const       {    return        x   <    n; }
            lambda_6_18            ( int&      _n   ) : n{      _n  } {}                                           Class constructor
  private:
        int     n;                                       Our captures became
  };                                                    fields in the class!

  int     n   =   10   ;
 auto       lessThanN            =       lambda_6_18            { n };                                 Capturing variable n from
  find_if       (begin, end, lessThanN);                                                               outer scope by passing to
                                                                                                                      constructor

If you are curious about this stuff, check out https://cppinsights.io/!
````

## PDF 第 73 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=73)

````text
You’ve seen this kind of thing before…





 std  ::vector      <int>      v {  1 ,2 , 3};                   auto    begin     =  v . begin   ();
                                                                 auto    end    =  v. end  ();
 for    ( const int&         e : v)                              for    (auto    it   =   begin; it       !=   end;    ++  it)
 {                                                               {
      // ...                                                     // ...
 }                                                               }
````

## PDF 第 74 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=74)

````text
It’s the same ordeal! Syntactic sugar


                                                                                class           lambda_6_18
                                                                                {
                                                                                public:
                                                                                      bool      operator()          ( int    x )   const
  int     n   =   10  ;                                                               {   return        x   <   n; }
  auto      lessThanN           =   [n](     int     x )                                  lambda_6_18           ( int&     _n  ) : n{      _n  }
  {   return        x   <   n; };                                               {}
                                                                                private:
  find_if       (begin, end, lessThanN);                                              int     n;
                                                                                };
                                                                                int     n   =   10  ;
                                                                                auto      lessThanN           =      lambda_6_18           {n};
                                                                                find_if       (begin, end, lessThanN);
````

## PDF 第 75 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=75)

````text
Functions & Lambdas Recap
•  Use functions/lambdas to pass around behaviour as variables
•  Aside: std::function                   is an overarching type for functions/lambdas
     •  Any functor/lambda/function pointer can be cast to it
    •   It is a bit slower
     •  I usually use auto/templates and don’t worry about the types!


 std  ::  function     <bool    ( int  ,  int   )>   less    =   std  ::  less  <int>    {};
 std  ::  function     <bool    ( char   )>   vowel     =   isVowel     ;
 std  ::  function     <int   ( int  ) >  twice      =  [](  int    x ) {    return      x   *  2 ; };
````

## PDF 第 76 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=76)

````text
What questions do you have?







                 bjarne_about_to_raise_hand
````

## PDF 第 77 页

[查看原页图](lecture-11-pages/page-077.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=77)

````text
Where do we use functions & lambdas?
````

## PDF 第 78 页

[查看原页图](lecture-11-pages/page-078.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=78)

````text
Algorithms
````

## PDF 第 79 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=79)

````text
Recall: The Standard Template Library (STL)





     Containers                                                       Iterators
     How do we store groups of                                        How do we traverse
     things?                                                          containers?


     Functors                                                         Algorithms
     How can we represent functions                                   How do we transform and modify
     as objects?                                                      containers in a generic way?
````

## PDF 第 80 页

[查看原页图](lecture-11-pages/page-080.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=80)

````text
Huh… that looks familiar
````

## PDF 第 81 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=81)

````text
<algorithm>                             is a collection of template functions




                std    ::  count_if         (InputIt           first     , InputIt             last    , UnaryPred              p );
                    How many elements in [first, last) match predicate p?


                  std   ::  sort     (RandomIt            first     , RandomIt              last    , Compare            comp     );
        Sorts the elements in [first, last) according to comparison comp


        std   ::   max_element            (ForwardIt             first      , ForwardIt              last    , Compare            comp     );
 Finds the maximum element in [first, last) according to comparison comp
````

## PDF 第 82 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=82)

````text
<algorithm>                                   functions operate on iterators




          std   ::   copy_if        (InputIt           r1  , InputIt            r2  , OutputIt              o , UnaryPred              p );
        Copy the only elements in [r1, r2) into o that match predicate p


         std   ::   transform          (InputIt           r1  , InputIt            r2   , OutputIt             o , UnaryOp            op  );
     Apply op to each element in [r1, r2), writing a new sequence into o


     std   ::  unique_copy             (InputIt           i1  , InputIt            i2   , OutputIt             o , BinaryPred                p );
Remove consecutive duplicates from [r1, r2), writing new sequence into o
````

## PDF 第 83 页

[查看原页图](lecture-11-pages/page-083.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=83)

````text
There are a lot of algorithms…
````

## PDF 第 84 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=84)

````text
Things you can do with the STL

     binary search • heap building • min/max
lexicographical comparisons • merge • set union
•set difference • set intersection • partition • sort
nth sorted element • shuffle • selective removal •
    selective copy • for-each • random sample

           all in their most general form!
````

## PDF 第 85 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=85)

````text
What questions do you have?







                 bjarne_about_to_raise_hand
````

## PDF 第 86 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=86)

````text
<algorithm>       lets us inspect and transform data
````

## PDF 第 87 页

[查看原页图](lecture-11-pages/page-087.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=87)

````text
Let’s write an algorithm using the STL!
````

## PDF 第 88 页

[查看原页图](lecture-11-pages/page-088.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=88)

````text
How can we make a tokenizer?
````

## PDF 第 89 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=89)

````text
Breaking down the problem

           “Breaking down the string”



{“Breaking”, “down”, “the”, “string”}
````

## PDF 第 90 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=90)

````text
Breaking down the problem

           “Breaking down the string”



{“Breaking”, “down”, “the”, “string”}
````

## PDF 第 91 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=91)

````text
Breaking down the problem

          “Breaking down the string”
           01234567  …    …    …
                            8         13      17
````

## PDF 第 92 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=92)

````text
Breaking down the problem

          “Breaking down the string”


           0               8        13     17           end()
````

## PDF 第 93 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=93)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 94 页

[查看原页图](lecture-11-pages/page-094.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=94)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 95 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=95)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 96 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=96)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 97 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=97)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 98 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=98)

````text
Breaking down the problem
             “Breaking down the string”

              0                     8           13        17               end()




                      “Breaking”   [0, 8)
                      “ down”      [8, 13)
                      “ the”       [13, 17)
                      “ string”    [17, end)
````

## PDF 第 99 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=99)

````text
Breaking down the problem
              “Breaking down the string”

               0                      8            13         17                end()

        Steps:
        1.    Get indices (iterators)
        2.    Loop over with 2 iterators,
              making tokens
````

## PDF 第 100 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=100)

````text
Step 1) Getting indices v1














                     We’re handling too much logic
                     ourselves…
````

## PDF 第 101 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=101)

````text
Step 1) Getting indices v2










           (std::isspace(*cur)){





If we use a predicate function…

                                               …then this looks like a                       filter,
                                               find_if,         &  find_all        .
````

## PDF 第 102 页

[查看原页图](lecture-11-pages/page-102.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=102)

````text
Step 1) Getting indices v3
````

## PDF 第 103 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=103)

````text
Step 1) Getting indices v3


 std::vector<It> find_all(It begin, It end, Pred p)




                                                                              std::isspace
                 source
````

## PDF 第 104 页

[查看原页图](lecture-11-pages/page-104.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=104)

````text
Step 2) Using indices to get tokens (bad)
````

## PDF 第 105 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=105)

````text
Step 2) Using indices to get tokens




 Spaces: {                                                      }



                                                              spaces.end()
````

## PDF 第 106 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=106)

````text
Step 2) Using indices to get tokens










                   {

                          }
````

## PDF 第 107 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=107)

````text
Step 2) Using indices to get tokens





      first1    = spaces.begin()
      last1     =            ?????
      first2    =            ?????
      d_first   = std::inserter(tokens, tokens.end())
      binary_op =            ?????
````

## PDF 第 108 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=108)

````text
Step 2) Using indices to get tokens





      first1    = spaces.begin()
      last1     = spaces.end() - 1
      first2    = spaces.begin() + 1
      d_first   = std::inserter(tokens, tokens.end())
      binary_op = “a lambda with 2 iterators as input
      and a token as output”
````

## PDF 第 109 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=109)

````text
Step 2) Using indices to get tokens





       first1    = spaces.begin()
       last1     = spaces.end() - 1
       first2    = spaces.begin() + 1
       d_first   = std::inserter(tokens, tokens.end())
       binary_op = [&](auto it1, auto it2) {
                       return Token(source, it1, it2);
                   }
````

## PDF 第 110 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=110)

````text
Step 3) Are we done?


                 “N’ot a!!    Str1ngs 4re   nice :/”








   {“N’ot”, “a!!”, “”, “Str1ngs” “4re”, “”, “nice”, “:/”}
````

## PDF 第 111 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=111)

````text
Step 3) Erase spaces



                                                                 container:
                                                                  -   tokens

                                                                 pred:
                                                                  -   whether a token is
                                                                      empty
````

## PDF 第 112 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=112)

````text
Step 3) Erase spaces




                                                          c:
                                                          tokens

                                                          pred:
                                                          [](const auto& t) {
                                                                return t.content.empty();
                                                          }
````

## PDF 第 113 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=113)

````text
Tokenizer


     Strategy:
    1.       Work through example
    2.       Figure out the logic
    3.       See if the logic follows a common algorithm
            a.       If so, use the std algorithm library for clarity
                     and accuracy

    1.       We found:
            b.       We need to get all the spaces (+ begin & end)
                    i.       The staff gave us a                             find_all              function :)
            c.       We need to convert our spaces into tokens
                    i.       The std gives us a                            transform               for that
            d.       We need to get rid of empty tokens
                    i.       The std gives us a                            erase_if             for that
````

## PDF 第 114 页

[查看原页图](lecture-11-pages/page-114.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=114)

````text
Ranges and Views
````

## PDF 第 115 页

[查看原页图](lecture-11-pages/page-115.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=115)

````text
Ranges are a new version of the STL
````

## PDF 第 116 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=116)

````text
Definition: A range is anything with a begin and end
````

## PDF 第 117 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=117)

````text
std::unordered_set<K,V>
std::vector<T>



                                                                                       Your own custom
                    What’s a range?                                                       type with a
                                                                                        begin      and     end  !




            std::map<K, V>

                                                             std::set<K>
````

## PDF 第 118 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=118)

````text
Recall: why did we pass iterators to find                                                              ?

It allows us to find in a subrange! But most of the time, we don’t need to.

 int     main    () {
     std    ::  vector      <char>         v   =   { 'a'   ,   'b'   ,   'c'    ,   'd'   ,   'e’   };
     auto       it    =   std   ::  find     (v.   begin     (), v.      end    (),     'c'   );
 }


                                              Do we really care about iterators
                                              here?    I just wanted to search the
                                                          entire container!
````

## PDF 第 119 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=119)

````text
Range algorithms operate on ranges

STD ranges provides new versions of <algorithm>                              for ranges

 int     main   () {
     std   ::  vector     <char>        v   =   { 'a'  ,   'b'   ,   'c'   ,   'd'  ,   'e’   };
     auto      it    =  std   ::  ranges      ::  find   (v,     'c'   );
 }

                                          Look! I can pass        v
                                        here because it is a
                                                  range  !
````

## PDF 第 120 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=120)

````text
Range algorithms operate on ranges

We can still work with iterators if we need to


 int    main    () {
     std   ::vector       <char>       v   =  { 'a'   ,   'b'  ,   'c'  ,   'd'   ,  'e'   };

     // Search from 'b' to 'd’
     auto      first      =   v. begin     ()   +   1 ;
     auto      last     =   v.  end  ()    -  1 ;
     auto      it   =   std   :: ranges      :: find    (first, last,             'c'  );
 }
````

## PDF 第 121 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=121)

````text
Ranges: The STL v2
• There are range equivalents of most of the STL <algorithm>              library
• These are very new! C++20/23/26 and beyond!
````

## PDF 第 122 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=122)

````text
Range algorithms are constrained

That just means they make use of the new STL concepts! Remember them?

                                                                                   A range has a begin and end! :)
 template        < class        T >
 concept         range        = requires          ( T &   t ) {     ranges      ::  begin     ( t );    ranges      ::  end     ( t ); };
 template         < class       T >                                             An input range is a range using an
 concept          input_range             =                                                         input iterator
       ranges      ::range       < T > &&      std   ::input_iterator                < ranges      ::  iterator_t           < T >>  ;

 template         < ranges      ::  input_range             R ,   class       T ,   class       Proj      =   std   ::  identity        >
 borrowed_iterator_t                    < R >   find    ( R   &&    r,    const       T &   value, Proj proj                  =   {} );

                                                                                     I’ve cut out some of the code
                                                                                 here, but notice that ranges find
                                                                                                   uses      concepts        !!
````

## PDF 第 123 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=123)

````text
Ranges Recap
• Ranges use concepts! Better error messages, what’s not to like?
• We can pass entire containers
````

## PDF 第 124 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=124)

````text
What questions do you have?







                 bjarne_about_to_raise_hand
````

## PDF 第 125 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=125)

````text
Ranges Recap
• Ranges use concepts! Better error messages, what’s not to like?
• We can pass entire containers
• Okay… is that it?
````

## PDF 第 126 页

[查看原页图](lecture-11-pages/page-126.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=126)

````text
Views: a way to compose algorithms
````

## PDF 第 127 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=127)

````text
Definition: A view is a range that lazily adapts another range
````

## PDF 第 128 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=128)

````text
Definition: A view is a range that lazily adapts another range
````

## PDF 第 129 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=129)

````text
Filter and transform in the old STL

This code is a bit awkward in the current STL


 std   ::vector       <char>        v  =   { 'a'   ,   'b'  ,   'c'   ,   'd'  ,   'e'   };
 // Filter -- Get only the vowels
 std   ::vector       <char>        f;
 std   ::  copy_if      (v.   begin    (), v.      end  (),     std   ::  back_inserter           (f), isVowel);

 // Transform -- Convert to uppercase
 std   ::vector       <char>        t;
 std   ::  transform        (f.   begin    (), f.      end  (),     std   :: back_inserter            (t), toupper);

 // { 'A', 'E' }
````

## PDF 第 130 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=130)

````text
Filter and transform with views!

A view is a range that lazily transforms its underlying range, one element at a time



 std   ::  vector      <char>        letters         =   { 'a'   ,  'b'   ,   'c'   ,   'd'   ,   'e’   };

 auto      f   =   std   ::  ranges      ::  views     ::  filter     (letters, isVowel);
 auto      t   =   std   ::  ranges      ::  views     ::  transform        (f, toupper);

 auto      vowelUpper            =   std   ::  ranges      ::  to < std   ::  vector      < char    >>(t);
````

## PDF 第 131 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=131)

````text
Views are composable


  auto       f   =    std   ::   ranges       ::  views       ::  filter       (letters, isVowel);
  //    f    is a view! It takes an underlying range                                                  letters
  // and yields a new range                                with only vowels                    !

  auto       t   =    std   ::   ranges       ::  views       ::  transform           (f, toupper);
  //    t    is a view! It takes an underlying range                                                  f
  // and yields a new range                                with uppercase chars                         !

  auto       vowelUpper              =    std   ::   ranges       ::  to   < std    ::  vector       <  char     >>(t);
  // Here we materialize the view into a vector!
  //    Nothing actually happens until this line!
````

## PDF 第 132 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=132)

````text
We can chain views together use operator |


 std   ::vector         <char>         letters          =   {  'a'   , 'b'   , 'c'    , 'd'   , 'e'    };
 std   ::vector         <char>         upperVowel              =   letters
     |      std   ::  ranges       ::  views      ::  filter       (isVowel)
     |      std   ::  ranges       ::  views      ::  transform          (toupper)
     |      std   ::  ranges       ::  to   < std   ::  vector       < char     >>();

 // upperVowel = { 'A', 'E' }
````

## PDF 第 133 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=133)

````text
Remember: range algorithms are eager

std::ranges         are a reskin of the old STL algorithms





 // This actually sorts vec, RIGHT NOWWW!!!!
 std :: ranges    :: sort  (v);
````

## PDF 第 134 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=134)

````text
Remember: views are lazy

std::ranges::views                      are a lazy way of composing algorithms



 auto      view     =   letters
      |   std  ::  ranges      :: views     ::  filter     (isVowel)
      |   std  ::  ranges      :: views     ::  transform        (toupper);

 std   ::vector       <char>        upperVowel           =
      std  ::  ranges      ::  to < std   ::  vector     < char    >>(view);
````

## PDF 第 135 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=135)

````text
Pro tip: Views are like Python generators

This code in C++ works exactly the same as this Python code

 auto     view     =   letters
      |   std  ::  ranges     :: views    ::  filter    (isVowel)
      |   std  ::  ranges     :: views    ::  transform       (toupper);
 auto     upperVowel          =  std   :: ranges     :: to  < std  ::  vector    < char   >>(view);




 view     =   (l   for    l   in   letters       if    isVowel     (l))          # Lazy evaluation
 view     =   (l.  upper    ()   for    l   in   view)                           # Lazy evaluation
 upperVowel          =  list    (view)
````

## PDF 第 136 页

[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=136)

````text
What questions do you have?







                  bjarne_about_to_raise_hand
````

## PDF 第 137 页

[查看原页图](lecture-11-pages/page-137.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page=137)

````text
Ranges and view recap
•  Why you might like ranges/views?
    •      Worry less about iterators
    •      Constrained algorithms mean better error messages
    •      Super readable, functional syntax
•  Why you might dislike ranges/views?
    •      They are extremely new, not fully feature complete yet
    •      Lack of compiler support
    •      Loss of performance compared to hand-coded version
    ▪      For more info, see The Terrible Problem of Incrementing a Smart Iterator
````
