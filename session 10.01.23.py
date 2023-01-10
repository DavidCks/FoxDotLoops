a1 >> sinepad([0], dur = PDur(5, 8), amp = [1,1,1,0,0,0])

x1 >> play("....###.", pshift = [0,0,0,0,0,-4,var([5,4,3,2],[4]),0], sus = .1, room = 1, mix = .3, rate = .5)
x2 >> play("x.xxx.x.", dur = 1/4)
x3 >> play(".-..*.-.", sample = 0)


l = var([2,0],[4,12])
a2 >> jbass(chop = l)

a3 >> space(pshift=linvar([0,-14],4), amp = var([1,0],[5,2]), room = 1, mix = .3, vib = 16, vibdepth = .5, oct = var([4.3,5,5.7,5],8))

Scale.default = "minor"

x_all.room = .3
x_all.mix = .3

x4 >> play("<---------><.x.x.x.x.x.x.#>", dur = 1/4, chop = 0, rate=[1,-1], pshift=linvar([0,-8],4), amp = var([1,0],8))

a4 >> pads([(0,2,-2),(2,4),(0,2),(4,6)], dur = 4, vib = 4, amp = .3, vibdepth = .05)

a5 >> bass([-5,-5,-7,-7,-5,-5,-3,-3], dur = 2, oct = 5, amp = .4, drive = 1)

a6 >> bass(dur = 1/4, amp = 1.25, oct = 4)

x5 >> play("<#-*R><VGV.>", pshift = var([0,2,3,3,3,2,2,0,0],2), chop = 2, rate = -1, amp = 1)


