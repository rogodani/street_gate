from sim800l import Sim800L
from street_gate_opener import StreetGateOpener

gsm_connection = Sim800L()
gate = StreetGateOpener()

while True:
    incoming = gsm_connection.check_incoming()
    # print("-------> INCOME: ", incoming)
    # print('-------> INCOME TYPE', type(incoming))
    if incoming and gate.phone_number_validation(incoming):
        # print('IN IF')
        # print(' - - - - > validation:', gate.phone_number_validation(incoming))
        gate.open_gate()
        # print('$' * 20, '\nCALL FROM {}\n'.format(incoming), '$' * 20)
