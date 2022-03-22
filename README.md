# pi-watch
 
I recently came across an IO board from PiMoroni called [Pirate Audio: Speaker for Raspberry Pi](https://shop.pimoroni.com/products/pirate-audio-mini-speaker?variant=31189753692243). 
This audio board has a small `1.3" (240x240) IPS LCD` display & a `1W speaker`. The display has an SPI interface and 
uses the `st7789` controller module & the audio is controlled by the onboard `MAX98357A` DAC chip. It fits perfectly on 
a [RaspberryPi Zero](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) and I instantly thought of building 
something with it - maybe a micro-TV or something which sounds cool, but I have to take into account the hardware restrictions 
of a pi-zero & of the HAT I am using.

PI Watch is a python based modern day simulation of a clock radio - at-least for Mark-I. 
I hope to convert this project into something more important than just a dumb clock trying to wake you up every morning 
by playing songs from your favorite stations on the internet radio/streaming service.

This is just one of the uses and I will post more projects & update this readme as I jot down more points.
