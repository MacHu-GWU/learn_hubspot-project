# -*- coding: utf-8 -*-

from learn_hubspot import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_hubspot.tests import run_cov_test

    run_cov_test(__file__, "learn_hubspot.api", preview=False)
