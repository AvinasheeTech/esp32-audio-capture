/* @file  i2s.h
   @brief header file for ICS43434 microphone based i2s functions.
   @author Shyam Jha (Avinashee Tech)
*/

#ifndef _I2S_H_
#define _I2S_H_

#include <driver/i2s_std.h>
#include <driver/gpio.h>
#include <stdint.h>
#include "freertos/Freertos.h"
#include "freertos/task.h"

//basic defines 
#define SAMPLE_BUFFER_SIZE 512
#define SAMPLE_RATE 16000
//pinouts
#define I2S_MIC_SERIAL_CLOCK GPIO_NUM_14   //bit clock line
#define I2S_MIC_LEFT_RIGHT_CLOCK GPIO_NUM_22  //left right channel clock / WS
#define I2S_MIC_SERIAL_DATA GPIO_NUM_21    //serial data line

//function declarations
void i2s_setup(void);
void i2s_readsamples(void *dest, size_t *bytes_read);


#endif