"""
Exercise 55: Wavelengths of Visible Light

The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

    Color   Wavelength (nm)
    ------------------------
    Violet 380 to less than 450
    Blue    450 to less than 495
    Green   495 to less than 570
    Yellow 570 to less than 590
    Orange 590 to less than 620
    Red     620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""



def main():
    r"""
    ***************************************************************************
    Exercise 55: Wavelengths of Visible Light
    ***************************************************************************

    >>> from testing import *
    >>> inputs = ['400', '460', '510', '580', '605', '720', '760']
    >>> batch_size = 1
    >>> regex = r'violet|blue|green|yellow|orange|red|non-visible'
    >>> stdout, outputs, tests = simulate_input(main, inputs, batch_size, regex)

    **************************************************************************

    >>> tests[0]
    ['violet']

    >>> tests[1]
    ['blue']

    >>> tests[2]
    ['green']

    >>> tests[3]
    ['yellow']

    >>> tests[4]
    ['orange']

    >>> tests[5]
    ['red']

    >>> tests[6]
    ['non-visible']

    """
    wavelength = int(input("Enter a wave length:  "))
    if wavelength >= 380 and wavelength <= 450:
        print("Violet")
    elif wavelength >= 450 and wavelength <= 495:
        print("Blue")
    elif wavelength >= 495 and wavelength <= 570:
        print("Green")
    elif wavelength >= 570 and wavelength <= 590:
        print("Yellow")
    elif wavelength >= 590 and wavelength <= 620:
        print("Orange")
    elif wavelength >= 620 and wavelength <= 750:
        print("Red")
    else:
        print("Error the wavelength is outside of my spectrum!(non-visible)")


if __name__ == "__main__":
    import doctest

    doctests = doctest.testmod()
    print("=" * 75)
    if doctests.failed == 0:
        print("All tests passed!")
    else:
        print(f"{doctests.failed} test(s) failed!")
    print("=" * 75)

    print("main():")
    main()
