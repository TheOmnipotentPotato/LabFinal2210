import numpy as np


def main() -> None:
    print("Please input you data now")
    length: float = float(input("Input ramp length: "))
    angle: float = float(input("Input ramp angle: "))
    coef_rolling_friction: float = float(input("Input coeficient of static friction: "))
    inital_height: float = float(input("Input the height at the end of the ramp: "))
    print(
        f" Length = {length} \n Angle = {angle} \n Coeficient of rolling fricition = {coef_rolling_friction} \n Inital Height = {inital_height}"
    )
    # convert the angle from deg -> rad
    # this is only to placate numpy
    angle: float = np.deg2rad(angle)
    print(f" Angle in rad = {angle}")
    final_ramp_velocity: float = np.sqrt(
        2 * 9.8 * (np.sin(angle) - coef_rolling_friction * np.cos(angle)) * length
    )
    delta_time_1: float = (
        final_ramp_velocity * np.sin(angle)
        + np.sqrt(
            (final_ramp_velocity**2) * (np.sin(angle) ** 2) + 2 * 9.8 * inital_height
        )
    ) / (-9.8)
    delta_time_2: float = (
        final_ramp_velocity * np.sin(angle)
        - np.sqrt(
            (final_ramp_velocity**2) * (np.sin(angle) ** 22.0) + 2 * 9.8 * inital_height
        )
    ) / (-9.8)
    dx_1: float = final_ramp_velocity * np.cos(angle) * delta_time_1
    dx_2: float = final_ramp_velocity * np.cos(angle) * delta_time_2
    print(f" Delta X_1 = {dx_1} \n Delta X_2 = {dx_2}")
    return None


if __name__ == "__main__":
    main()
    print("Have a nice day!")
