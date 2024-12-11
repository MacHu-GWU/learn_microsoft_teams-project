# -*- coding: utf-8 -*-

from learn_microsoft_teams import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_microsoft_teams.tests import run_cov_test

    run_cov_test(__file__, "learn_microsoft_teams.api", preview=False)
