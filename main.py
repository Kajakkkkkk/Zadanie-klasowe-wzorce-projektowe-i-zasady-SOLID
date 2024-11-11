from abc import ABC, abstractmethod


class StatisticsLogger(ABC):
    @abstractmethod
    def display_statistics(self) -> None:
        pass

    @abstractmethod
    def get_execution_times(self) -> list[float]:
        pass


class ExecutionTimesBaseStatistics(StatisticsLogger):
    def __init__(self, execution_times: list[float]) -> None:
        self._execution_times = execution_times

    def display_statistics(self) -> None:
        for time in self._execution_times:
            print(time)

    def get_execution_times(self) -> list[float]:
        return self._execution_times


# dekorator obiektowy
class WithMeanStatisticsLogger(StatisticsLogger):
    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        execution_times = self._logger.get_execution_times()
        if execution_times:
            mean_value = sum(execution_times) / len(execution_times)
            print(f"Średni czas wykonania: {mean_value}")

    def get_execution_times(self) -> list[float]:
        return self._logger.get_execution_times()


class WithSummaryStatisticsLogger(StatisticsLogger):
    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        execution_times = self._logger.get_execution_times()
        if execution_times:
            count = len(execution_times)
            total = sum(execution_times)
            minimum = min(execution_times)
            maximum = max(execution_times)
            print(f"Liczba rekordów: {count}, Suma: {total}, Min: {minimum}, Max: {maximum}")
        self._logger.display_statistics()

    def get_execution_times(self) -> list[float]:
        return self._logger.get_execution_times()
        
def client_code_object_decorators():
    base_logger = ExecutionTimesBaseStatistics([3.5, 4.8, 2.1, 5.9])
    mean_logger = WithMeanStatisticsLogger(base_logger)
    summary_logger = WithSummaryStatisticsLogger(mean_logger)
    summary_logger.display_statistics()

if __name__ == "__main__":
    print("Wynik dekoratorów obiektowych:")
    client_code_object_decorators()
