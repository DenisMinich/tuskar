# pylint: disable=invalid-name
# pylint: disable=missing-docstring
"""Tests for engine.py"""
from tuskar import engine
from tuskar import tasks_plan


def test_engine_returns_plan_without_it_was_mentioned_before():
    # INIT
    plan_name = 'test_plan'
    # ACt
    plan = engine.Engine.get_plan(plan_name)

    # CHECK
    assert isinstance(plan, tasks_plan.TasksPlan)


def test_engine_returns_default_plan_if_no_name_was_provided():
    # INIT
    # ACt
    plan = engine.Engine.get_plan()

    # CHECK
    assert isinstance(plan, tasks_plan.TasksPlan)
