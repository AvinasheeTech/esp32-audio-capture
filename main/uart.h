/* @file  uart.c
   @brief header file for uart functions.
   @author Shyam Jha (Avinashee Tech)
*/


#ifndef _UART_H_
#define _UART_H_

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_log.h"
#include "driver/uart.h"
#include "string.h"
#include "driver/gpio.h"

//macros
#define TXD_PIN (GPIO_NUM_17)
#define RXD_PIN (GPIO_NUM_16)

//function declarations
void uart_init(void);
int uart_sendData(const char* logName, void* data, size_t len);

#endif