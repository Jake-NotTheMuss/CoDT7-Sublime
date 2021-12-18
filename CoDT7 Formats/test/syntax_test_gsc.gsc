/* SYNTAX TEST "Packages/CoDT7 Formats/GSC.sublime-syntax" */

#using scripts\codescripts\struct;
/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.compiler.using */
/* <- keyword.control.import.using */
/*                               ^ punctuation.terminator */

#precache( "fx", "zombie/fx_glow_eye_orange" );
/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.compiler.precache */
/* <- keyword.control.import.precache */
/*       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.group */
/*       ^ punctuation.section.group.begin */
/*                                           ^ punctuation.section.group.end */
/*         ^^^^ string.quoted.double */
/*         ^ punctuation.definition.string.begin */
/*            ^ punctuation.definition.string.end */  
/*             ^ punctuation.separator */
/*               ^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.double */  
/*               ^ punctuation.definition.string.begin */
/*                                         ^ punctuation.definition.string.end */    
/*                                            ^ punctuation.terminator */
#namespace test;
/*^^^^^^^^^^^^^^ meta.compiler.namespace */
/* <- keyword.control.import.namespace */
/*         ^ entity.name.namespace */
/*             ^ punctuation.terminator */

#using_animtree("generic");
/*^^^^^^^^^^^^^^^^^^^^^^^^^ meta.compiler.using_animtree */
/* <- keyword.control.import.using_animtree */
/*             ^^^^^^^^^^^ meta.group */
/*             ^ punctuation.section.group.begin */
/*                       ^ punctuation.section.group.end */
/*              ^^^^^^^^^ string.quoted.double */
/*              ^ punctuation.definition.string.begin */
/*                      ^ punctuation.definition.string.end */
/*                        ^ punctuation.terminator */

function animtreetest()
{
  useanimtree(#animtree);
/*^ support.function.builtin */
/*           ^^^^^^^^^^^ meta.group */
/*           ^ punctuation.section.group.begin */
/*                     ^ punctuation.section.group.end */
/*            ^ variable.language */
/*                      ^ punctuation.terminator */
}

function array_test( &array, array )
/*                   ^ keyword.operator.address-of */
/*                    ^ - support */
/*                           ^ - support */
{
  a = array::add();
  array = array();
/*^ - support */
/*        ^^^^^^^ meta.function-call */
/*        ^ support.function.builtin */
  array_func_ptr = & array;
/*                 ^ keyword.operator.address-of */
/*                   ^ support.function.builtin */

  val = 5 &array;
/*      ^ meta.number.integer.decimal constant.numeric.value */
/*        ^ keyword.operator.arithmetic */
/*         ^ - support */
}


function operators_test()
{
  a = &init;
/*    ^ keyword.operator.address-of */

  a = 4 &init;
/*    ^ meta.number.integer.decimal constant.numeric.value */
/*      ^ keyword.operator.arithmetic */

  root = %generic::root;
/*       ^ - keyword.operator.arithmetic */
/*       ^^^^^^^^^^^^^^ meta.anim-reference string.unquoted */

  root = 4 %generic;
/*       ^ meta.number.integer.decimal constant.numeric.value */
/*         ^ keyword.operator.arithmetic */
/*          ^ - string */
}


function main(){
  a=5;
  while(a>0)a--;
  /*     ^ keyword.operator.comparison */
  /*      ^ meta.number constant.numeric.value */
  /*         ^^ keyword.operator.arithmetic */

  level.foo = 0;
  /* <- constant.language */
  /*   ^ punctuation.accessor */
  /*    ^ variable.other.member */
  /*          ^ meta.number.integer.decimal constant.numeric.value */
  /*           ^ punctuation.terminator */
}

function private autoexec X() {}
/*       ^ storage.modifier */
/*               ^ storage.modifier */
/*                        ^ entity.name.function */

class foo {
/*    ^ entity.name.class */
	var a;
/*^ storage.type */
	var b;
/*^ storage.type */
	constructor() {}
/*^ keyword.declaration */
}

#define EXTTS_BUFSIZE (PTP_BUF_TIMESTAMPS /* comment block */ * level.players.size) // comment line
/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.preprocessor.macro */
/*                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.group */
/* <- keyword.control.import.define */
/*      ^ entity.name.constant.preprocessor */
/*                                        ^ comment.block */
/*                                                              ^ constant.language */
/*                                                                   ^ punctuation.accessor */
/*                                                                            ^ keyword */
/*                                                                                  ^ comment.line */

#insert \
scripts\shared\shared.gsh;
/*^^^^^^^^^^^^^^^^^^^^^^^^ meta.preprocessor */

#define MY_MACRO(a, b)
/*^^^^^^^^^^^^^^^^^^^^ meta.preprocessor.macro */
/*              ^^^^^^ meta.preprocessor.macro.parameters */
/*      ^^^^^^^^ entity.name.function.preprocessor */
/*                   ^ punctuation.section.group.end */

#define max(a, b, \
/*^^^^^^^^^^^^^^^^^ meta.preprocessor.macro */ \
/*         ^^^^^^^^ meta.preprocessor.macro.parameters */ \
/* <- keyword.control.import.define */ \
/*      ^ entity.name.function.preprocessor */ \
/*         ^ punctuation.section.group.begin */ \
/*          ^ variable.parameter */ \
/*           ^ punctuation.separator */ \
/* */ \
/* <- comment.block */ \
 c)  ((a>b) ? (a>c?a:c) : (b>c?b:c))
 /* <- meta.preprocessor.macro meta.group variable.parameter */
  /* <- meta.preprocessor.macro meta.group punctuation.section.group.end */
 /*               ^ keyword.operator.ternary */
 /*                 ^ keyword.operator.ternary */

#define AUTOEXEC autoexec
/*      ^ entity.name.constant */
/*               ^ storage.modifier */


// The following example ensures that comments at the end of preprocessor
// directives don't mess with context transitions
function func() {
/*       ^^^^^^^^ meta.function */
/*              ^ meta.block punctuation.section.block.begin */
/*           ^^ meta.function.parameters */
/*           ^ meta.group punctuation.section.group.begin */
/*       ^ entity.name.function */
    #if( EXTAL == 40000 )       /* 40 MHz */
/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function meta.block */
/*  ^ keyword.control.import */
        #define PLL_RFD_PHI1    10      // PLL0_PH1 = 40MHz
/*      ^ keyword.control.import */
/*                              ^^ meta.number constant.numeric.value */
/*                                      ^ comment.line */
    #endif
/*  ^ keyword.control.import */
}
/* <- meta.function meta.block punctuation.section.block.end */
 /* <- - meta.function meta.block */

function f(x, \
          /*  ^ punctuation.separator.continuation */
      y);

#define CONST0 16 // Comment
#define CONST1 8
/* <- keyword.control.import.define */
/*      ^ entity.name.constant */

#define MACRO_WITH_CURLY_BRACE {
/* <- keyword.control.import.define */
/*      ^ entity.name.constant */

#define MACRO_WITH_CURLY_BRACE_2 }
/* <- keyword.control.import.define */
/*      ^ entity.name.constant */

function
hello() {
    /* <- meta.function entity.name.function */
    return 0;
}

function
IntCompare (
  /* <- meta.function entity.name.function */
  )
{
  const a = 0;
  /* <- meta.block storage.modifier */

  b = 1;
  return max (a, b);
  /* <- meta.block keyword.control */
  /*       ^ meta.block meta.function-call support.function.builtin */
}

function
foo()
/* <- meta.function entity.name.function */
{
   return LIB_SUCCESS;
}

function bar()
/*         ^ meta.function entity.name.function */
{
    return LIB_SUCCESS;
}

THIS_IS_REALLY_JUST_A_MACRO_AND_NOT_A_RETURN_TYPE
/* <- meta.assumed-macro */

function main() {
/* <- keyword.declaration */
    /*   ^ meta.function entity.name.function */
    return 0;
}

#if 0
#ifdef moo
/* <- - keyword.control */
#endif
/* <- - keyword.control */
#endif

#if 0
/*  ^ meta.number constant.numeric.value */
function disabled_func() {
/*       ^ comment.block */
}
#endif

#if TRUE
/*  ^ constant.language */
function enabled_func() {}
/*       ^ entity.name.function */
#else
function disabled_func() {
/*       ^ comment.block */
}
#endif

#if 1
    #if false
/*      ^ constant.language */
        function a(){}
/*      ^ comment.block */
    #else
        function b(){}
    #endif
#else
    function c(){}
/*  ^ comment.block */
#endif

/**
    *
/*  ^ comment.block punctuation.definition.comment */

/////////////////////////////////////////////
// Preprocessor branches starting blocks
/////////////////////////////////////////////


#ifdef FOO
if (1) {
#elif BAR
if (2) {
# elif BAZ
if (3) {
# else
if (4) {
#endif
   	bar = 1;
}
/* <- meta.block punctuation.section.block.end */
 /* <- - meta.block */


/////////////////////////////////////////////
// Test preprocessor branching and C blocks
/////////////////////////////////////////////


function foo(val, val2)
/*       ^^^^^^^^^^^^^^ meta.function */
/*          ^^^^^^^^^^^ meta.function.parameters meta.group */
/*          ^ punctuation.section.group.begin */
/*                    ^ punctuation.section.group.end */
/*           ^^^ variable.parameter */
/*              ^ punctuation.separator */
/*                ^^^^ variable.parameter */
{
/* <- meta.function meta.block */
    result = spawnstruct();
    result.kk = func(val);
/*        ^ punctuation.accessor */
    if (result !== 0) {
/*             ^^^ keyword.operator.comparison */
        return 0;
#if CROSS_SCOPE_MACRO
 /* <- keyword.control.import */
    } else if (result > 0) {
        return 1;
#endif
 /* <- keyword.control.import */
    }
/*  ^ meta.block meta.block punctuation.section.block.end */
/*   ^ - meta.block meta.block */

#if FOO
/* <- keyword.control.import */
    if (val == -1) {
/*  ^^ keyword.control */
/*                 ^ meta.block meta.block punctuation.section.block.begin */
#else
 /* <- keyword.control.import */
    if (val == -2) {
/*                 ^ meta.block meta.block punctuation.section.block.begin */
#endif
 /* <- keyword.control.import */
        val += 1;
    }
/*  ^ meta.block meta.block punctuation.section.block.end */
/*   ^ - meta.block meta.block */

    return -1;
}
/* <- meta.function punctuation.section.block.end */
 /* <- - meta.function */


/////////////////////////////////////////////
// Matching various function definitions
/////////////////////////////////////////////

function /* comment */ myfunc
/* <- keyword.declaration */
/*       ^ comment.block */
/*                     ^^^^^^ meta.function entity.name.function */
  (a)
/*^^^ meta.function.parameters meta.group */
/*^ punctuation.section.group.begin */
/* ^ variable.parameter */
/*  ^ punctuation.section.group.end */
{
/* <- meta.function meta.block punctuation.section.block.begin */
}


MACRO1
function
/* <- - entity.name.function */
func_name() {
/* < entity.name.function */
}

MACRO1 function MACRO2 myfuncname () {
/*                     ^^^^^^^^^^^^^^^ meta.function */
/*                                ^^ meta.function.parameters */
/*                                   ^ meta.block punctuation.section.block.begin
/*     ^ keyword.declaration */
/*                     ^ entity.name.function */

        do {
            break;
        } while(true);

    switch (a) {
      case 1: break;
/*          ^ punctuation.separator */
      case 100 - 10: break;
/*                 ^ punctuation.separator */
      default: break;
/*           ^ punctuation.separator */
    }
}

private function MACRO funcname(){}
/*                     ^^^^^^^^^^^^ meta.function */
/*                             ^^ meta.function.parameters */
/* ^ storage.modifier */
/*      ^ keyword.declaration */
/*                     ^ entity.name.function */

MACRO function
/*    ^ keyword.declaration */
funcname2
/* ^ entity.name.function */
()
{
		a = array(1,2,3);
    b = a[0];
/*       ^^^ meta.brackets */
/*       ^ punctuation.section.brackets.begin */
/*         ^ punctuation.section.brackets.end */
}

/////////////////////////////////////////////
// Invalid
/////////////////////////////////////////////
)
/* <- invalid.illegal.stray-bracket-end */
}
/* <- invalid.illegal.stray-bracket-end */


/////////////////////////////////////////////
// Inserts
/////////////////////////////////////////////

#insert scripts\shared\version.gsh;
/*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.preprocessor.insert */
/* <- keyword.control.import.insert */
/*                                ^ punctuation.terminator */


/////////////////////////////////////////////
// Numeric Constants
/////////////////////////////////////////////
function numbers(){

dec0 = 0;
/*     ^ meta.number.integer.decimal constant.numeric.value */
/*      ^ punctuation.terminator - constant */
dec1 = 1234567890;
/*     ^^^^^^^^^^ meta.number.integer.decimal constant.numeric.value */
/*               ^ punctuation.terminator - constant */

dec2 = 1234567890s0f;
/*     ^ meta.number.integer.decimal constant.numeric.value */
/*               ^^^ invalid.illegal.numeric.suffix */
/*                  ^ punctuation.terminator - constant */

oct1 = 01234567;
/*     ^^^^^^^^ meta.number.integer.octal */
/*     ^ constant.numeric.base */
/*      ^^^^^^^ constant.numeric.value */
/*             ^ punctuation.terminator - constant */

hex1 = 0x0+0xF

hex1 = 0x0123456789abcdef_4uz;
/*     ^^^^^^^^^^^^^^^^^^ meta.number.integer.hexadecimal */
/*                       ^^^^ invalid.illegal.numeric.suffix */
/*                           ^ punctuation.terminator - constant */

f = 1.1+1.1e1+1.1e-1;
/*  ^^^ meta.number.float.decimal */
/*  ^^^ constant.numeric.value */
/*   ^ punctuation.separator.decimal */
/*     ^ keyword.operator.arithmetic */
/*      ^^^^^ meta.number.float.decimal */
/*      ^^^^^ constant.numeric.value */
/*       ^ punctuation.separator.decimal */
/*           ^ keyword.operator.arithmetic */
/*            ^^^^^^ meta.number.float.decimal */
/*            ^^^^^^ constant.numeric.value */
/*             ^ punctuation.separator.decimal */
/*                  ^ punctuation.terminator - constant */

f = 1.+1..;
/*  ^^ meta.number.float.decimal */
/*  ^^ constant.numeric.value */
/*   ^ punctuation.separator.decimal */
/*    ^ keyword.operator.arithmetic */
/*     ^ meta.number.integer.decimal */
/*     ^ constant.numeric.value */
/*      ^^ invalid.illegal.syntax */
/*        ^ punctuation.terminator - constant */

}
/////////////////////////////////////////////
// Control Keywords
/////////////////////////////////////////////


function control_keywords()
{
  if (x < 5)
  /* <- keyword.control */
  {}
  else
  /* <- keyword.control */
  {}

  switch (x)
  /* <- keyword.control */
  {
  case 1:
  /* <- keyword.control */
      break;
      /* <- keyword.control.flow.break */
  default:
  /* <- keyword.control */
      break;
      /* <- keyword.control.flow.break */
  }

  do
  /* <- keyword.control */
  {
      if (y == 3)
          continue;
          /* <- keyword.control.flow.continue */
  } while (y < x);
  /*^ keyword.control */

  switch (a) {
      case 1: break;
  /*        ^ punctuation.separator */
      case 100 - 10: break;
  /*               ^ punctuation.separator */
      default: break;
  /*         ^ punctuation.separator */
  }

  return 123;
  /* <- keyword.control.flow.return */
}
