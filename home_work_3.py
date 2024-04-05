from scipy.constants import pi, epsilon_0, electron_volt, elementary_charge, proton_mass, speed_of_light, mu_0, m_e
import numpy as np


def question_1():
    """
    EM wave in plasma
    :return:
    """

    def v_phase(_l_, n):
        """
        Phase velocity
        :param _l_: nm
        :param n: cm^-3
        :return: m/s
        """
        lambda_m = _l_ * 1.0e-9
        n_m_3 = n * 1.0e6
        v = np.sqrt(
            elementary_charge ** 2 / 4 / pi ** 2 / speed_of_light ** 2 / epsilon_0 / m_e * n_m_3 * lambda_m ** 2 + 1)-1
        return v

    variation_dict = {
        'Plasma - wave 1': {
            'lambda': 500,  #
            'n': 1.0e17,  # cm-3
        },
        'Plasma - wave 2': {
            'lambda': 500,  #
            'n': 1.0e19,  # cm-3
        },
    }
    for key, variation in variation_dict.items():
        print(
            f'{key}:\nlambda = {variation["lambda"]:3.2e} nm; n = {variation["n"]:3.2e} cm^-3;')
        print(f'v = {v_phase(variation["lambda"], variation["n"]):3.2e} m/s')


print('quastion 1')
question_1()


def question_3():
    """
    total reflection of EM wave
    :return:
    """

    def n_min(alfa, f):
        """
        minimal density of full reflection
        :param alfa: degrees
        :param f: GHz
        :return: m^-3
        """
        f_Hz = f * 1.0e9
        alfa_rad = alfa * pi / 180.0
        n = 4 * pi ** 2 * epsilon_0 * m_e / elementary_charge ** 2 * f_Hz ** 2 * (1.0 - np.cos(alfa_rad) ** 2)
        return n

    variation_dict = {
        'EM_wave': {
            'angle': 45,  # deg
            'f': 1.0,  # GHz
        },
    }
    for key, variation in variation_dict.items():
        print(
            f'{key}:\nangle = {variation["angle"]:3.2e} deg; f = {variation["f"]:3.2e} GHz;')
        print(f'n = {n_min(variation["angle"], variation["f"]):3.2e} m^-3')


print('quastion 3')
question_3()
