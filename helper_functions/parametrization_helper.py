from blueprints.codes.eurocode.exposure_classes import Exposure


def get_environment_description(exposure: Exposure, environment: str) -> str:
    """Get the description of the environment based on the exposure class.

    Parameters
    ----------
        exposure (Exposure): the exposure class
        environment (str): the environment

    Returns
    -------
        str: the description of the environment based on the exposure class
    """
    return exposure(environment).description_of_the_environment()
