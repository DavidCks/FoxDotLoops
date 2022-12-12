a1 >> play("X..X....X.X.....", sample = 3, rate = .5, formant = 0)

a2 >> play(".+..-.~.#...-.+.", rate = .2)

b5 >> play("..........#.....", sample = 0, dur = 1/2, pshift = var([3,4,5,8,-2],8), rate = .2)

b6 >> space([linvar([20,49],6)], amp = var([linvar([0,.02],12), 0,.015],[16,16]), drive = 1, dur = 1, oct = 5, pshift = 1, glide = [-14,0,14,0], chop = 2)

c1 >> keys(PZip( PEuclid2(3,8,4,7), PEuclid2(3,8,2,9), PEuclid2(3,8,6,0)) | PZip(P[0,1,1,0,1,0,1,0] * 2, P[-3, 4]), room = 1, mix = 1, amp = P[0].stretch(24) | P[1].stretch(16),  pshift = 1)
