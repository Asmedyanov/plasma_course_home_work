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
        print(f'{key}:\nn = {variation["n"]:3.2e} 1/m^3; kT = {variation["kT"]:3.2e} eV')
        print(f'r_Debye = {r_Debye(variation["n"], variation["kT"]):3.2e} m')
        print(f'N_Debye = {N_Debye(variation["n"], variation["kT"]):3.2e} particles\n')


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
        electron density [m^-3]
        :return:
        inter-electron distance [m]
        """
        return n_e ** (-1 / 3)

    def E_field(n_e):
        """
        :param n_e:
        electron density [m^-3]
        :return:
        electric field [V/m]
        """
        ret = elementary_charge * n_e * r_ee(n_e) / (2.0 * epsilon_0)
        return ret

    def W_potential(n_e):
        """
        :param n_e:
        electron density [m^-3]
        :return:
        potential energy [J/m^3]
        """
        ret = elementary_charge * n_e * E_field(n_e) * r_ee(n_e)
        return ret

    def W_kinetic(n_e, T_e):
        """

        :param n_e:
        electron density [m^-3]
        :param T_e:
        electron temperature [eV]
        :return:
        """
        ret = 3 / 2 * n_e * T_e * electron_volt
        return ret

    variation_dict = {
        'Question 3': {
            'n_e': 1.0e16,  # m^-3
            'kT': 1.0,  # eV
        },
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\nn = {variation["n_e"]:3.2e} 1/m^3; kT = {variation["kT"]:3.2e} eV')
        print(f'r_ee = {r_ee(variation["n_e"]):3.2e} m')
        print(f'E_field = {E_field(variation["n_e"]):3.2e} V/m\n')
        print(f'W_potential = {W_potential(variation["n_e"]):3.2e} J/m^3\n')
        print(f'W_kinetic = {W_kinetic(variation["n_e"], variation["kT"]):3.2e} J/m^3\n')
        print(
            f'W_kinetic/W_potential = {W_kinetic(variation["n_e"], variation["kT"]) / W_potential(variation["n_e"]):3.2e} J/m^3\n')


print('Question 3')
question_3()


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
        print(
            f'{key}:\nE = {variation["E"]:3.2e} eV; A = {variation["A"]:3.2e}; Z = {variation["Z"]:3.2e}; B = {variation["B"]:3.2e} Tl;')
        print(f'r_Larmor = {r_Larmor(variation["E"], variation["A"], variation["Z"], variation["B"]):3.2e} m')


print('question 5')
question_5()
