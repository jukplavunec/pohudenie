from app.weight_helper.lost_weight_protocol import LostWeight
from typing import NoReturn

from app.weight_helper.my_types import GlebParams, KsyhaParams
import matplotlib.pyplot as plt
import seaborn as sns

class KsyhaLostWeight(LostWeight):
    def __init__(self, ksyha_params: KsyhaParams) -> NoReturn:
        if ksyha_params is None:
            raise ValueError("KsyhaParams should not be None")
        super().__init__(ksyha_params)


class GlebLostWeight(LostWeight):
    def __init__(self, gleb_params: GlebParams) -> NoReturn:
        if gleb_params is None:
            raise ValueError("GlebParams should not be None")
        self._hand_volume = gleb_params.hand_volume
        super().__init__(gleb_params)

    def change_hand_volume(self) -> NoReturn:
        y_size = len(self._hand_volume)
        sns.lineplot(x=self.gleb_dates[:y_size], y=self._hand_volume, label="Volume")
        plt.xlabel("Date")
        plt.ylabel("Brest volume (cm)")
        sns.set_style("dark")
        plt.title("Gleb change brest volume")
        plt.show()

if __name__ == '__main__':
    gleb = GlebLostWeight(
        GlebParams(
            weight=[92, 89, 87, 85, 83],
            brest_volume=[100, 96, 94.2, 93.8, 91.5],
            stomach_volume=[100],
            ass_volume=[100],
            leg_volume=[100],
            hand_volume=[100]
        )
    )
    gleb.lost_weight_plot()
