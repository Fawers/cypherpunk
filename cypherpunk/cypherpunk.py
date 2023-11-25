from .step_calculator import StepCalculator, NegatedStepper


class Cypherpunk:
    def __init__(self, alphabet: str):
        alpha_set = set(alphabet)

        if len(alphabet) != len(alpha_set):
            # TODO criar um erro específico para o cypherpunk
            raise ValueError(f"alfabeto contém duplicatas: {alphabet!r}")

        self.__alphabet = alphabet

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

        def iter():
            alphabet_size = len(self.__alphabet)
            current_step = initial_step

            for c in msg:
                pos_alpha = self.__alphabet.find(c)
                next_pos = (pos_alpha + current_step) % alphabet_size
                new_c = self.__alphabet[next_pos]
                yield new_c
                current_step = stepper.next(current_step)

        cyphered = ''.join(iter())
        return cyphered

    def _check_msg_chars_exist_in_alphabet(self, msg: str):
        all_chars_exist = all(c in self.__alphabet for c in msg)

        if not all_chars_exist:
            raise Exception("alguns chars não existem no alfabeto")
