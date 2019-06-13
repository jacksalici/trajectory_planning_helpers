import numpy as np


def calc_ax_profile(vx_profile: np.ndarray,
                    el_lengths: np.ndarray,
                    eq_length_output: bool = False) -> np.ndarray:
    """
    Created by:
    Alexander Heilmeier

    Documentation:
    Function calculates the acceleration profile for a given velocity profile.

    Inputs:
    vx_profile: array containing the velocity profile used as a basis for the acceleration calculations.
    el_lengths: array containing the element lengths between every point of the velocity profile.
    eq_length_output: assumes zero acceleration for the last point of the acceleration profile and therefore returns
                      len(ax_profile) == len(vx_profile). Without eq_length_output:
                      len(vx_profile) == len(ax_profile) + 1 == len(el_lengths) + 1
    """

    # check inputs
    if vx_profile.size != el_lengths.size + 1:
        raise ValueError("Array size of vx_profile should be 1 element bigger than el_lengths!")

    # calculate longitudinal acceleration profile array numerically: (v_end^2 - v_beg^2) / 2*s
    if eq_length_output:
        ax_profile = np.zeros(vx_profile.size)
        ax_profile[:-1] = (np.power(vx_profile[1:], 2) - np.power(vx_profile[:-1], 2)) / (2 * el_lengths)
    else:
        ax_profile = (np.power(vx_profile[1:], 2) - np.power(vx_profile[:-1], 2)) / (2 * el_lengths)

    return ax_profile


# testing --------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass