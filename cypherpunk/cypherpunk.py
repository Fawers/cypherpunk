from .step_calculator import StepCalculator, NegatedStepper


class Cypherpunk:
    def __init__(self, alphabet: str):
        self.__alphabet = alphabet
        # TODO checar duplicatas no alfabeto

    def __iter__(self, msg: str, istep: int, sc: StepCalculator):
        # TODO consertar esse __iter__
        alphabet_size = len(self.__alphabet)
        current_step = istep

        for c in msg:
            pos_alpha = self.__alphabet.find(c)
            next_pos = (pos_alpha + current_step) % alphabet_size
            new_c = self.__alphabet[next_pos]
            current_step = sc.next(current_step)
            yield new_c

    # cypher.forth()
    def forth(self, msg: str, initial_step: int, stepper: StepCalculator):
        return self._cypher(
            msg, initial_step, stepper)

    # cypher.back()
    def back(self, msg: str, initial_step: int, stepper: StepCalculator):
        return self._cypher(
            msg, -initial_step,
            NegatedStepper(stepper))

    def _cypher(self, msg, initial_step, stepper: StepCalculator):
        self._check_msg_chars_exist_in_alphabet(msg)

        cyphered = ''.join(
            self.__iter__(msg, initial_step, stepper))
        return cyphered

    def _check_msg_chars_exist_in_alphabet(self, msg: str):
        all_chars_exist = all(c in self.__alphabet for c in msg)

        if not all_chars_exist:
            raise Exception("alguns chars não existem no alfabeto")
