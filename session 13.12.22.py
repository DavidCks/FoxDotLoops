v2 >> play("-.--*.-.", formant = 1, sample = 3, room = 1, mix = .3, dur = 1/4)
v3 >> play("....o...", formant = 0, sample = a2.sample, room = 1, mix = .3, rate = .1, striate = 1)
v4 >> play("l.ll....l..l....", rate = .8)

v5 >> play("MMMM..V.", pshift = [5,4,3,2,0,0,0,0], amp = [1,1,1,1,1,1,linvar([2,1], 16),1])

v6 >> play("www.w..w", pshift = [3,4,3,2,-21,0,0,-14], room = .3, mix = linvar([1,0], 16), echo = 8, tremolo = 16)

v7 >> play("X.X.", amp = 3, rate = 1, formant = 1)

v8 >> gong([-4.5], chop = P[4].stretch(8) | P[1].stretch(6) | P[2].stretch(2) | P[1].stretch(8), echo = 1.5)

v9 >> play("****", tremolo = 8, pshift = PRand(14), sample = PRand(9))

v3 >> jbass([1,1.5,2,1.5], dur = 4, oct = 6, room = 1, mix = 1, tremolo = 2)

a_all.lpf = 0
a_all.hpf = 0

a_all.room = .3

a_all.hpf = 1000

v_all.lpf = 
v_all.hpf = 1000

a_all.lpf = 1000

a_all.bend = 0

a_all.tremolo = 0

a_all.chop = 0

a_all.glide = 0

a_all.amp = .5
a_all.room = 1
a_all.mix = .1

a5 >> quin([(0,3,5,7),(1,3,5,7),(1,3,5,7),(1,3,5,7),(1,3,5,7),(1,3,5,7),(1,3,5,7),(-1,2,5,8)], chop = 2, tremolo = 0)

b_all.stop

v2 >> play("LLLLfcvgbhj.L...", room = .3, mix = .3, striate = 1, glide = -7, bend = 1)

v3 >> play("x.--o.-.", room = .3, mix = .3, dur = 1/4, chop = 0)

v4 >> ambi(chop = linvar([4,0], 4), room = 1, mix = .3)

v6 >> pads([(4,2),(2,-2),(2,0,-4),(2,0)], dur = 4, chop = 0, sus = 4)

v7 >> pads([11,0,0,0,7,0,0,0,9,0,0,0,0,9,7,4], glide = -4, room = 1, mix = .3, sus = 4, chop = 6, echo = 4, pshift = 0, bend = .7, amp = [1,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1])


a_all.amp = 0

print(FxList)





a_all.stop()

b_all.stop()


Scale.default = "minor"

print()

print(SynthDefs)
