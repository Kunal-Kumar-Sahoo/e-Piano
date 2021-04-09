# e-Piano
A virtual simulated Python program where notes of piano are passed as an argument and an output audio (in .wav file) is produced

Basic Anatomy of Piano:
A piano consists of multiple octaves
1 octave = 7 white keys + 5 black keys

Nomenclature of Piano keys:
White keys: C, D, E, F, G, A, B
Black keys: Named wrt the relative position with an adjacent white key
            b: Flat (if a black key is present on the left of the white key)
            #: Sharp (if a black key is present on the right side of the white key)
            
Our notation: White keys would be denoted as usual but black keys would be identified as sharp keys and would be denoted as corresponding white keys in lower case.

Understanding the wave: The mathematical aspect
We know sound can travel as a Plane-progressive wave having the equation:
y(x, t) = A.sin(wt - kx)
Where
  w = Angular frequency = 2.pi.f; f = frequency of the sound wave
  k = Wave number = 2.pi/lambda; lamda = wavelength of the sound wave

If we neglect the wave-number factor of the equation
y(t) = A.sin(wt) -----As per Physics point of view because the frequency is assumed to be constant

We will keep  t constant and f variable because we will be using multiple keys having different frequencies. So, the equation becomes
y(f) = A.sin(2.pi.f.t)

Now the keys of any instrument is tuned with the help of Resonance of waves and in Piano it is done using "Equal Temperament System" and is given mathematically as:
note_frequency = base_frequency * (2 ** (n/12)); where n is the number of notes away from the base_frequency note
