# this is why you don't vibe a midi file for ufnnies

# Building a multi-track MIDI file (melody + bass + harmony) with a more detailed transcription of MEGALOVANIA.
# This writes /mnt/data/megalovania_full.mid and returns the filename.
from pathlib import Path
import mido

def make_more_accurate_midi(filename="megalovania_snippet.mid", tempo_bpm=240, ticks_per_quarter=480):
    # create midi file
    mid = mido.MidiFile(type=1, ticks_per_beat=ticks_per_quarter)

    # Track 0: global + melody on channel 0
    t0 = mido.MidiTrack()
    mid.tracks.append(t0)

    microseconds_per_quarter = mido.bpm2tempo(tempo_bpm)

    # tempo meta (delta 0)
    t0.append(mido.MetaMessage('set_tempo', tempo=microseconds_per_quarter, time=0))
    # time signature 4/4
    t0.append(mido.MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
    # program change: Acoustic Grand Piano on channel 0
    t0.append(mido.Message('program_change', program=0, channel=0, time=0))

    # MEGALOVANIA main riff, note names:
    # D D D A G# G F D F G C C D A G# G F D F G B B D A G# G F D F G
    # A# A# D A G# G F D F G F F F F D D D F F F G G# G F D F G F F F
    # G G# A C A D D D A D C A A A A G G G A A A A G A C A G D A G F C
    # G F E D D D D F C F D F G G# G F
    #
    # Pitches are mapped near the original register:
    #   C=72, D=74, E=76, F=77, G=79, G#=80, A=81, A#=82, B=83.
    # Durations are mostly 1/8 notes (0.5 quarter) with occasional 1/4 notes.
    melody_seq = [
        # Phrase 1
        (74, 0.5, 120), (74, 0.5, 120), (74, 1.0, 122),
        (81, 1.0, 124), (80, 0.5, 120), (79, 0.5, 118), (77, 1.0, 118),
        (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),
        (72, 0.5, 116), (72, 0.5, 116), (74, 1.0, 120),
        (81, 1.0, 124), (80, 0.5, 120), (79, 0.5, 118), (77, 1.0, 118),
        (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),
        (83, 0.5, 124), (83, 0.5, 124),
        (74, 1.0, 120), (81, 1.0, 124), (80, 0.5, 120), (79, 0.5, 118),
        (77, 1.0, 118), (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),

        # Phrase 2 (Bb variation)
        (82, 1.0, 124), (82, 0.5, 124),
        (74, 1.0, 120), (81, 1.0, 124), (80, 0.5, 120), (79, 0.5, 118),
        (77, 1.0, 118), (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),

        (77, 0.5, 118), (77, 0.5, 118), (77, 0.5, 118), (77, 1.0, 118),
        (74, 0.5, 120), (74, 0.5, 120), (74, 1.0, 120),
        (77, 0.5, 120), (77, 0.5, 120), (77, 1.0, 120),
        (79, 0.5, 122), (80, 0.5, 124), (79, 0.5, 120), (77, 1.0, 118),
        (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),

        (77, 0.5, 118), (77, 0.5, 118), (77, 0.5, 118),
        (79, 0.5, 122), (80, 0.5, 124), (81, 1.0, 124),
        (72, 0.5, 116), (81, 1.5, 124),

        # Phrase 3
        (74, 0.5, 120), (74, 0.5, 120), (74, 1.0, 120),
        (81, 1.0, 124), (74, 0.5, 120), (72, 0.5, 116), (81, 1.0, 124),

        (81, 0.5, 124), (81, 0.5, 124), (81, 1.0, 124),
        (79, 0.5, 120), (79, 0.5, 120), (79, 1.0, 120),
        (81, 0.5, 124), (81, 0.5, 124), (81, 1.0, 124),
        (81, 0.5, 124), (79, 0.5, 120), (81, 1.0, 124),
        (72, 0.5, 116), (81, 1.0, 124),

        (79, 0.5, 120), (74, 0.5, 120), (81, 1.0, 124),
        (79, 0.5, 120), (77, 0.5, 118), (72, 0.5, 116),
        (79, 1.0, 120), (77, 0.5, 118), (76, 1.0, 118),

        # Phrase 4 (closing)
        (74, 0.5, 120), (74, 0.5, 120), (74, 0.5, 120), (74, 1.0, 120),
        (77, 1.0, 120), (72, 0.5, 116), (77, 1.0, 120),
        (74, 0.5, 120), (77, 0.5, 120), (79, 1.0, 122),
        (80, 0.5, 124), (79, 0.5, 120), (77, 1.5, 118),
    ]

    # melody: sequential notes, durations in quarters
    for note, dur_q, vel in melody_seq:
        ticks = int(dur_q * ticks_per_quarter)
        t0.append(mido.Message('note_on', note=note, velocity=vel, channel=0, time=0))
        t0.append(mido.Message('note_off', note=note, velocity=64, channel=0, time=ticks))

    # Track 1: Bassline on channel 1 (left hand pattern from score)
    t1 = mido.MidiTrack()
    mid.tracks.append(t1)

    # Fingered Bass: GM program 33 -> zero-based index 32
    t1.append(mido.Message('program_change', program=32, channel=1, time=0))

    # Bass pattern approximating the piano sheet:
    # D octave pattern for two bars, then Bb, C, A.
    # Using D2=38, D3=50, Bb1=34, Bb2=46, C2=36, C3=48, A1=33, A2=45.
    bass_seq = [
        # bar 1-2: D minor (octaves)
        (38, 0.5), (50, 0.5), (38, 0.5), (50, 0.5),
        (38, 0.5), (50, 0.5), (38, 1.0),
        (38, 0.5), (50, 0.5), (38, 0.5), (50, 0.5),
        (38, 0.5), (50, 0.5), (38, 1.0),

        # bar 3: Bb
        (34, 0.5), (46, 0.5), (34, 0.5), (46, 0.5),
        (34, 0.5), (46, 0.5), (34, 1.0),

        # bar 4: C
        (36, 0.5), (48, 0.5), (36, 0.5), (48, 0.5),
        (36, 0.5), (48, 0.5), (36, 1.0),

        # bar 5: A
        (33, 0.5), (45, 0.5), (33, 0.5), (45, 0.5),
        (33, 0.5), (45, 0.5), (33, 1.0),
    ]

    # repeat bass pattern, encoding the flag in the velocity
    flag = "amateursCTF{h1t_th3_n0t3s}"
    for cycle in range(5):
        for j, (note, dur_q) in enumerate(bass_seq):
            # linear step index over cycles
            step_index = cycle * len(bass_seq) + j
            flag_index = step_index % len(flag)
            vel = ord(flag[flag_index])
            ticks = int(dur_q * ticks_per_quarter)
            t1.append(mido.Message('note_on', note=note, velocity=vel, channel=1, time=0))
            t1.append(mido.Message('note_off', note=note, velocity=64, channel=1, time=ticks))

    # Track 2: Harmony / chords on channel 2
    t2 = mido.MidiTrack()
    mid.tracks.append(t2)

    # program 4 (Electric Piano 1, etc.)
    t2.append(mido.Message('program_change', program=4, channel=2, time=0))

    chord_seq = [
        # (notes_list, duration_q)
        ([74, 77, 81], 2.0),  # Dm (D5,F5,A5) held 2 quarters
        ([70, 74, 77], 2.0),  # Bb (Bb4,D5,F5)
        ([72, 76, 79], 2.0),  # C (C5,E5,G5) -- using E natural as 76 (E5)
        ([69, 72, 76], 2.0),  # A (A4,C#5?,E5) approximated with C5 (72) instead of C#
    ]

    first_chord = True
    for _ in range(2):
        for notes, dur_q in chord_seq:
            ticks = int(dur_q * ticks_per_quarter)

            delta_on = 0 if first_chord else 0
            first_chord = False

            # first note_on carries the delta, others at same tick (time=0)
            t2.append(mido.Message('note_on', note=notes[0], velocity=80, channel=2, time=delta_on))
            for n in notes[1:]:
                t2.append(mido.Message('note_on', note=n, velocity=78, channel=2, time=0))

            # first note_off carries duration, others at same tick (time=0)
            t2.append(mido.Message('note_off', note=notes[0], velocity=64, channel=2, time=ticks))
            for n in notes[1:]:
                t2.append(mido.Message('note_off', note=n, velocity=64, channel=2, time=0))

    # save
    mid.save(filename)
    return filename

# Call the function explicitly when running this script
if __name__ == "__main__":
    make_more_accurate_midi(filename="megalovania_snippet.mid", tempo_bpm=100, ticks_per_quarter=960)