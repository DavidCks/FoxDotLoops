a1 >> play("V.*.(VW).V.", echo = 1.5, pshift = b3.pshift, room = .3, mix = .3)

b2 >> play("----$...........", sample = PRand(9), dur = 1/4)

b4 >> play("$.PL", echo = 1.5, dur = 1, sample = 4, room = 10, mix = .3, lpf = 500)

b5 >> play("..$.llll", dur = 1, sample = 7)

b3 >> ambi([(0,2,-3)], amp = .3, oct = 6, chop = P[2,4,8,4].stutter(4), pshift = P[0,1,2,1].stutter(4))

b6 >> play(".dfghjklpokiju............LLLL..........", rate = 3, pshift=linvar([0,-7],8), glide = 0, dur = 1/4, room = 10, mix = .3, amp = .75, formant = 0, chop = 4)

b8 >> play("=", dur = 1/2, sample = [1,2,3,4,7,6], chop = P[1,2].stutter(8))

c9 >> keys(glide = 0, amp = 1, echo = 0)

c1 >> pads(P[-2,3,5,0], dur = 4, room = 10, mix = .3)

c6 >> pads(P[0,.5,1,3], chop = [2,4,8, 16], amp = .7, room = 10, mix = .3, dur = 4)
