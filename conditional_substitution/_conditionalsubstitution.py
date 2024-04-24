from typing import Text

from launch import (  # pyright: ignore [reportMissingTypeStubs]
    LaunchContext,
    Substitution,
    Condition,
    SomeSubstitutionsType,
)
from launch.utilities import (  # pyright: ignore [reportMissingTypeStubs]
    normalize_to_list_of_substitutions,
    perform_substitutions,
)


class ConditionalSubstitution(Substitution):
    """
    Ternary operator for ROS 2 launch substitutions.

    Substitution which resolves to one of two other substitutions depending on a condition.
    result = condition ? then_s : else_s
    """

    def __init__(
        self,
        condition: Condition,
        then_s: SomeSubstitutionsType,
        else_s: SomeSubstitutionsType,
    ):
        """
        Create a ConditionalSubstitution.

        :param then_s: Resulting substitution when condition evaluates to true
        :param else_s: Resulting substitution when condition evaluates to false
        """
        self.condition = condition
        self.then_s = normalize_to_list_of_substitutions(then_s)
        self.else_s = normalize_to_list_of_substitutions(else_s)

    def perform(self, context: LaunchContext) -> Text:
        if self.condition.evaluate(context):
            return perform_substitutions(context, self.then_s)
        else:
            return perform_substitutions(context, self.else_s)
