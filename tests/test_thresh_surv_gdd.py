"""Tests for the ThreshSurvGDD model class (threshold survival model, GDD forcing)."""

import contextlib
import inspect
import io
import unittest

from phenosurv import ThreshSurvGDD


class TestThreshSurvGDDClass(unittest.TestCase):

    def test_is_a_class(self):
        self.assertTrue(inspect.isclass(ThreshSurvGDD))

    def test_can_instantiate_without_data(self):
        # Inspecting the Stan code should not require data.
        model = ThreshSurvGDD()
        self.assertIsInstance(model, ThreshSurvGDD)


class TestThreshSurvGDDPrintCode(unittest.TestCase):

    def setUp(self):
        self.model = ThreshSurvGDD()

    def _printed_code(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.model.print_code()
        return buffer.getvalue()

    def test_has_print_code_method(self):
        self.assertTrue(callable(getattr(self.model, "print_code", None)))

    def test_print_code_writes_to_stdout(self):
        self.assertNotEqual(self._printed_code().strip(), "")

    def test_printed_code_contains_stan_program_blocks(self):
        code = self._printed_code()
        for block in (
            "functions {",
            "data {",
            "transformed data {",
            "parameters {",
            "transformed parameters {",
            "model {",
            "generated quantities {",
        ):
            with self.subTest(block=block):
                self.assertIn(block, code)

    def test_printed_code_is_the_gdd_threshold_model(self):
        code = self._printed_code()
        self.assertIn("MODIFIED (THRESHOLDING) SURVIVAL MODEL w/ LINEAR (GDD) FORCING", code)
        for declaration in ("real T_base;", "real Psi0_bar;", "real<lower=0> sigma;"):
            with self.subTest(declaration=declaration):
                self.assertIn(declaration, code)


if __name__ == "__main__":
    unittest.main()
