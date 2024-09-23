class timeconvert:
    """
    A class to convert time formats

    Methods: 
    ------
    sec_min(seconds):
        Converts seconds to minutes
        
    min_hours

    """
    def sec_min(self ,seconds):
        """
        Convert seconds to minutes.

        Parameters:
        -----------
        seconds : int
            The number of seconds to convert.

        Returns:
        --------
        float
            The equivalent number of minutes.
        """
        return seconds / 60
    


    def min_hours(self, minutes):
        """
    Convert minutes to hours.

    Parameters:
    -----------
    minutes : float
        The number of minutes to convert.

    Returns:
    --------
    float
        The equivalent number of hours.
    """
        return minutes / 60
    

    def hours_days(self, hours):
        """
    Convert hours to days.

    Parameters:
    -----------
    hours : float
        The number of hours to convert.

    Returns:
    --------
    float
        The equivalent number of days.
    """
        return hours / 24
    
converter = timeconvert()
print(converter.sec_min(300))
print(converter.min_hours(300))
print(converter.hours_days(300))

print("Docstrings using doc_:")
print("Point.__doc__:")
print(timeconvert.__doc__)
print("\nPoint.__init__.__doc__:")
print(timeconvert.__init__.__doc__)
print("\nPoint.get_distance.__doc__:")
print(timeconvert.hours_days.__doc__)

    