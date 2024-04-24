# ConditionalSubstitution

Allows you to choose between two substitutions using a condition.

```python
from launch import LaunchDescription
from launch.actions import LogInfo, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from conditional_substitution import ConditionalSubstitution


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("some_argument"),
            LogInfo(
                msg=ConditionalSubstitution(
                    IfCondition(LaunchConfiguration("some_argument")),
                    "some_argument evaluated to true!",
                    "some_argument evaluated to false!",
                )
            ),
        ]
    )
```