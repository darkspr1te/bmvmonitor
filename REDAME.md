
```
-Project details-
Add esp8266 serial to telnet adapter to a victron BMV-600s , grab that data and display via RRD on a linux (ubuntu svr) box 
right now capture works, graphing is broken, display is non-existant via any means other than pulling file to another machine
this is prof of concept works right now. 

Project goal is long term battery health monitoring and power failure rates. Later goals is to add features

CPU:ESP8266
ADDITIONAL:Victron BMV-600S 

```
### Done:
- [x] Add basic readme's and docs
- [x] Add project details-structure-references

### Still TODO:

- [ ] Add netcat filter
- [ ] Add rdd write routine
- [ ] Add web page readback 
- [ ] Add security - lol spec - 

### Feature Ideas:

- [ ] Add simple protocol to ESP (send V get last V reading ) 
- [ ] Add option of AP mode 
- [ ] Add optical isolation (althought you still pull the 3.3v ESP main power from the BMV unit) 
- [ ] Switch to wifi updatable esp bootloader/firmware 
- [ ] Add can for option of talking to Victron blue sol 3000 or similar via ve-direct (or what ever silly name attached to thier protocol, it's either can or serial with isolation) 



[URL]
Pinouts and protocol examples [Victron BMV Pinouts](http://jeperez.com/connect-bmv-victron-computer/)
ESP iám Using is Node MCU [Node MCU Pinouts] (https://iotbytes.wordpress.com/nodemcu-pinout/)




