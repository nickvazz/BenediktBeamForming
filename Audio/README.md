# BenediktBeamForming

Physics 180 Report
Details of Code Objectives
George Condit
The purpose of our research is, on a high level, to create a method to passively, efficiently, and accurately
monitor student interactions in the classroom. However, the basis for our method hinges on the concept of
acoustic beamforming- the process of manipulating multi-channel audio to syncopate desired wave patterns
and facilitate the occurrence of constructive interference. This interference virtually ‘amplifies’ the signal from
a desired source. At this point in our research, we are avoiding any attempt at accomplishing this in real time,
although real time manipulation is on the project’s horizon.

On a lower level, this is accomplished using bit transposition within our gathered WAV files.

Our objectives are, for the time being, as follows:

-Calculate the time elapsed from signal generation until signal reception for each individual mic

 Given angle of target with respect to array center

 Given distance to target with respect to array center

 Given a defined speed of sound

-Open recorded file for reading

 Naming convention to be determined. Factors include (but are not limited to) channel number,
recording date, or custom input filename.

-Open new (separate) file for writing

-Read recorded file’s header information and copy+paste into new file’s header

 Bit depth

 Sample rate

-Loop from “data” (header tag) until the end of file.

-Given angle and distance (including individual mic distance), begin bit transposition

 Sample rate: 92kHz (92,000 samples per second)

 24 bit: 3 bytes per sample

 276 bytes/second

 Transposition amount is equal number of samples in time delay between microphone reception
