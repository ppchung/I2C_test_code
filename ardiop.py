#include "arduino.h"
#include "arduino_io_switch.h"

int main(){
        arduino_init(0,1);

        config_arduino_switch(A_GPIO, A_GPIO, A_GPIO, A_GPIO, IIC, IIC, D_UART, D_UART, D_GPIO,$

        u8 rawdata;

        spi_transfer(0x00, 1, rawdata, NULL);

        printf(rawdata);
}
