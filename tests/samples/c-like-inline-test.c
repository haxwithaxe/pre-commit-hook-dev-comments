/* This file contains test samples for the C-like inline comments with
 *   test.
 */

/****************************************************************************/
/* Matching samples ([M]atching)                                            */
/****************************************************************************/

// SAMPLE M0.0: Nominal inline comment with trigger text at the beginning.
// TEST: nominal inline comment M0.0

// SAMPLE M0.1: Nominal inline comment with trigger text at the beginning. Double quote version.
/* TEST: nominal inline comment M0.1 */


// SAMPLE M3.0: Added space around the beginning and end of the inline
//   comment. 4 leading spaces.
//vv Spaces here
    // TEST: one-line block comment. M3.0

// SAMPLE M3.1: Added space around the beginning and end of the inline
//   comment. 4 leading spaces.
//vv Spaces here
    /* TEST: one-line block comment. M3.1 */


// SAMPLE M4.0: Added junk before the beginning and after the end of the one-line block
//   comment.
char *foo;    // TEST: block comment after stuff. M4.0 // random note for future devs

// SAMPLE M4.1: Added junk before the beginning and after the end of the one-line block
//   comment.
char *foo;    /* TEST: block comment after stuff. M4.1 */ // random note for future devs


// SAMPLE M6.0: An inline comment with extra whitespace before the trigger text.
//   Mixed tabs and spaces.
//    vvvv Tab here
    //	  TEST: Random whitespaces before trigger text. M6.0
//^^Here ^^ Spaces here

// SAMPLE M6.1: An inline comment with extra whitespace before the trigger text.
//   Mixed tabs and spaces.
//   vvv Tab here
   /* 	  TEST: Random whitespaces before trigger text. M6.1*/
//^^Here^^ Spaces here


// SAMPLE M7.0: An inline comment without whitespace before or after the trigger text.
//TEST

// SAMPLE M7.1: An inline comment without whitespace before or after the trigger text.
/*TEST*/


// SAMPLE M8.0: An inline comment with whitespace before the trigger text.
// TEST

// SAMPLE M8.1: An inline comment with whitespace before and after the trigger text.
/* TEST */


// SAMPLE M9: This is an inline comment but it has the closing of a block comment. That doesn't matter.
// AKA S1 in the block comment tests
// TEST: inline comment with block ending */


/****************************************************************************/
/* Non-matching samples ([S]kipped)                                         */
/****************************************************************************/

// SAMPLE S0.0: This is a multi-line block comment not an inline comment. Leading * before trigger word.
/* Some helpful text
 * TEST: Multiple inline comments S0.0
 */

// SAMPLE S0.1: This is a multi-line block comment not an inline comment. No leading * before trigger word.
/* Some helpful text
TEST: Multiple inline comments S0.1
*/


// SAMPLE S2.0: This is an inline comment with junk in front of the trigger text.
// This isn't intended but it's a limit of the current implementation.
// fooTEST: This should not match. S2.0

// SAMPLE S2.1: This is an inline comment with junk in front of the trigger text.
// This isn't intended but it's a limit of the current implementation.
/* fooTEST: This should not match. S2.1 */


// SAMPLE S(-1): Last one to make syntax highlighting wackyness less obnoxious.
//   Malformed block comment. No closing so it should not match.
/* TEST: opened but not closed inline block-syntax comment S(-1)

// Tabs vs spaces is important to the tests so don't mangle either of them.
// vim: set tabstop=4 shiftwidth=4 noexpandtab
