from Monopoly import Monopoly

N_PROPERTIES = 20
N_SIMULATIONS = 300
N_TIME_OUT = 1000

if __name__ == '__main__':
    Monopoly(N_SIMULATIONS, N_TIME_OUT, N_PROPERTIES).run()