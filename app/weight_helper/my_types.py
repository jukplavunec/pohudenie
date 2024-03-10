from pydantic import BaseModel



class LostWeightParams(BaseModel):
    weight: list[float | int]
    brest_volume: list[float | int]
    stomach_volume: list[float | int]
    ass_volume: list[float | int]
    leg_volume: list[float | int]

class GlebParams(BaseModel):
    weight: list[float | int]
    brest_volume: list[float | int]
    stomach_volume: list[float | int]
    ass_volume: list[float | int]
    leg_volume: list[float | int]
    hand_volume: list[float | int]


class KsyhaParams(BaseModel):
    weight: list[float | int]
    brest_volume: list[float | int]
    stomach_volume: list[float | int]
    ass_volume: list[float | int]
    leg_volume: list[float | int]
