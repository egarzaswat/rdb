delete all
load ../Inputs/5P21.pdb, main
hide all
bg_color white
show cartoon, (chain A)
color white

set_color color1, [0.000,0.040,1.000]
create sector1, (resi 487,496,188,483,383,353,290,424,281,495,174,360,425,391,442,345,77,472,485,452,479,214,346,413,264,150,486,337,447,318,122,317,406,46,348,460,314,312,463,462,455,480,335,388,331,470,476,398,375,454,288,356,481,342,488,456,409,131,338,313,285,333,341,405,334,282,125,218,311,402,310,469,339,268,448,224,386,306,132,18,273,484,173,156,263,26,203,319,440,449,493,332,403,54,301,76,368,471,205,364,283,259,207,410,347,416,197,190,270,477,373,17,394,491,474,441) & (chain A)
color color1, sector1
show spheres, sector1
show surface, sector1

set_color color2, [1.000,0.000,0.000]
create sector2, (resi 9,11,434,376,427,378,10,371,439,6,199,350,475,8,292,359,382,445,154,437,279,417,355,420,217,14,277,161,446,160,60,362,133,144,412,367,169,16,44,291,146,19,40,253,265,302,15,13,56,134,468,20,120,66,365) & (chain A)
color color2, sector2
show spheres, sector2
show surface, sector2

set_color color_ic1, [1.000,0.000,0.000]
create ic_1, (resi 391,345,472,479,346,413,337,406,348,460,462,455,480,335,331,470,476,398,356,481,342,488,456,409,338,313,285,341,405,334,282,218,311,402,310,469,339,448,224,386,306,273,484,263,440,449,493,332,403,76,368,471,205,283,259,410,347,416,270,477,373,17,394,491,474) & (chain A)
color color_ic1, ic_1
show spheres, ic_1
show surface, ic_1

set_color color_ic2, [1.000,0.600,0.000]
create ic_2, (resi 487,496,483,383,353,424,495,360,442,485,452,214,264,150,486,318,317,314,463,388,319,441) & (chain A)
color color_ic2, ic_2
show spheres, ic_2
show surface, ic_2

set_color color_ic3, [0.800,1.000,0.000]
create ic_3, (resi 188,290,281,174,425,77,447,122,46,312,375,454,288,131,333,125,268,132,18,173,156,26,203,54,301,364,207,197,190) & (chain A)
color color_ic3, ic_3
show spheres, ic_3
show surface, ic_3

set_color color_ic4, [0.200,1.000,0.000]
create ic_4, (resi 434,427,439,199,475,359,445,437,417,355,217,14,60,362,133,412,367,44,13,120) & (chain A)
color color_ic4, ic_4
show spheres, ic_4
show surface, ic_4

set_color color_ic5, [0.000,1.000,0.400]
create ic_5, (resi 376,378,371,350,292,382,154,279,420,277,161,446,160,144,169,291,146,19,253,265,302,56,134,468) & (chain A)
color color_ic5, ic_5
show spheres, ic_5
show surface, ic_5

set_color color_ic6, [0.000,1.000,1.000]
create ic_6, (resi 9,11,10,6,8,16,40,15,20,66,365) & (chain A)
color color_ic6, ic_6
show spheres, ic_6
show surface, ic_6

set_color color_ic7, [0.000,0.400,1.000]
create ic_7, (resi 48,489,79,266,457,465,473,321,407,401,444,211,466,363,309,75,138,351,458,428,308,118,12,275,430,482,459,213,307,269,433,274,450,284,305,352,397,165,158,392,210,296,389,294,68,257,289,349,411,490,372) & (chain A)
color color_ic7, ic_7
show spheres, ic_7
show surface, ic_7

set_color color_ic8, [0.200,0.000,1.000]
create ic_8, (resi 492,61,344,464) & (chain A)
color color_ic8, ic_8
show spheres, ic_8
show surface, ic_8

set_color color_ic9, [0.800,0.000,1.000]
create ic_9, (resi 208,421,369,438,423,399,221,453,320,414,315,220,59,278,272,358,50,328,379,323,435,304,316,141,400,418,113,55,271,361,443,325) & (chain A)
color color_ic9, ic_9
show spheres, ic_9
show surface, ic_9

set_color color_ic10, [1.000,0.000,0.600]
create ic_10, (resi ) & (chain A)
color color_ic10, ic_10
show spheres, ic_10
show surface, ic_10

zoom
set transparency, 0.4
ray
png PF00071
