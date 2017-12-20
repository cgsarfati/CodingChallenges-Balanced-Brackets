"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or < >.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    # store open/close brackets in a dict: K is close, V is open
    # convert openers to set for O1 runtime search

    # implement stack r/t FILO fitting balanced dynamic
    # if open, append to stack
    # if close
      # if empty stack, fail fast
      # if stack[-1] corresponds to closed bracket in dict, rm [-1]
    # after loop, if stack empty, means balanced

    # keep track of open/close relation
    closers = {")": "(", "]": "[", "}": "{", ">": "<"}

    # use set for 0(1) runtime search of openers
    openers = set(closers.values())

    # implement Stack to store openers, and rm them depending on closers
    openers_seen = []

    # loop through phrase to target brackets
    for char in phrase:

        # openers
        if char in openers:
            openers_seen.append(char)

        # closers
        elif char in closers:

            # FAIL-FAST: if empty stack, means closer too early
            if openers_seen == []:
                return False

            # if correct, rm last bracket + continue traversing
            if openers_seen[-1] == closers.get(char):
                openers_seen.pop()

            # FAIL-FAST: if mis-match b/w last opener and current closer
            else:
                return False

    # if traversal finished and stack ultimately empty, means balanced
    return openers_seen == []

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"
