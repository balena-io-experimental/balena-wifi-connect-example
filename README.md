balena-wifi-connect-example
==========================

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/balena-io-projects/balena-wifi-connect-example/blob/master/LICENSE)

> Example application to demonstrate [wifi-connect](https://github.com/balena-io/wifi-connect)

This example is written in python, consisting of an RPi3 and a [Display-O-Tron HAT](https://shop.pimoroni.com/products/display-o-tron-hat) to provide visual feedback. 

The [Dockerfile](./Dockerfile.template) is split into two sections; the first section is for resin-wifi-connect and the second is for the Display-O-Tron HAT. This provides a good idea of the correct way to combine the balena-wifi-connect Dockerfile and your app's Dockerfile into one. 

The [start](./start) script has been modifed to run this example app both before and after running balena-wifi-connect. This provides both visual feedback on the connection status and a good idea of the correct way to integrate the balena-wifi-connect start script into your app.

The first image shows the Display-O-Tron HAT when no configured connection has been found and the second image shows what happens once a connection has been configured and successfully connected.

![Not connected](./images/20161213_162534.jpg?raw=true)
![Connected](./images/20161213_163703.jpg?raw=true)
