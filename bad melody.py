a1 >> pluck([0,1,2,3], chop = 4, oct = 3, room=.5, mix=.5, lpf = 1000)
a2 >> pluck([0,2,1,3], oct = 4, dur = 4, room = .5, mix = .5, chop = 8, lpf = 1000)

a3 >> space([(0,2,-3),(0,2,4),(0,1,-4),(0,3),  (0,2,-3),(0,2,4),(0,1,7),(0,7)], glide = [7,-7],  chop = [0,0,0,16], dur = 2, sus = 4, room = .3, mix = .3, amp = 1, oct = 4)

b1 >> play("s.s.", dur = .25, echo = .25, lpf = 1500, room = 1, mix = linvar([.2,.8], 16), amp = var([2,0],[16,16]))
b2 >> play("~.~.*X~.~.~.*X~.", sample = 5, lpf = 4000, amp = .5, echo = .25, chop = 2, vib = 1, vibdepth = 1, rate = var([linvar([.5,-.5],8),1],[8,8]))
b3 >> play("V.-.V.-.V.-.(MV).--", sample = 2, dur = .25, lpf = [1000,0,0,0], rate = 1)
b4 >> play("-.-.-.-.-.-(-.)-.-...(x.).(x.).(x.).(K.).(x.).K.(K.).", dur = .125, rate = .5, bend = .1)

c1 >> sinepad([1,2,0,0,2,3,1,4], glide = [0,0,0,7,0,7,0,-7], chop = [3,6,3,9], room = .1, mix = .5, dur = 2, amp = 2, formant = linvar([0,.5],8), slide = [0,0,0,-3])

a_all.slide = [0,0,0,-1]
b_all.slide = [-2,0,0,0,-2,0,0,0,1,0,0,0,-1,0,0,0]
b_all.room = 10
b_all.mix = .3
b_all.amp = .5
c1.room = 10
c1.mix = .1
a_all.mix = 1
a_all.room = .3

b_all.lpf = 5000

a_all.stop()
b_all.stop()
c_all.stop()

print(FxList)


Scale.default = "minor"
