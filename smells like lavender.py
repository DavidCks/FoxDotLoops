a2 >> space(P[8,7,5,4] | [9,8,5,4], hpf = 1000, lpf = 200, formant = 2, amp = .25, drive = 1, vib = 8, vibdepth = .02)

a1 >> pads([(0,4),(0,2)], tremolo = 2, amp = linvar([-.5,1], 8), pshift = [0,0,0,1], formant = -1, oct = 4, dur = 4)

a3 >> play("x.xx..xxx.x.;.x.", rate = .2, sample = 3, striate = 1, swell = 1, amp = 1)

a4 >> ambi([0,4,7,11,10,9,8], dur = [4,4,6,2,4,4,6], amp = .3)

a5 >> ambi(PRand(7) - 7, dur = 4)

a8 >> pads([(0,2),(0,4),(3,1),(1,-1)], blur = 16, dur = 8, oct = 5, amp = .5, room = 1, mix = .3)
a9 >> pads(P[0].stretch(12) | P[4].stretch(12) | P[-1].stretch(12) | P[3].stretch(12), amp = 1.2, chop = [3,3,2], dur = PDur(3,8), room = 1, mix = .3, scale = Scale.minor)

a6 >> pluck(P[1,4,0,0,2,3,6,3,2,1], dur = [1,1,.5,.5,1,1,1,.5,.5,1], oct = 4, blur = 6, room = .8, mix = .3, formant = linvar([2,0],8), vib = 2, vibdepth = .02)

a7 >> snick(amp = linvar([1,-1],16))

Scale.default = "minor"

