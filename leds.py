# based of https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py

devMode = False
try:
    from rpi_ws281x import PixelStrip, Color
except ImportError:
    print("Warning: Could not import 'rpi_ws281x', assuming you're in dev mode")
    devMode = True

# LED strip configuration:
LED_COUNT = 32        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def set_color(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

# Main program logic follows:
if __name__ == '__main__':
    if not devMode:
        # Create NeoPixel object with appropriate configuration.
        strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        try:
            while True:
                set_color(strip, Color(255, 255, 255))

        except KeyboardInterrupt:
            set_color(strip, Color(0, 0, 0))