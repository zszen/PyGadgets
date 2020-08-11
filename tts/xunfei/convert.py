# import pywav

# wave_read = pywav.WavRead("demo.pcm")
# # # print parameters like number of channels, sample rate, bits per sample, audio format etc
# # # Audio format 1 = PCM (without compression)
# # # Audio format 6 = PCMA (with A-law compression)
# # # Audio format 7 = PCMU (with mu-law compression)
# print(wave_read.getparams())

# # wave_write = pywav.WavWrite("demo.wav", 1, 8000, 8, 1)
# # # raw_data is the byte array. Write can be done only once for now.
# # # Incremental write will be implemented later
# # with open('demo.pcm','r') as f:
# #     wave_write.write(f)
# # # close the file stream and save the file
# # wave_write.close()