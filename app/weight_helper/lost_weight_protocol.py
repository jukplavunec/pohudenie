import matplotlib.pyplot as plt
from typing import NoReturn
from app.weight_helper.consts import CYCLE_DAY_RANGE, CYCLE_DAY_STEP, DAY_CUTOFF
from my_types import LostWeightParams
from datetime import date, timedelta
import seaborn as sns


class LostWeight:
    def __init__(self, gleb_params: LostWeightParams) -> NoReturn:
        if gleb_params is None:
            raise ValueError("GlebParams should not be None")
        self._weight = gleb_params.weight
        self._brest_volume = gleb_params.brest_volume
        self._stomach_volume = gleb_params.stomach_volume
        self._ass_volume = gleb_params.ass_volume
        self._leg_volume = gleb_params.leg_volume
        self.__gleb_dates = [
            (date(2024, 3, 11) + timedelta(days=i)).isoformat()[:DAY_CUTOFF]  # 2024-03-11 + i days
            for i in range(0, CYCLE_DAY_RANGE, CYCLE_DAY_STEP)]

    @property
    def all_params(self) -> tuple[float]:
        return (
            self._weight,
            self._brest_volume,
            self._stomach_volume,
            self._ass_volume,
            self._leg_volume,
        )

    @property
    def gleb_dates(self) -> list[str]:
        return self.__gleb_dates
    def lost_weight_plot(self) -> NoReturn:
        y_size = len(self._weight)
        sns.lineplot(x=self.__gleb_dates[:y_size], y=self._weight, label="Weight", marker="o")
        plt.xlabel("Date")
        plt.ylabel("Weight (kg)")
        plt.title("Gleb lost weight")
        plt.savefig("gleb_lost_weight.png")
        plt.show()

    def change_brest_volume(self) -> NoReturn:
        y_size = len(self._brest_volume)
        sns.lineplot(x=self.__gleb_dates[:y_size], y=self._brest_volume, label="Volume")
        plt.xlabel("Date")
        plt.ylabel("Brest volume (cm)")
        sns.set_style("dark")
        plt.title("Gleb change brest volume")
        plt.show()


    def change_stomach_volume(self) -> NoReturn:
        y_size = len(self._stomach_volume)
        sns.lineplot(x=self.__gleb_dates[:y_size], y=self._stomach_volume, label="Volume")
        plt.xlabel("Date")
        plt.ylabel("Brest volume (cm)")
        sns.set_style("dark")
        plt.title("Gleb change brest volume")
        plt.show()
        
    def change_ass_volume(self) -> NoReturn:
        y_size = len(self._ass_volume)
        sns.lineplot(x=self.__gleb_dates[:y_size], y=self._ass_volume, label="Volume")
        plt.xlabel("Date")
        plt.ylabel("Brest volume (cm)")
        sns.set_style("dark")
        plt.title("Gleb change brest volume")
        plt.show()

    def change_ass_volume(self) -> NoReturn:
        y_size = len(self._leg_volume)
        sns.lineplot(x=self.__gleb_dates[:y_size], y=self._leg_volume, label="Volume")
        plt.xlabel("Date")
        plt.ylabel("Brest volume (cm)")
        sns.set_style("dark")
        plt.title("Gleb change brest volume")
        plt.show()

