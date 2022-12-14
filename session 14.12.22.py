a1 >> play("X.~X*.X~-.-.*V*V", sample = 4, vib = .1, vibdepth = -.5, room = 5, mix = .1)
    
a2 >> play("V...", rate = 2)

a3 >> play("..V.", rate = 1)

a4 >> sinepad(dur = 1/4, amp = P[1,1,1,0, 1,1,1,0, 1,0,1,1, 1,1,1,0], pshift = linvar([6,0], 32), room = 10, mix = .3, vib = 2, vibdepth = 1)

b4 >> dbass( dur = 1/4, amp = P[a4.amp].reverse(), pshift = P[0].stretch(16) | P[.5].stretch(16) | P[1].stretch(16) | P[.5].stretch(16))

b5 >> play("L.o.", sample = 4, room = 1, mix = .3)

c6 >> play("P.", sample = 3, pshift = var([3,3,5,4],[8,8,8,8]))
c7 >> play("P.", sample = 3, pshift = var([0,1,2],[8,8,16]))

d8 >> play("K...(K.)...KKK.K.K.", dur = 1/4, amp = 2, sample = PRand(9), mix = .3, room = .3)

d9 >> play("o.ooo.o.o.....", dur = d8.dur, sample = 2)

c_all.lpf = 00

d_all.formant = [0,0,1]

a4.formant = [1,0,0]

a4.bend = [0,0,.3]

a4.echo = [0,0,.5]

c_all.shape = -.1
c_all.room = 1
c_all.mix = .3

c_all.formant = 1

Clock.bpm = linvar([200,50], 128)

Clock.bpm = 220

a_all.pshift = var([linvar([7, -14], 64), var([linvar([7, 0], 32),0],[4,4])],[32,64 + 32])
b_all.pshift = a_all.pshift
c_all.pshift = a_all.pshift
d_all.pshift = a_all.pshift


x = var([linvar([1000,10000],8), 0],[8,24])

a_all.lpf = x
b_all.lpf = x
c_all.lpf = x
d_all.lpf = x

a_all.hpf = x /100
b_all.hpf = x /100
c_all.hpf = x /100
d_all.hpf = x /100


Clock.bpm = 200
