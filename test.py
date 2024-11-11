import pytest
from main import ExecutionTimesBaseStatistics


def test_execution_times_base_statistics():
    execution_times = [4, 5.8, 2, 6.2]
    logger = ExecutionTimesBaseStatistics(execution_times)

    assert logger.get_execution_times() == execution_times


def test_execution_times_with_single_element():
    execution_times = [5.2]
    logger = ExecutionTimesBaseStatistics(execution_times)

    assert logger.get_execution_times() == execution_times


if __name__ == "__main__":
    pytest.main()
