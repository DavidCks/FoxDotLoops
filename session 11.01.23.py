a1 >> play("K(K.)R(.K)", rate = 1, tremolo = [0,0,4,0], lpf = 300, amp = 4, formant = 1, pshift = [-7,-5,-12,0], sample = 3)
a2 >> play(".#.*", sample = 1)

a3 >> fuzz(dur = var([PDur(3,8),PDur(5,8)],4), lpf = 300, tremolo = 3, amp = 2)

a4 >> play("E..", sample = 2, rate = 1, dur = 4, amp = 1)

a5 >> play("(o/).u.", sample = 4, room = 1, mix = .3, rate = -1)
a6 >> play("pp..", bend = 1, sample = 1, room = 1, mix = 2)

a7 >> glass(PRand(4) * 2, chop = var([8,4],8), room = 1, mix = 1)

a9 >> play("-x-x", sample = 4, room = 1, mix = .1)

b1 >> sinepad(pshift = linvar([-3,6], 8), room=1, mix=.2, chop = 2, amp = var([3,0],[9,7]))

b2 >> dirt(amp = 2, dur = PDur(3,8), vib = 1, vibdepth = .15, pshift = var([linvar([0,40],8),0,linvar([0,24],8),0],8), tremolo = var([4,16,8,20,2,3,2,3],2)) 

b3 >> pluck( dur = [1/2, 1/2, 1/4, 1/4, 1/4, 1/4], room = 1, mix = .3, formant = linvar([3,4],16), amp = var([linvar([-2,3],16),.5],16))


Clock.bpm = 180
print(SynthDefs)

