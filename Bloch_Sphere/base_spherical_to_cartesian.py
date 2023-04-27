def spherical_to_cartesian(spherical: Sequence[float]) -> np.ndarray:
    Returns a numpy array ``[x, y, z]`` based on the spherical
    coordinates given.

    Parameters
    ----------
    spherical
        A list of three floats that correspond to the following:

        r - The distance between the point and the origin.

        theta - The azimuthal angle of the point to the positive x-axis.

        phi - The vertical angle of the point to the positive z-axis.
    
    r, theta, phi = spherical
    return np.array(
        [
            r * np.cos(theta) * np.sin(phi),
            r * np.sin(theta) * np.sin(phi),
            r * np.cos(phi),
        ],
    )