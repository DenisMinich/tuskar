# pylint: disable=invalid-name
# pylint: disable=missing-docstring
"""Tests for tuskar.tasks_storage.py"""
from tuskar import task


class RedSignalTask(task.Task):
    conditions = {'signal': 'red'}


def test_check_conditions_returns_true_if_context_has_valid_key_value_pair():
    # INIT
    context = {'signal': 'red'}

    # ACT
    passed_conditions = RedSignalTask.check_conditions(context)

    # CHECK
    assert passed_conditions


def test_check_conditions_returns_false_if_not_valid_value_found():
    # INIT
    context = {'signal': 'green'}

    # ACT
    passed_conditions = RedSignalTask.check_conditions(context)

    # CHECK
    assert not passed_conditions


def test_check_conditions_returns_false_if_no_key_found():
    # INIT
    context = {}

    # ACT
    passed_conditions = RedSignalTask.check_conditions(context)

    # CHECK
    assert not passed_conditions
