def calculate_ohms_law(operation: str, values: dict[str, float]):
    if operation == "calculate-voltage":
        current = values.get("current")
        resistance = values.get("resistance")

        if current is None or resistance is None:
            raise ValueError(
                "Current and resistance are required to calculate voltage."
            )

        result = current * resistance

        return {
            "formula": "V = I × R",
            "result": result,
            "unit": "V",
            "steps": [
                "V = I × R",
                f"V = {current} × {resistance}",
                f"V = {result} V",
            ],
        }

    elif operation == "calculate-current":
        voltage = values.get("voltage")
        resistance = values.get("resistance")

        if voltage is None or resistance is None:
            raise ValueError(
                "Voltage and resistance are required to calculate current."
            )

        if resistance == 0:
            raise ValueError(
                "Resistance cannot be zero."
            )

        result = voltage / resistance

        return {
            "formula": "I = V / R",
            "result": result,
            "unit": "A",
            "steps": [
                "I = V / R",
                f"I = {voltage} / {resistance}",
                f"I = {result} A",
            ],
        }

    elif operation == "calculate-resistance":
        voltage = values.get("voltage")
        current = values.get("current")

        if voltage is None or current is None:
            raise ValueError(
                "Voltage and current are required to calculate resistance."
            )

        if current == 0:
            raise ValueError(
                "Current cannot be zero."
            )

        result = voltage / current

        return {
            "formula": "R = V / I",
            "result": result,
            "unit": "Ω",
            "steps": [
                "R = V / I",
                f"R = {voltage} / {current}",
                f"R = {result} Ω",
            ],
        }

    else:
        raise ValueError(
            "Invalid Ohm's Law operation."
        )