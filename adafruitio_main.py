from adafruitio import AdafruitIO as io


def led_callback(val):
    if val == "ON":
        rb.pixel(BLUE)
    elif val == "OFF":
        rb.pixel(BLACK)
    else:
        print(f'led: incorrect value {val}')
    
    
def arcoiris_callback(val):
    val = int(val)
    if val > -1 and val < 256:
        rb.arcoiris(val)
    else:
        print(f'arcoiris: incorrect value {val}')
        
# Subscription callback
def sub_callback(topic, msg, retained):
    message = msg.decode()
    if topic == "crcibernetica/feeds/scd41-led":
        led_callback(message)
    elif topic == "crcibernetica/feeds/scd41-arcoiris":
        arcoiris_callback(message)
#     print(f'Topic: "{topic.decode()}" Message: "{msg.decode()}" Retained: {retained}')

