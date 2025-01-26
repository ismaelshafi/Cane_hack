from machine import Pin, time_pulse_us
import time
import network
import requests
from time import sleep
import gc

ssid = 'ISMAELS_SURFACE'
password = 'O62(403y'
print(gc.mem_free())
# Your phone number in international format (including the + sign)
phone_number = '+18324156784'
# Example: phone_number = '+351912345678'

# Your callmebot API key
api_key = '7791178'

# Init Wi-Fi Interface
def init_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Connect to your network
    wlan.connect(ssid, password)
    # Wait for Wi-Fi connection
    connection_timeout = 10
    while connection_timeout > 0:
        if wlan.status() >= 3:
            break
        connection_timeout -= 1
        print('Waiting for Wi-Fi connection...')
        sleep(1)
    # Check if connection is successful
    if wlan.status() != 3:
        return False
    else:
        print('Connection successful!')
        network_info = wlan.ifconfig()
        print('IP address:', network_info[0])
        return True

def send_message(phone_number, api_key, message):
    # Set the URL
    url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message}&apikey={api_key}'

    # Make the request
    response = requests.get(url)
    # check if it was successful
    if (response.status_code == 200):
        print('Success!')
    else:
        print('Error')
        print(response.text)





SOUND_SPEED=340 # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US=10

trig_pin = Pin(15, Pin.OUT) # Broche GP15 de la Pico
echo_pin = Pin(14, Pin.IN)  # Broche GP14 de la Pico

while True:
    # Prepare le signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    print(distance_cm)
    if (distance_cm > 100):
        try: 
            if init_wifi(ssid, password):
                message = 'POTENTIAL_EMERGECY_FOR_ISMAEL' 
                send_message(phone_number, api_key, message)
            print(gc.mem_free())
            False
        except Exception as e:
            print('Error:', e)
            False

    time.sleep_ms(500)
    
    
