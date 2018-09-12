import scipy.io.wavfile as wav
import sys

def split_audio(f_in_name, init_sec, init_desv, end_sec, end_desv, f_out_name):
    print("From " + f_in_name + " extracting " + f_out_name)
    (rate, sig) = wav.read(f_in_name)
    i = rate * init_sec + int(rate * init_desv)
    e = rate * end_sec + int(rate * end_desv)
    wav.write(f_out_name+".wav", rate, sig[i:e])

if len(sys.argv) != 7:
    print("Wrong format. It should be f_in_name init_sec init_desv end_sec end_desv f_out_name")
else:
    f_in = str(sys.argv[1])
    f_out = str(sys.argv[6])

    init_sec = int(sys.argv[2])
    init_desv = float(sys.argv[3])

    end_sec = int(sys.argv[4])
    end_desv = float(sys.argv[5])

    split_audio(f_in, init_sec, init_desv, end_sec, end_desv, f_out)