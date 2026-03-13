/* This file contains test samples for the C-like block comments with 
 *   debug.
 */

/****************************************************************************/
/* Matching samples ([M]atching)                                            */
/****************************************************************************/

// SAMPLE M0: Nominal block comment with trigger text at the beginning.
/* DEBUG: nominal block comment
 *
 *  This should match the debug block comment regex
 *
 */

// SAMPLE M1: A block comment with the trigger text a few lines into it.
/* This should match the debug block comment regex
 *
 * DEBUG: mid-block comment
 *
 */

// SAMPLE M2: A one-line block syntax comment with the trigger word at the
//   beginning.
/* DEBUG: one-line block comment. This should match the debug block comment regex */


// SAMPLE M3.0: Added space around the beginning and end of the block
//   comment. 4 leading spaces.
    /* DEBUG: one-line block comment. M3.0 */

// SAMPLE M3.1: Added tab around the beginning of the block
//   comment. 1 leading tab. Mixed tabs and spaces.
// v Tab here
	/* DEBUG: Block comment with a tab before. M3.1 */


// SAMPLE M4: Added junk before the beginning and after the end of the one-line block
//   comment.
char *foo;    /* DEBUG: block comment after stuff. M4 */ # random note for future devs


// SAMPLE M5: Added junk before the beginning of the multi-line block
//   comment.
char *bar;  /* DEBUG: Stuff before a block comment shouldn't matter.

    M5
    */


/****************************************************************************/
/* Non-matching samples ([S]kipped)                                         */
/****************************************************************************/

// SAMPLE S0: This is an inline comment not a block comment.
// This should *NOT* match the debug block comment regex
// DEBUG: multiple inline comments
//

// SAMPLE S1: This is an inline comment not a block comment but it has the 
//   closing of a block comment.
// This should *NOT* match the debug block comment regex
// DEBUG: inline comment with block ending */

// SAMPLE S2: Malformed block comment. No closing so it should not match.
// This should *NOT* match the debug block comment regex
/* DEBUG: opened but not closed block comment


// Tabs vs spaces is important to the tests so don't mangle either of them.
// vim: set tabstop=4 shiftwidth=4 noexpandtab
