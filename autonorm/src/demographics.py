from typing import Optional
from .enums import Race, Sex, Handedness, DemographicVariableType, DemographicCoding


class DemographicVariable():
    def __init__(self, demo_type: DemographicVariableType, coding: DemographicCoding, value: float):
        self._harmonized_battery_mappings = {
            DemographicVariableType.RACE.value: {
                Race.ASIAN.value: 95,
                Race.WHITE.value: 99,
                Race.AMERICAN_INDIAN_OR_ALASKAN_NATIVE.value: 94,
                Race.BLACK_OR_AFRICAN_AMERICAN.value: 96,
                Race.NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER.value: 97
            },
            DemographicVariableType.SEX.value: {
                Sex.MALE.value: 95,
                Sex.FEMALE.value: 99
            },
            DemographicVariableType.HANDEDNESS.value: {
                Handedness.RIGHT.value: 1,
                Handedness.LEFT.value: 2,
                Handedness.AMBIDEXTOROUS.value: 3
            }
        }

        self._demo_var_type = demo_type
        self._coding = coding
        self._value = value
        self._category = None
        self.set_category()

    def set_category(self):
        if self._coding == DemographicCoding.CUSTOM:
            self._category = self._category
        if self._coding == DemographicCoding.PSYNCS:
            if self._demo_var_type == DemographicVariableType.RACE:
                self._category = Race(self._value).value
            if self._demo_var_type == DemographicVariableType.SEX:
                self._category = Sex(self._value).value
            if self._demo_var_type == DemographicVariableType.HANDEDNESS:
                self._category = Handedness(self._value).value
        if self._coding == DemographicCoding.HARMONIZED_BATTERY:
            if self._demo_var_type in [DemographicVariableType.RACE, DemographicVariableType.SEX, DemographicVariableType.HANDEDNESS]:
                type = self._harmonized_battery_mappings[self._demo_var_type.value]
                category = list(type.keys())[list(type.values()).index(int(self._value))]
                self._category = category

    def set_value(self):
        if self._coding == DemographicCoding.CUSTOM:
            self._value = self._value
        if self._coding == DemographicCoding.PSYNCS:
            if self._demo_var_type == DemographicVariableType.RACE:
                self._value = Race(self._category).value
            if self._demo_var_type == DemographicVariableType.SEX:
                self._value = Sex(self._category).value
            if self._demo_var_type == DemographicVariableType.HANDEDNESS:
                self._value = Handedness(self._category).value
        if self._coding == DemographicCoding.HARMONIZED_BATTERY:
            if self._demo_var_type in [DemographicVariableType.RACE, DemographicVariableType.SEX, DemographicVariableType.HANDEDNESS]:
                type = self._harmonized_battery_mappings[self._demo_var_type.value]
                if self._category:
                    value = type[self._category]
                    self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value != value:
            self._value = value
            self.set_category()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        try:
            if self._demo_var_type in [DemographicVariableType.RACE, DemographicVariableType.SEX, DemographicVariableType.HANDEDNESS]:
                if self._category != value:
                    self._category = value
                    self.set_value()
            else:
                raise Exception('Cannot set category for ' + self._demo_var_type.name + ' Demographic Variable type')
        except Exception as e:
            raise e

    @property
    def coding(self):
        return self._coding

    @coding.setter
    def coding(self, value):
        if self._coding != value:
            self._coding = value
            self.set_value()


class RaceVariable(DemographicVariable):
    def __init__(self, coding: DemographicCoding, value: float):
        super().__init__(demo_type=DemographicVariableType.RACE, coding=coding, value=value)

    @property
    def category(self) -> Race:
        return Race(self._category)

    @category.setter
    def category(self, value: Race):
        if self._category != value.value:
            self._category = value.value
            self.set_value()


class SexVariable(DemographicVariable):
    def __init__(self, coding: DemographicCoding, value: float):
        super().__init__(demo_type=DemographicVariableType.SEX, coding=coding, value=value)

    @property
    def category(self) -> Sex:
        return Sex(self._category)

    @category.setter
    def category(self, value: Sex):
        if self._category != value.value:
            self._category = value.value
            self.set_value()


class HandednessVariable(DemographicVariable):
    def __init__(self, coding: DemographicCoding, value: float):
        super().__init__(demo_type=DemographicVariableType.HANDEDNESS, coding=coding, value=value)

    @property
    def category(self) -> Handedness:
        return Handedness(self._category)

    @category.setter
    def category(self, value: Handedness):
        if self._category != value.value:
            self._category = value.value
            self.set_value()


class Demographics():
    def __init__(self, coding: DemographicCoding, race: Optional[int], sex: Optional[int], handedness: Optional[int], age: Optional[int], education: Optional[int], diagnosis: Optional[int]):
        self.race: Optional[RaceVariable] = RaceVariable(coding=coding, value=race) if race else None
        self.sex = SexVariable(coding=coding, value=sex) if sex else None
        self.handedness = HandednessVariable(coding=coding, value=handedness) if handedness else None
        self.age = DemographicVariable(demo_type=DemographicVariableType.AGE, coding=coding, value=age) if age else None
        self.education = DemographicVariable(demo_type=DemographicVariableType.EDUCATION,
                                             coding=coding, value=education) if education else None
        self.diagnosis = DemographicVariable(demo_type=DemographicVariableType.DIAGNOSIS,
                                             coding=coding, value=diagnosis) if diagnosis else None
        self._coding = coding

    @property
    def coding(self) -> DemographicCoding:
        return self._coding

    @coding.setter
    def coding(self, value: DemographicCoding):
        if self._coding != value:
            self._coding = value
            if self.race:
                self.race.coding = value
            if self.handedness:
                self.handedness.coding = value
            if self.age:
                self.age.coding = value
            if self.education:
                self.education.coding = value
            if self.diagnosis:
                self.diagnosis.coding = value

    def get_dict(self):
        return {
            "race": self.race.value if self.race else None,
            "sex": self.sex.value if self.sex else None,
            "handedness": self.handedness.value if self.handedness else None,
            "age": self.age.value if self.age else None,
            "education": self.education.value if self.education else None,
            "diagnosis": self.diagnosis.value if self.diagnosis else None
        }
