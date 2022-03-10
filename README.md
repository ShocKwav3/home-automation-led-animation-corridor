# Home automation corridor
Nothing very interesting, just some led strip giving some fancy show, based on motion detection. Oh wait... the animation is probably interesting ;)
Also serves as a hub of information about the portable [Door key dispenser](https://github.com/ShocKwav3/home-automation-door-key-dispenser)

## Tech details
### Parts
 - ESP8266 (or whatever)
 - Led strips (I used WS2812B)
 - Motion detectors (x2)
 - 5V regulator
 - Power supply
 - Resistors (10k and 330)
 - Capacitor (500uf-1000uf)
 - Logic level shifter

### How it works
Basically the led strip should be placed near the ground on the corridor. When someone enters the apartment, the led should play a animation, something like we see in a airport's runway, showing the direction to go in. When someone is going out should play same animation with different direction. Easy.

This is done by using two motion sensors. One near the door, one away from the door. Let's call them outer and inner respectively. When inner detects motion then outer will be waiting for detection. In a certain period if there is motion on the outer the exit animation is played and vice versa. Can be achieved by other sensors such as sonar (ik ik...)

System stays in deep sleep and only wakes up by these motion sensors.

The [door key dispenser](https://github.com/ShocKwav3/home-automation-door-key-dispenser) would be connected wirelessly and send information to this device. Summary will be shown in the connected oled display.

### Circuit diagram
![alt text](https://github.com/ShocKwav3/home-automation-led-animation-corridor/blob/main/fritzing/led-corridor_img.png)
