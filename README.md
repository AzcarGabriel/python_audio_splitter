# Python audio splitter
## Using scipy.io.wavfile


# Use
##Input arguments
- f_in_name: name of the wav to split.
- init_sec: integer second where the new audio will start.
- init_desv: fraction of the second where the new audio will start.
- end_sec: integer second where the new audio will end.
- end_desv: fraction of the second where the new audio will end.
- f_out_name: name of the output wav (without the .wav extension).


##Output
- Wav file.

# Example
- Split audio1.wav between 60.5 to 70.2 seconds. Output: a1.wav
```sh
> python3 splitter.py audio1.wav 60 0.5 70 0.2 a1
```