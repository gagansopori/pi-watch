# pi-watch
 
## Introduction
I recently came across an IO board from PiMoroni called [Pirate Audio: Speaker for Raspberry Pi](https://shop.pimoroni.com/products/pirate-audio-mini-speaker?variant=31189753692243). 
This audio board has a small `1.3" (240x240) IPS LCD` display & a `1W speaker`. The display has an SPI interface and 
uses the `st7789` controller module & the audio is controlled by the onboard `MAX98357A` DAC chip. ![PIM485](https://cdn.shopify.com/s/files/1/0174/1800/products/Pirate_Audio_Smol_Speaker_1_of_3_192x192.jpg?v=1574166432)It fits perfectly on 
a [RaspberryPi Zero](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) and I instantly thought of building 
something with it - maybe a modern day simulation of a clock radio - at-least for Mark-I. I hope to convert this project 
into something more important than just a dumb clock trying to wake you up every morning by playing songs from your 
favorite stations on the internet radio/streaming service.

## Hardware
 * [Pirate Audio: Speaker for Raspberry Pi](https://shop.pimoroni.com/products/pirate-audio-mini-speaker?variant=31189753692243) - Depending on your use case, you can select from a variety of IO options.
 * [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) - Zero has the best form factor for this board, but you can use any other Pi for it.
 * [5V, 2A Power Supply Unit](https://www.raspberrypi.com/products/raspberry-pi-universal-power-supply/) - I'm using the official Raspberry Pi power supply unit, but you can use one of your preference.
 * [Raspberry Pi Case](https://www.adafruit.com/product/3252) - I'm using a clear-top case by [AdaFruit Industries](https://www.adafruit.com/) but there are a lot of other good options available depending on your use-case.
 * Micro-SD Card - I'm using a 32GB Class 3 SD Card, but if you want a better performance, you should use a Class 10 or higher SD-card.

## Installation
I'm going to assume that you already have a working pi set-up with your choice of OS & is fully updated. If not, refer to [this article]() to get started. Now, to be able to run this program you'll need to set the following few up on your Pi:
* Python-3 - Python-2 is EOL & this app was written in Python3.
    ```
    sudo apt-get install python3
    ```
  * After you've installed python, you'll need to a few other libraries as a pre-requisite to the display driver module we'll install later:
    ```
    sudo apt-get update
    sudo apt-get install python3-rpi.gpio python3-spidev python3-pil python3-numpy
    ```
* ST7789 Display Module - This is the driver for the display attached to the hat we're using.
  ```
  sudo pip3 install ST7789
  ```
  * This is an SPI based display, so you'll also need to enable I2C & SPI channels on your Pi. You can do this by changing Inteface Options in Raspi-Config (```sudo raspi-config```)
* Git - To be able to clone the project initially & to pull any future updates & bug fixes.
  ```
  sudo apt-get install git
  ```
* OpenWeatherMaps Developer Access - It's free to use for non-commercial purposes, but you do need to signup for [developer access](https://openweathermap.org/price). Once done, you'll need to update your api-key in the properties file. (I'll integrate secrets at a later point to keep the codebase separate)


## Running the Application
Now that we've set everything up, its time to get the app & run it on your pi.
 - Get the app using git:
   ```
    git clone https://github.com/gagansopori/pi-watch.git
   ```
 - Run the `main.py` file using commandline:
   ```
    python3 /location-to-your-project/main.py
   ```
 - If you want to set this up as a cron job you can use crontab from linux as such:
    ```
   crontab -e
   ```
   - Setup the task to run everytime you reboot.
   ```
   @reboot python3 /location-to-your-project/main.py 
   ```

<p/>

That's it. Your weather station is ready to go. This is just one of the uses, and I will post more & update this readme as add more functionalities to this project
