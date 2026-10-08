"""Threshold survival model with growing-degree-day (GDD) forcing."""

from importlib.resources import files


class ThreshSurvGDD:
    stan_file = files("phenosurv") / "stan" / "thresh-surv-gdd.stan"

    def print_code(self):
        """Print the model's Stan code."""
        print(self.stan_file.read_text())
