delete all
load ../Inputs/5P21.pdb, main
hide all
bg_color white
show cartoon, (chain A)
color white

set_color color1, [0.000,0.040,1.000]
create sector1, (resi 51,13,135,149,59,58,62,140,201,68,55,206,196,209,66,142,178,151,130,157,207,14,176,138,150,24,146,200,133,184,247,185,217,152,153,28,160,53,80,145,141,123,154,91,225,158,52,120) & (chain A)
color color1, sector1
show spheres, sector1
show surface, sector1

set_color color2, [1.000,0.000,0.000]
create sector2, (resi 143,147,136,8,128,15,159,127,17,115,214,114,27,137,208,126,63,220,98,57,71) & (chain A)
color color2, sector2
show spheres, sector2
show surface, sector2

set_color color_ic1, [1.000,0.000,0.000]
create ic_1, (resi 51,13,135,149,14,133,152,153,160,145,123,154,91,158,52,120) & (chain A)
color color_ic1, ic_1
show spheres, ic_1
show surface, ic_1

set_color color_ic2, [1.000,0.667,0.000]
create ic_2, (resi 59,140,201,206,178,157,207,176,150,146,184,217,53,80,225) & (chain A)
color color_ic2, ic_2
show spheres, ic_2
show surface, ic_2

set_color color_ic3, [0.667,1.000,0.000]
create ic_3, (resi 58,62,68,55,196,209,66,142,151,130,138,24,200,247,185,28,141) & (chain A)
color color_ic3, ic_3
show spheres, ic_3
show surface, ic_3

set_color color_ic4, [0.000,1.000,0.000]
create ic_4, (resi 143,8,159,115,114,27,208,220,98) & (chain A)
color color_ic4, ic_4
show spheres, ic_4
show surface, ic_4

set_color color_ic5, [0.000,1.000,0.667]
create ic_5, (resi ) & (chain A)
color color_ic5, ic_5
show spheres, ic_5
show surface, ic_5

set_color color_ic6, [0.000,0.667,1.000]
create ic_6, (resi 147,136,128,15,127,17,214,137,126,63,57,71) & (chain A)
color color_ic6, ic_6
show spheres, ic_6
show surface, ic_6

set_color color_ic7, [0.000,0.000,1.000]
create ic_7, (resi 102,193) & (chain A)
color color_ic7, ic_7
show spheres, ic_7
show surface, ic_7

set_color color_ic8, [0.667,0.000,1.000]
create ic_8, (resi 20,21,162,11,16,84,10,204,25,65,161) & (chain A)
color color_ic8, ic_8
show spheres, ic_8
show surface, ic_8

set_color color_ic9, [1.000,0.000,0.667]
create ic_9, (resi 189,60,191,188,205,203,192,183,174,131,75,132,199,224) & (chain A)
color color_ic9, ic_9
show spheres, ic_9
show surface, ic_9

zoom
set transparency, 0.4
ray
png PF00071
