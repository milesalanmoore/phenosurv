"""Tests for the Stan models vendored from phenostan into the package."""

import unittest
from importlib.resources import files

STAN_DIR = files("phenosurv") / "stan"


class TestPackagedModels(unittest.TestCase):

    def test_thresh_surv_gdd_stan_file_is_packaged(self):
        self.assertTrue((STAN_DIR / "thresh-surv-gdd.stan").is_file())

    def test_phenostan_version_file_exists(self):
        self.assertTrue((STAN_DIR / "PHENOSTAN_VERSION").is_file())

    def test_phenostan_version_file_is_not_empty(self):
        self.assertNotEqual((STAN_DIR / "PHENOSTAN_VERSION").read_text().strip(), "")


if __name__ == "__main__":
    unittest.main()
