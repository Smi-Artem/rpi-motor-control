import RPi.GPIO as GPIO
import time

# Номера GPIO пинов (BCM numbering)
MOTOR1_PIN = 4
MOTOR2_PIN = 23
MOTOR3_PIN = 26
MOTOR4_PIN = 6

# Частота PWM (обычно 50 Hz для ESC)
PWM_FREQUENCY = 50

# Значение ШИМ (в микросекундах -  подберите значение)
MOTOR_SPEED = 1500  # Примерно середина, настраивайте

try:
    # Настройка GPIO
    GPIO.setmode(GPIO.BCM) # Используем BCM номера пинов

    # Настройка пинов как выходы
    GPIO.setup(MOTOR1_PIN, GPIO.OUT)
    GPIO.setup(MOTOR2_PIN, GPIO.OUT)
    GPIO.setup(MOTOR3_PIN, GPIO.OUT)
    GPIO.setup(MOTOR4_PIN, GPIO.OUT)

    # Создание PWM объектов
    pwm1 = GPIO.PWM(MOTOR1_PIN, PWM_FREQUENCY)
    pwm2 = GPIO.PWM(MOTOR2_PIN, PWM_FREQUENCY)
    pwm3 = GPIO.PWM(MOTOR3_PIN, PWM_FREQUENCY)
    pwm4 = GPIO.PWM(MOTOR4_PIN, PWM_FREQUENCY)

    # Расчет duty cycle
    duty_cycle = (MOTOR_SPEED / 20000) * 100 # (pulse_width / period) * 100

    # Запуск PWM с заданным duty cycle
    pwm1.start(duty_cycle)
    pwm2.start(duty_cycle)
    pwm3.start(duty_cycle)
    pwm4.start(duty_cycle)

    print("Моторы запущены на фиксированной скорости. Нажмите Ctrl+C для остановки.")

    while True:
        time.sleep(1)  # Держим программу активной

except KeyboardInterrupt:
    print("Остановка моторов...")

    # Остановка PWM
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()

    # Очистка GPIO
    GPIO.cleanup()

    print("Все моторы остановлены.")