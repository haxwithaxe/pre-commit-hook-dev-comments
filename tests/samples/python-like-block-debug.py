"""This file contains test samples for the Python-like block comments with
debug.
"""


##############################################################################
# Matching samples ([M]atching)                                              #
##############################################################################

# SAMPLE M0.0: Nominal block comment with trigger text at the beginning. Double
#   quote version. Mixed leading tabs and spaces.
"""DEBUG: nominal block comment

This should match the debug block comment regex. Double quotes.
	<Tab here M0.0
"""

# SAMPLE M0.1: Nominal block comment with trigger text at the beginning. Single
#   quote version. Mixed leading tabs and spaces.
'''DEBUG: nominal block comment

This should match the debug block comment regex. Single quotes.
	<Tab here M0.1
'''


# SAMPLE M1.0.: A block comment with the trigger text a few lines into it. Mixed tabs and spaces.
"""This should match the debug block comment regex

DEBUG: mid-block comment. Double quotes.
	<Tab here M1.0
"""

# SAMPLE M1.1.: A block comment with the trigger text a few lines into it. Single quote version. Mixed tabs and spaces.
'''This should match the debug block comment regex

DEBUG: mid-block comment. Single quotes.
	<Tab here M1.1
'''

# SAMPLE M2.0: A one-line block syntax comment with the trigger word at the
#   beginning. Double quote version.
"""DEBUG: one-line block comment. M2.0"""

# SAMPLE M2.1: A one-line block syntax comment with the trigger word at the
#   beginning. Single quote version.
'''DEBUG: one-line block comment. M2.1'''


# SAMPLE M3.0: Added space around the beginning and end of the block
#   comment. 4 leading spaces.
    """ DEBUG: one-line block comment. M3.0 """

# SAMPLE M3.1: Added tab around the beginning of the block
#   comment. 1 leading tab. Mixed tabs and spaces.
# v Tab here
	""" DEBUG: Block comment with a tab before. M3.1 """


# SAMPLE M4: Added junk before the beginning and after the end of the one-line block
#   comment.
def foo() -> None:    """ DEBUG: block comment after stuff. M4 """ # random note for future devs
    pass

# SAMPLE M5: Added junk before the beginning of the multi-line block
#   comment.
SOME_VAR = 42  """ DEBUG: Stuff before a block comment shouldn't matter.

    M5
    """

# SAMPLE M6.: A block comment with extra whitespace before the trigger text
#   mid-block. Mixed tabs and spaces.
'''This should match the debug block comment regex
vvvv Tab here
	  DEBUG: mid-block comment. Single quotes.
    ^^ Space here
	<Tab here M1.1
'''


##############################################################################
# Non-matching samples ([S]kipped)                                           #
##############################################################################

# SAMPLE S0: This is an inline comment not a block comment.
# Some helpful text
# DEBUG: Multiple inline comments S0
#

# SAMPLE S1: This is an inline comment not a block comment but it has the
#   closing of a block comment.
# DEBUG: inline comment with block ending S1 '''

# SAMPLE S2: This is a block comment with junk in front of the trigger text.
# This isn't intended but it's a limit of the current implementation.
"""fooDEBUG: This should not match. S2"""

# SAMPLE S(-1): Last one to make syntax highlighting wackyness less obnoxious.
#   Malformed block comment. No closing so it should not match.
''' DEBUG: opened but not closed block comment S(-1)

# Tabs vs spaces is important to the tests so don't mangle either of them.
# vim: set tabstop=4 shiftwidth=4 noexpandtab
