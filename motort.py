import RPi.GPIO as GPIO
import time

# ============================================================================
#  Настройки
# ============================================================================

# Номера GPIO пинов (BCM numbering)
MOTOR1_PIN = 4
MOTOR2_PIN = 27
MOTOR3_PIN = 26
MOTOR4_PIN = 6

# Частота PWM (обычно 50 Hz для ESC, проверьте datasheet BLHELI 30A)
PWM_FREQUENCY = 50

# Диапазон значений ШИМ (в микросекундах) для BLHELI ESC
PWM_MIN = 1000  # Минимум (остановка)
PWM_MAX = 2000  # Максимум (полная скорость)
PWM_RANGE = PWM_MAX - PWM_MIN  # Диапазон

# Желаемая скорость моторов (в процентах, 0-100)
MOTOR_SPEED_PERCENT = 50  # Примерно половина скорости

# ============================================================================
#  Настройка GPIO и PWM
# ============================================================================

try:
    # Настройка GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)  # Отключаем предупреждения

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

    # Функция для установки скорости мотора (из предыдущего примера)
    def set_motor_speed(pwm_object, speed_percent):
        pulse_width = PWM_MIN + (speed_percent / 100) * PWM_RANGE
        duty_cycle = (pulse_width / 20000) * 100  # Для 50Hz PWM
        pwm_object.ChangeDutyCycle(duty_cycle)

    # Запуск PWM с заданной скоростью
    set_motor_speed(pwm1, MOTOR_SPEED_PERCENT)
    pwm1.start(0) # Начинаем с 0 чтобы не сразу на полную
    set_motor_speed(pwm2, MOTOR_SPEED_PERCENT)
    pwm2.start(0)
    set_motor_speed(pwm3, MOTOR_SPEED_PERCENT)
    pwm3.start(0)
    set_motor_speed(pwm4, MOTOR_SPEED_PERCENT)
    pwm4.start(0)

    print(f"Моторы запущены на {MOTOR_SPEED_PERCENT}% скорости. Нажмите Ctrl+C для остановки.")

    # ========================================================================
    #  Основной цикл (просто держим моторы включенными)
    # ========================================================================
    try:
        while True:
            time.sleep(1)  # Держим программу активной
    except KeyboardInterrupt:
        print("Остановка моторов...")

    finally:
        # ====================================================================
        #  Остановка и очистка
        # ====================================================================
        print("Stopping PWM")
        pwm1.stop()
        pwm2.stop()
        pwm3.stop()
        pwm4.stop()

        print("Cleaning up GPIO")
        GPIO.cleanup()
        print("All motors stopped.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    GPIO.cleanup()
    print("GPIO cleanup complete.")
