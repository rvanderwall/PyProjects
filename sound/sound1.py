
if False:
    from playsound import playsound
    playsound('sample1.mp3')

if True:
    import simpleaudio as sa
    filename = 'PinkPanther30.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

if False:
    import simpleaudio as sa
    import numpy as np

    frequency = 440
    fs = 44100
    seconds = 3

    t = np.linspace(0, seconds, seconds * fs, False)
    note = np.sin(frequency * t * 2 * np.pi)

    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj. wait_done()


