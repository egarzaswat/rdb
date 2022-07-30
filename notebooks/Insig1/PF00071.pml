delete all
load ../Inputs/5P21.pdb, main
hide all
bg_color white
show cartoon, (chain A)
color white

set_color color1, [0.000,0.040,1.000]
create sector1, (resi 76,13,173,98,113,94,116,112,81,162,48,60,88,179,178,103,84,52,120,108,7,63,136,49,121,165,181,174,6,175,169,125,109,92,20,168,172,167,56,44,97,10,115,107,105,86,14,91,100,53,171,177,61,117,166,110,176,93,147,126,89,95) & (chain A)
color color1, sector1
show spheres, sector1
show surface, sector1

set_color color2, [1.000,0.000,0.000]
create sector2, (resi 75,62,158,163,150,58,9,137,12,133,159,78,17) & (chain A)
color color2, sector2
show spheres, sector2
show surface, sector2

set_color color_ic1, [1.000,0.000,0.000]
create ic_1, (resi 13,98,113,94,112,52,165,174,169,44,91,100,110,93) & (chain A)
color color_ic1, ic_1
show spheres, ic_1
show surface, ic_1

set_color color_ic2, [1.000,1.000,0.000]
create ic_2, (resi 76,173,48,84,108,7,136,49,121,109,20,172,167,97,10,107,14,53,171,61,117,166,176,147) & (chain A)
color color_ic2, ic_2
show spheres, ic_2
show surface, ic_2

set_color color_ic3, [0.000,1.000,0.000]
create ic_3, (resi 116,81,162,60,88,179,178,103,120,63,181,6,175,125,92,168,56,115,105,86,177,126,89,95) & (chain A)
color color_ic3, ic_3
show spheres, ic_3
show surface, ic_3

set_color color_ic4, [0.000,1.000,1.000]
create ic_4, (resi 75,62,158,163,150,58,9,137,12,133,159,78,17) & (chain A)
color color_ic4, ic_4
show spheres, ic_4
show surface, ic_4

set_color color_ic5, [0.000,0.000,1.000]
create ic_5, (resi 21,19,28,80,90,82,29,99,143,22) & (chain A)
color color_ic5, ic_5
show spheres, ic_5
show surface, ic_5

set_color color_ic6, [1.000,0.000,1.000]
create ic_6, (resi 42,122,87,146,182) & (chain A)
color color_ic6, ic_6
show spheres, ic_6
show surface, ic_6

zoom
set transparency, 0.4
ray
png PF00071
