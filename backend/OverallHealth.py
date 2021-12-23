Data = {
    "Voltage": {"0": {"L": 11550, "R": 12100, "N": 10450, "M": 9900}},
    "Oil": {"0": {"L": 95, "R": 145, "N": 20, "M": 20}},
    "Winding": {"0": {"L": 100, "R": 150, "N": 25, "M": 25}},
    "Moisture": {"0": {"L": 20, "R": 100, "N": 0, "M": 0}},
    "Current": {
        "TF-01": {"L": 3.75, "R": 6, "N": 0, "M": 0},
        "TF-02": {"L": 1.25, "R": 2, "N": 0, "M": 0},
        "TF-03": {"L": 0.75, "R": 1.2, "N": 0, "M": 0},
    },
    "Weights": {"Voltage": 10, "Current": 25, "Winding": 25, "Oil": 20, "Moisture": 20},
}


def f(attribute, value, type="0"):
    if  Data[attribute][type]["M"] !=  Data[attribute][type]["N"]:
        if value > Data[attribute][type]["N"] and value < Data[attribute][type]["L"]:
            return 1
        elif value >= Data[attribute][type]["L"] and value <= Data[attribute][type]["R"]:
            return (1 - ((value - Data[attribute][type]["L"])/ (Data[attribute][type]["R"] - Data[attribute][type]["L"]))** 3)
        elif value >= Data[attribute][type]["M"] and value <= Data[attribute][type]["N"]:
            return ((value - Data[attribute][type]["M"])/ (Data[attribute][type]["N"] - Data[attribute][type]["M"])) ** (1 / 3)
        elif value > Data[attribute][type]["R"] and value < Data[attribute][type]["M"]:
            return 0
        else:
             pass
    else:
        if value < Data[attribute][type]["L"]:
            return 1
        elif value >= Data[attribute][type]["L"] and value <= Data[attribute][type]["R"]:
            return (1 - ((value - Data[attribute][type]["L"])/ (Data[attribute][type]["R"] - Data[attribute][type]["L"]))** 3)
        elif value > Data[attribute][type]["R"]:
            return 0
        else:
             pass

    return 0


def get_health(
    Transformer_Type,
    Current_Input,
    Voltage_Input,
    Oil_Temperature,
    Winding_Temperature,
    Moisture_Level,
):
    attribute_list = {
        "Current": Current_Input,
        "Voltage": Voltage_Input,
        "Oil": Oil_Temperature,
        "Winding": Winding_Temperature,
        "Moisture": Moisture_Level,
    }
    health = 0
    for attribute in attribute_list:
        if attribute == "Current":
            health += (
                f(attribute, attribute_list[attribute], Transformer_Type)
                * Data["Weights"][attribute]
            )
        else:
            health += (
                f(attribute, attribute_list[attribute]) * Data["Weights"][attribute]
            )

    return health