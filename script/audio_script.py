'''
@file      audio_script.py
@brief     script to record and save audio using ICS43434
@author    Shyam Jha (Avinashee Tech)
'''

import serial
import wave
import time

# --- Serial Configuration ---
SERIAL_PORT = 'COM8'  # Replace with your serial port 
BAUD_RATE = 921600
OUTPUT_FILENAME = 'recorded_audio.wav'

# --- Audio characteristics ---
SAMPLE_RATE = 16000   # Samples per second
CHANNELS = 1          # Mono
SAMPLE_WIDTH = 4      # 4 bytes = 32-bit audio
RECORD_SECONDS = 20   # Duration to record

'''
@brief  connect to uart device, record i2s audio data and saves it to a WAV file.
@retval None
'''
def record_audio_from_serial():

    audio_frames = []  # List to save audio data

    try:
        # Establish serial connection with a timeout of 1 second
        ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUD_RATE,
            timeout=1
        )
        print(f"Connected to serial port {SERIAL_PORT} at {BAUD_RATE} baud.")

        # Wait a moment for the connection to establish and DMA to start
        time.sleep(2) 

        print(f"Recording for {RECORD_SECONDS} seconds...")
        start_time = time.time()

        while (time.time() - start_time) < RECORD_SECONDS:
            # Read all available bytes from the serial buffer
            data = ser.read(ser.in_waiting)
            if data:
                audio_frames.append(data)
        
        # Stop recording and close the serial port
        ser.close()
        print("Recording stopped. Serial port closed.")

    except serial.SerialException as e:
        print(f"Error opening or communicating with the serial port: {e}")
        return

    if not audio_frames:
        print("No audio data received.")
        return

    # Combine the list of byte objects into a single byte string
    pcm_data = b''.join(audio_frames)
    print(f"Received {len(pcm_data)} bytes of PCM data.")

    # Save the PCM data to a WAV file
    try:
        with wave.open(OUTPUT_FILENAME, 'wb') as wav_file:
            wav_file.setnchannels(CHANNELS)
            wav_file.setsampwidth(SAMPLE_WIDTH)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(pcm_data)
        print(f"Audio saved successfully to {OUTPUT_FILENAME}")
    except Exception as e:
        print(f"Error writing WAV file: {e}")

if __name__ == '__main__':
    record_audio_from_serial()
