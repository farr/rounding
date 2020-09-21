import numpy as np

def round_consistently(values, min_sig_digits=2, return_least_sig=False):
    """Returns `values` rounded consistently.

    The return values will all have *at least* `min_sig_digits`, and will be
    rounded at the same decimal place.

    :param values: Sequence of values to be rounded.

    :param min_sig_digits: Minimum number of significant figures to preserve for
      any value.

    :param return_least_sig: If `True` return both the rounded values and the
      least-significant digit in the rounding.

    :return: `rounded_values` or (`rounded_values, least_sig_digit`) depending
      on the `return_least_sig` flag.

    Examples:
        >>> import numpy as np
        >>> x, y, z = (1.0584378784847064, -0.8138475623409628, -0.6127108398864638)

        >>> round_consistently([x,y,z])
        [1.06, -0.81, -0.61]

        >>> round_consistently([x,y,0.01*z])
        [1.0584, -0.8138, -0.0061]

        >>> round_consistently([100*x,y,z])
        [105.84, -0.81, -0.61]

        >>> round_consistently([x,y,z], min_sig_digits=4)
        [1.0584, -0.8138, -0.6127]

        >>> round_consistently(1e30*np.array([x,y,z]))
        [1.06e+30, -8.099999999999999e+29, -6.1e+29]

        >>> round_consistently([x,y,z], return_least_sig=True)
        ([1.06, -0.81, -0.61], -2)
    """
    most_sig_pow_10 = [int(np.floor(np.log10(np.abs(v)))) for v in values]
    round_digit = np.min(most_sig_pow_10) - min_sig_digits + 1

    rounded_values = [round(v, -round_digit) for v in values]
    if return_least_sig:
        return rounded_values, round_digit
    else:
        return rounded_values

def center_and_range_latex(c, l, h, min_sig_digits=2):

    r"""Return a LaTeX string which is x^{+(h-c)}_{-(c-l)} giving a central
    value and (incremental) range rounded appropriately.

    :param c: The central value.

    :param l: The lower value (not the increment!).

    :param h: The upper value.

    :param min_sig_digits: The minimum number of significant digits each of the
       three formatted numbers should carry.


    Examples:

        >>> import numpy as np
        >>> h, l, c = (1.0584378784847064, -0.8138475623409628, -0.6127108398864638)

        >>> center_and_range_latex(c, l, h)
        '-0.61^{+1.67}_{-0.20}'

        >>> center_and_range_latex(c, l, h, min_sig_digits=4)
        '-0.6127^{+1.6711}_{-0.2011}'

        >>> center_and_range_latex(1e3*c, 1e3*l, 1e3*h)
        '-610^{+1670}_{-200}'
    """

    upper = h - c
    lower = c - l

    (c, l, h), n = round_consistently([c, upper, lower], min_sig_digits=min_sig_digits, return_least_sig=True)

    if n < 0:
        # Then we need to tell the f format string about it.
        nf = abs(n)
    else:
        nf = 0

    return '{{:.{:d}f}}^{{{{+{{:.{:d}f}}}}}}_{{{{-{{:.{:d}f}}}}}}'.format(nf, nf, nf).format(c, l, h)
