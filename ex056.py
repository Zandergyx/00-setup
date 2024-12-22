"""
Exercise 56: Frequency to Name

Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

    Name              Frequency Range (Hz)
    ---------------------------------------
    Radio Waves       Less than 3 × 10^9
    Microwaves        3 × 10^9 to less than 3 × 10^12
    Infrared Light    3 × 10^12 to less than 4.3 × 10^14
    Visible Light     4.3 × 10^14 to less than 7.5 × 10^14
    Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
    X-Rays            3 × 10^17 to less than 3 × 10^19
    Gamma Rays        3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays the name of the radiation as part of an appropriate message.
"""


def main():
    r"""
    ***************************************************************************
    Exercise 56: Frequency to Name
    ***************************************************************************

    >>> from testing import *
    >>> inputs = ['2.5e9', '5e10', '3.5e13', '5e14', '2.9e17', '1e18', '4e19']
    >>> batch_size = 1
    >>> regex = r'radio|microwaves|infrared|visible|ultraviolet|x-rays|gamma'
    >>> stdout, outputs, tests = simulate_input(main, inputs, batch_size, regex)

    **************************************************************************

    >>> tests[0]
    ['radio']

    >>> tests[1]
    ['microwaves']

    >>> tests[2]
    ['infrared']

    >>> tests[3]
    ['visible']

    >>> tests[4]
    ['ultraviolet']

    >>> tests[5]
    ['x-rays']

    >>> tests[6]
    ['gamma']

    """
    radiation = float(input("Enter a wave length:  "))
    if radiation <= (3*10**9):
        print("Radio Waves")
    elif radiation >= (3*10**9) and radiation <= (2*10**12):
        print("Microwaves")
    elif radiation >= (3*10**12) and radiation <= (4.3*10**14):
        print("Infrared Light")
    elif radiation >= (4.3*10**14) and radiation <= (7.5*10**14):
        print("Visible Light")
    elif radiation >= (7.5*10**14) and radiation <= (3*10**17):
        print("Ultraviolet Light")
    elif radiation >= (3*10**17) and radiation <= (3*10**19):
        print("X-Rays")
    elif radiation >= (3*10**19):
        print("Gamma Rays")
    else:
        print("Error the radiation is outside of my spectrum!")


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
