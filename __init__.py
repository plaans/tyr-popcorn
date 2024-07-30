from fractions import Fraction
from typing import Dict
from tyr.planners.model.apptainer_planner import ApptainerPlanner


# pylint: disable=too-many-ancestors
class PopcornPlanner(ApptainerPlanner):
    """The Popcorn planner wrapped into local apptainer planner."""

    def _file_extension(self) -> str:
        return "pddl"

    def _get_apptainer_file_name(self) -> str:
        return "popcorn.sif"

    def _get_engine_epsilon(self) -> Fraction:
        return Fraction(1, 1000)

    def _get_write_domain_options(self) -> Dict[str, bool]:
        opts = super()._get_write_domain_options()
        opts["control_support"] = True
        opts["force_predicate"] = True
        return opts

    def _starting_plan_str(self) -> str:
        return "; Cost"

    def _ending_plan_str(self) -> str:
        return "\n"

    def _parse_plan_line(self, plan_line: str) -> str:
        return plan_line


__all__ = ["PopcornPlanner"]
