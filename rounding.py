import numpy as np

def round_consistently(values, min_sig_digits=2):
    """Returns `values` rounded consistently.

    The return values will all have *at least* `min_sig_digits`, and will be
    rounded at the same decimal place.

    :param values: Sequence of values to be rounded.

    :param min_sig_digits: Minimum number of significant figures to preserve for
      any value.

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
    """
    most_sig_pow_10 = [int(np.floor(np.log10(np.abs(v)))) for v in values]
    round_digit = np.min(most_sig_pow_10) - min_sig_digits + 1

    return [round(v, -round_digit) for v in values]
