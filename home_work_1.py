from scipy.constants import pi, epsilon_0, electron_volt, elementary_charge


def question_1():
    """
    Calculate the electron Debye radius and number of particles in Debye sphere for
    the following electron densities and temperatures in:
        a) thermonuclear plasma:
            n = 1.0e21 #1/m^3
            kT = 1.0e4 #eV
        b) glow discharge:
            n = 1.0e16 #1/cm^3
            n = 1.0e22 #1/m^3
            kT = 2.0 #eV
        c) solar corona:
            n = 1.0e15 #1/m^3
            kT = 1.0e2 #eV
    """

    def r_Debye(n, kT):
        """
        the electron Debye radius
        :param n: plasma density [1/m^3]
        :param kT: plasma temperature [eV]
        :return: the electron Debye radius [m]
        """
        l = (epsilon_0 * kT * electron_volt / (n * elementary_charge ** 2)) ** 0.5
        return l

    def N_Debye(n, kT):
        """
        number of particles in Debye sphere
        :param n: plasma density [1/m^3]
        :param kT: plasma temperature [eV]
        :return: number of particles in Debye sphere
        """
        N = n * 4.0 / 3.0 * pi * r_Debye(n, kT) ** 3
        return N

    variation_dict = {
        'thermonuclear plasma': {
            'n': 1.0e21,
            'kT': 1.0e4
        },
        'glow discharge': {
            'n': 1.0e22,
            'kT': 2.0
        },
        'solar corona': {
            'n': 1.0e15,
            'kT': 1.0e2
        }
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\nn = {variation["n"]} 1/m^3; kT = {variation["kT"]} eV')
        print(f'r_Debye = {r_Debye(variation["n"], variation["kT"])} m')
        print(f'N_Debye = {N_Debye(variation["n"], variation["kT"])} particles\n')


question_1()
