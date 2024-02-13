from scipy.constants import pi, epsilon_0, electron_volt, elementary_charge, proton_mass


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


print('question 1')
question_1()


def question_3():
    """
    consider plasma with electron density of n_e = 1e10 cm^-3 and electron temperature of 1 eV. electrons are much warmer than ions.
    """

    def r_ee(n_e):
        """
        inter-electron distance in plasma
        :param n_e:
        electron density [cm^-3]
        :return:
        inter-electron distance [m]
        """
        return (n_e ** (-1 / 3)) * 1e-2





def question_5():
    """
    Calculate the Larmor radius for a 3.5 MeV He++ particle in an 8 Tesla DT fusion reaction.
    assume that V_|| is negligible.
    :return:
    """

    def r_Larmor(E, A, Z, B):
        """
        The Larmor radius
        :param E: particle energy [eV]
        :param A: particle mass [a.e.m.]
        :param Z: particle charge [e]
        :param B: magnetic field [Tl]
        :return: r_Larmor [m]
        """
        E_J = E * electron_volt
        M_kg = A * proton_mass
        Q_C = Z * elementary_charge
        r = (2 * E_J * M_kg) ** 0.5 / Q_C / B
        return r

    variation_dict = {
        'alpha particle fusion plasma': {
            'E': 3.5e6,
            'A': 4,
            'Z': 2,
            'B': 8
        }
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\nE = {variation["E"]} eV; A = {variation["A"]}; Z = {variation["Z"]}; B = {variation["B"]} Tl;')
        print(f'r_Larmor = {r_Larmor(variation["E"], variation["A"], variation["Z"], variation["B"])} m')


print('question 5')
question_5()
