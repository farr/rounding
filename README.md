# Rounding Consistently for Presentation

Here is a very simple code for rounding and formatting numbers for presentation
and publication (e.g. for presenting credible intervals or measurements and +/-
uncertainty).  It implements the following algorithm:

1. All numbers in a group should be rounded to the same decimal place.
1. Each number in the group should carry *at least* two significant digits.
1. The minimum number of digits should be presented consistent with the first two rules.

The module can also produce LaTeX code for the commonly-used X^{+Y}_{-Z} presentation format.
