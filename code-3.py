class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

class AutonomousVehicle:
    def __init__(self, target_speed):
        self.target_speed = target_speed
        self.current_speed = 0
        self.controller = PIDController(Kp=0.1, Ki=0.01, Kd=0.05)  # Tuned PID gains
        self.dt = 0.1  # Time step for simulation

    def update_speed(self):
        error = self.target_speed - self.current_speed
        control_output = self.controller.update(error, self.dt)
        self.current_speed += control_output * self.dt

if __name__ == "__main__":
    autonomous_car = AutonomousVehicle(target_speed=30)  # Set target speed to 30 m/s
    simulation_time = 10  # Simulation time in seconds
    steps = int(simulation_time / autonomous_car.dt)
    
    for _ in range(steps):
        autonomous_car.update_speed()
        print("Current Speed:", autonomous_car.current_speed)
