# pylint: disable=invalid-name
# pylint: disable=missing-docstring
"""Tests for tuskar.tasks_storage.py"""
import mock
import pytest


from tuskar import tasks_storage


_TASK_NAME = 'signal_processor'


def test_tasks_storage_raises_value_error_if_no_suitable_tasks_found():
    # INIT
    test_storage = tasks_storage.TasksStorage()
    test_storage.add_task(_TASK_NAME, mock.MagicMock(
        **{'check_conditions.return_value': False}))
    test_storage.add_task(_TASK_NAME, mock.MagicMock(
        **{'check_conditions.return_value': False}))

    # ACT
    # CHECK
    pytest.raises(ValueError, test_storage.get_task, _TASK_NAME, mock.Mock())


def test_tasks_storage_returns_task_if_only_one_task_passed_conditions():
    # INIT
    test_storage = tasks_storage.TasksStorage()
    test_storage.add_task(_TASK_NAME, mock.MagicMock(**{
        'check_conditions.return_value': True, 'marker': 1, }))
    test_storage.add_task(_TASK_NAME, mock.MagicMock(**{
        'check_conditions.return_value': False, 'marker': 2, }))

    # ACT
    task_to_execute = test_storage.get_task(_TASK_NAME, mock.Mock())

    # CHECK
    assert task_to_execute.marker == 1


def test_tasks_storage_raises_value_error_if_two_suitable_tasks_found():
    # INIT
    test_storage = tasks_storage.TasksStorage()
    test_storage.add_task(_TASK_NAME, mock.MagicMock(
        **{'check_conditions.return_value': True}))
    test_storage.add_task(_TASK_NAME, mock.MagicMock(
        **{'check_conditions.return_value': True}))

    # ACT
    # CHECK
    pytest.raises(ValueError, test_storage.get_task, _TASK_NAME, mock.Mock())
