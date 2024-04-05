from scipy.constants import pi, epsilon_0, electron_volt, elementary_charge, proton_mass, speed_of_light, mu_0
import numpy as np


def question_4():
    """
    Polarization drift
    :return:
    """

    def n_e_dot_drift(J, B_z, E_dot):
        """
        density of plasma with polarization drift
        :param J:
        :param B_z:
        :param E_dot:
        :return:
        """
        ret = J * B_z ** 2 / (proton_mass * speed_of_light ** 2 * E_dot)
        return ret

    variation_dict = {
        'drifting plasma': {
            'B': 0.4,  # T
            'E_dot': 5.5e3,  # V*cm^-1*s^-1
            'J': 8.0e3  # A/m^2
        },
    }
    for key, variation in variation_dict.items():
        print(
            f'{key}:\nB = {variation["B"]:3.2e} T; E_dot = {variation["E_dot"]:3.2e} V*cm^-1*s^-1; J = {variation["J"]:3.2e} A/m^2')
        print(f'n = {n_e_dot_drift(variation["J"], variation["B"], variation["E_dot"]):3.2e} cm^-3')


print('question 4')
question_4()


def question_6():
    """
    Columb logarithm
    :return:
    """

    def lnL(n, kT):
        """

        :param n: cm-3
        :param kT: keV
        :return:
        """
        kT_J = kT * electron_volt * 1.0e3
        n_m = n * 1.0e6
        ret = np.log(6 * pi * epsilon_0 / elementary_charge ** 2 * np.sqrt(epsilon_0 / 2 / n_m) * kT_J ** 1.5)
        return ret

    variation_dict = {
        'plasma 1': {
            'n': 1.0e16,
            'kT': 0.3
        },
        'plasma 2': {
            'n': 1.0e16,
            'kT': 3
        },
        'plasma 3': {
            'n': 1.0e16,
            'kT': 30
        },
        'plasma 4': {
            'n': 1.0e16,
            'kT': 60
        }
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\nn = {variation["n"]:3.2e} cm-3; kT = {variation["kT"]:3.2e} eV')
        print(f'l_Columb = {lnL(variation["n"], variation["kT"]):3.2e}')


print('question 6')
question_6()


def question_2():
    """
    electrical drift
    :return:
    """

    def v_drift(T, a, B):
        """

        :param T: eV
        :param a: cm
        :param B: T
        :return:
        """
        ret = 2 * T / (a * 1.0e-2 * B * np.exp(1))
        return ret

    variation_dict = {
        'plasma 1': {
            'a': 1.0,
            'kT': 0.2,
            'B': 0.2
        }
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\na = {variation["a"]:3.2e} cm-3; kT = {variation["kT"]:3.2e} eV; B = {variation["B"]:3.2e} T')
        print(f'v_drift = {v_drift(variation["kT"], variation["a"], variation["B"]):3.2e} m/s')


print('question 2')
question_2()


def question_3():
    """
    drift
    :return:
    """

    def v_electrical(phi_0, I, r_wall, r_wire):
        """

        :param phi_0: [V]
        :param I: [A]
        :param r_wall: [cm]
        :param r_wire: [mm]
        :return:
        """
        r_wall_m = r_wall * 1.0e-2
        r_wire_m = r_wire * 1.0e-3
        ret = 2.0 * pi / mu_0 * phi_0 / np.log(r_wall_m / r_wire_m) / I
        return ret

    def v_gradient(phi_0, I, r_wall, r_wire, r_e):
        """

        :param phi_0: [V]
        :param I: [A]
        :param r_wall: [cm]
        :param r_wire: [mm]
        :param r_e: [cm]
        :return:
        """

        r_wall_m = r_wall * 1.0e-2
        r_wire_m = r_wire * 1.0e-3
        r_e_m = r_e * 1.0e-2
        ret = 2.0 * pi / mu_0 * phi_0 / np.log(r_wall_m / r_wire_m) / I * np.log(r_wall_m / r_e_m)
        return ret


    variation_dict = {
        'plasma 1': {
            'phi': 460.0,
            'I': 500.0,
            'r_wall': 10,
            'r_wire': 1.0,
            'r_e': 1.0,
        }
    }
    for key, variation in variation_dict.items():
        print(f'{key}:\n phi = {variation["phi"]:3.2e} V; I = {variation["I"]:3.2e} A; r_wall = {variation["r_wall"]:3.2e} cm; r_wire = {variation["r_wire"]:3.2e} mm;r_e = {variation["r_e"]:3.2e} cm;')
        print(f'v_electrical = {v_electrical(variation["phi"], variation["I"], variation["r_wall"], variation["r_wire"]):3.2e} m/s')
        print(f'v_gradient = {v_gradient(variation["phi"], variation["I"], variation["r_wall"], variation["r_wire"], variation["r_e"]):3.2e} m/s')

print('question 3')
question_3()
