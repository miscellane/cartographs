import os
import sys
import logging

import pandas as pd


def main():

    # States
    print('\nStates')
    states: pd.DataFrame = boundaries.states(year=settings.latest)
    logger.info(states.info())

    # Counties
    print('\nCounties')
    counties = boundaries.counties(year=settings.latest)
    logger.info(counties.info())


if __name__  == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import cartographs.boundaries.us.settings
    import cartographs.boundaries.us.boundaries

    settings = cartographs.boundaries.us.settings.Settings()
    boundaries = cartographs.boundaries.us.boundaries.Boundaries(crs=settings.crs)

    main()
