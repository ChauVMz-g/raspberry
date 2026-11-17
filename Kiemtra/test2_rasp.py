import sys
from time import sleep
from urllib import request, parse, error

from grove.grove_light_sensor_v1_2 import GroveLightSensor   # Cảm biến ánh sáng (A0)
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger  # Cảm biến khoảng cách (D5)
from grove.display.jhd1802 import JHD1802  # LCD I2C

from gpiozero import LED, Buzzer

LIGHT_PIN = 0         # Cổng Analog A0
ULTRASONIC_PIN = 5    # Cổng Digital D5

LED_PIN = 16          # Cổng Digital D16 (GPIO 16)
BUZZER_PIN = 18       # Cổng Digital D18 (GPIO 18)

BASE_URL = "https://api.thingspeak.com"
API_KEY_WRITE = "KG8ED62ME1SB70C7"

def thingspeak_write(fields):
    try:
        body = parse.urlencode({f"field{k}": v for k, v in fields.items()}).encode()
        req = request.Request(f"{BASE_URL}/update", data=body, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("X-THINGSPEAKAPIKEY", API_KEY_WRITE)
        
        with request.urlopen(req, timeout=10) as r:
            res = r.read().decode()
            print(f" [THINGSPEAK SUCCESS] Entry ID: {res}")
            return res
    except error.URLError as e:
        print(f" [THINGSPEAK ERROR] Gửi dữ liệu thất bại: {e.reason}")
    except Exception as e:
        print(f" [THINGSPEAK ERROR] Lỗi không xác định: {e}")

def main():
    light_sensor = GroveLightSensor(LIGHT_PIN)
    distance_sensor = GroveUltrasonicRanger(ULTRASONIC_PIN)
    lcd = JHD1802()

    led = LED(LED_PIN)
    led_status = 0

    buzzer = Buzzer(BUZZER_PIN)
    buzzer_status = 0

    print_counter = 0
    write_counter = 0

    print("Hệ thống IoT giám sát đang khởi chạy...")
    print("Nhấn Ctrl+C để dừng chương trình an toàn.\n")

    try:
        while True:
            value1 = light_sensor.light
            value2 = distance_sensor.get_distance()

            if value1 > 200:
                led.on()
                led_status = 1
            elif value1 < 150:
                led.off()
                led_status = 0

            if value2 < 10:
                buzzer.on()
                buzzer_status = 1
            elif value2 > 40:
                buzzer.off()
                buzzer_status = 0

            if print_counter >= 10:
                print_counter = 0
                print(f"[MONITOR] Light: {value1:<4} | Dist: {value2:.1f}cm | LED: {led_status} | BUZZER: {buzzer_status}")
                
                lcd.setCursor(0, 0)
                lcd.write(f"Light: {value1:<10}")
                lcd.setCursor(1, 0)
                lcd.write(f"Dist : {value2:<7.1f}cm")
            else:
                print_counter += 1

            if write_counter >= 20:
                write_counter = 0
                print("[THINGSPEAK] Đang đẩy dữ liệu 4 trường lên Server...")
                thingspeak_write({
                    1: value1, 
                    2: round(value2, 1), 
                    3: led_status, 
                    4: buzzer_status
                })
            else:
                write_counter += 1

            sleep(1)

    except KeyboardInterrupt:
        print("\n[STOP] Đã phát hiện thao tác dừng (Ctrl+C).")
    finally:
        led.off()
        buzzer.off()
        print("[SAFE EXIT] Đã tắt LED, Buzzer và thoát chương trình.")
        sys.exit(0)

if __name__ == "__main__":
    main()