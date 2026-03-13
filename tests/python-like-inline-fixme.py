"""This file contains test samples for the Python-like inline comments with
fixme.
"""

##############################################################################
# Matching samples ([M]atching)                                              #
##############################################################################

# SAMPLE M0.0: Nominal inline comment with trigger text at the beginning.
# FIXME: nominal inline comment M0.0

# SAMPLE M0.1: Nominal inline comment with trigger text at the beginning.
#    Double quote version.
"""FIXME: nominal inline comment M0.1"""

# SAMPLE M0.2: Nominal inline comment with trigger text at the beginning.
#    Single quote version.
'''FIXME: nominal inline comment M0.2'''


# SAMPLE M3.0: Added space around the beginning and end of the inline
#   comment. 4 leading spaces.
# vv Spaces here
	# FIXME: one-line block comment. M3.0

# SAMPLE M3.1: Added space around the beginning and end of the inline
#   comment. 4 leading spaces.
# vv Spaces here
    """ FIXME: one-line block comment. M3.1 """

# SAMPLE M3.2: Added space around the beginning and end of the inline
#   comment. 4 leading spaces.
# vv Spaces here
    ''' FIXME: one-line block comment. M3.2 '''


# SAMPLE M4.0: Added junk before the beginning and after the end of the
#   inline comment.
def foo() -> None:    # FIXME: block comment after stuff. M4.0 # random note for future devs
    pass

# SAMPLE M4.1: Added junk before the beginning and after the end of the
#   one-line block comment.
def foo() -> None:    """ FIXME: block comment after stuff. M4.1 """ # random note for future devs
    pass

# SAMPLE M4.2: Added junk before the beginning and after the end of the
#   one-line block comment.
def foo() -> None:    ''' FIXME: block comment after stuff. M4.2 ''' # random note for future devs
    pass


# SAMPLE M6.0: An inline comment with extra whitespace before the trigger text.
#   Mixed tabs and spaces.
#    vvvv Tab here
    #	  FIXME: Random whitespaces before trigger text. M6.0
#^^Here ^^ Spaces here

# SAMPLE M6.1: An inline comment with extra whitespace before the trigger text.
#   Mixed tabs and spaces.
#     vv Tab here
   """ 	  FIXME: Random whitespaces before trigger text. M6.1"""
#^^Here ^^ Spaces here

# SAMPLE M6.2: An inline comment with extra whitespace before the trigger text.
#   Mixed tabs and spaces.
#     vv Tab here
   ''' 	  FIXME: Random whitespaces before trigger text. M6.2'''
#^^Here ^^ Spaces here


# SAMPLE M7.0: An inline comment without whitespace before or after the trigger
#   text.
#FIXME

# SAMPLE M7.1: An inline comment without whitespace before or after the trigger
#   text.
"""FIXME"""

# SAMPLE M7.2: An inline comment without whitespace before or after the trigger
#   text.
'''FIXME'''


# SAMPLE M8.0: An inline comment with whitespace before the trigger text.
# FIXME

# SAMPLE M8.1: An inline comment with whitespace before and after the trigger
#   text.
""" FIXME """

# SAMPLE M8.2: An inline comment with whitespace before and after the trigger
#   text.
''' FIXME '''


# SAMPLE M9: This is an inline comment but it has the closing of a block
#   comment. That doesn't matter.
# AKA S1 in the block comment tests
# FIXME: inline comment with block ending */


##############################################################################
# Non-matching samples ([S]kipped)                                           #
##############################################################################

# SAMPLE S0.0: This is an multi-line block comment not an inline comment.
""" Some helpful text
FIXME: Multiple inline comments S0.0
"""

# SAMPLE S0.1: This is an multi-line block comment not an inline comment.
''' Some helpful text
FIXME: Multiple inline comments S0.1
'''

# SAMPLE S2: This is an inline comment with junk in front of the trigger text.
# This isn't intended but it's a limit of the current implementation.
# fooFIXME: This should not match. S2

# SAMPLE S(-1): Last one to make syntax highlighting wackyness less obnoxious.
#   Malformed block comment. No closing so it should not match.
''' FIXME: opened but not closed block comment S(-1)

# Tabs vs spaces is important to the tests so don't mangle either of them.
# vim: set tabstop=4 shiftwidth=4 noexpandtab
