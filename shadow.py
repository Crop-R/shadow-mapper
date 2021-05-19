import numpy as np
import c_shadowmap

from solar import to_juliandate, sun_vector


def calculate(date_time, lat, lng, dsm, resolution, view_alt, timezone=0, scaled=False):
    """Calculate the shadow that is cat for a digital elevation model on it self.
    :param date_time: utc timestamp, time of observation
    :param latitude: latitude of observation
    :param longitude: longitude of observation
    :param dsm: Digital surface model (2-dimensional numpy array containing height in meters)
    :param resolution: resolution of the DSM
    :param view_altitude: altitude for which the shadow should be calculated
    :param timezone: timezone hour offset relative to UTC (default 0
    :param scaled: indicates if value for lit area should be scaled for the sun angle.
    Useful if you want to calculate shadows for multiple points of time and to find out relative incoming solar radiation.
    :return: 2-dimensional array containing 0 for shadowed pixels and a number for lit pixels.
    """
    jd = to_juliandate(date_time)
    sv = sun_vector(jd, lat, lng, timezone)
    shadow = c_shadowmap.calculate(dsm.astype(float), sv[0], sv[1], sv[2] * resolution, view_alt, np.amax(dsm))
    if scaled:
        return shadow * sv[2]
    else:
        return shadow
