
from typing import List


from garak.generators.base import Generator


class Arjen(Generator):
    """This generator always returns the empty string."""

    supports_multiple_generations = True
    generator_family_name = "Arjen"
    name = "Arjen"

    def _call_model(self, prompt: str, generations_this_call: int = 1) -> List[str]:
        return [""] * generations_this_call

