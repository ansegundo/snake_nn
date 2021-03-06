import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

prediction = [
  "right",
  "right",
  "right",
  "right",
  "right",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "left",
  "left",
  "left",
  "down",
  "down",
  "down",
  "down",
  "down",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "left",
  "left",
  "left",
  "left",
  "left",
  "down",
  "down",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "left",
  "up",
  "up",
  "up",
  "up",
  "up",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "up",
  "up",
  "up",
  "up",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "left",
  "left",
  "left",
  "left",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "down",
  "down",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "up",
  "up",
  "up",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "left",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "left",
  "right",
  "right",
  "right",
  "right",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "up",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "down",
  "down",
  "down",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right",
  "right"
]

data_to_eval = [
    [
      3,
      0,
      10,
      10,
      12.206555615733702,
      0,
      0
    ],
    [
      4,
      0,
      10,
      10,
      11.661903789690601,
      0,
      0
    ],
    [
      5,
      0,
      10,
      10,
      11.180339887498949,
      0,
      0
    ],
    [
      6,
      0,
      10,
      10,
      10.770329614269007,
      0,
      0
    ],
    [
      6,
      1,
      10,
      10,
      9.848857801796104,
      0,
      3
    ],
    [
      6,
      2,
      10,
      10,
      8.94427190999916,
      0,
      3
    ],
    [
      6,
      3,
      10,
      10,
      8.06225774829855,
      0,
      3
    ],
    [
      6,
      4,
      10,
      10,
      7.211102550927978,
      0,
      3
    ],
    [
      6,
      5,
      10,
      10,
      6.4031242374328485,
      0,
      3
    ],
    [
      6,
      6,
      10,
      10,
      5.656854249492381,
      0,
      3
    ],
    [
      6,
      7,
      10,
      10,
      5,
      0,
      3
    ],
    [
      6,
      8,
      10,
      10,
      4.47213595499958,
      0,
      3
    ],
    [
      6,
      9,
      10,
      10,
      4.123105625617661,
      0,
      3
    ],
    [
      6,
      10,
      10,
      10,
      4,
      0,
      3
    ],
    [
      7,
      10,
      10,
      10,
      3,
      0,
      0
    ],
    [
      8,
      10,
      10,
      10,
      2,
      0,
      0
    ],
    [
      9,
      10,
      10,
      10,
      1,
      0,
      0
    ],
    [
      10,
      10,
      3,
      7,
      7.615773105863909,
      1,
      0
    ],
    [
      11,
      10,
      3,
      7,
      8.54400374531753,
      1,
      0
    ],
    [
      12,
      10,
      3,
      7,
      9.486832980505138,
      1,
      0
    ],
    [
      13,
      10,
      3,
      7,
      10.44030650891055,
      1,
      0
    ],
    [
      14,
      10,
      3,
      7,
      11.40175425099138,
      1,
      0
    ],
    [
      14,
      9,
      3,
      7,
      11.180339887498949,
      1,
      2
    ],
    [
      14,
      8,
      3,
      7,
      11.045361017187261,
      1,
      2
    ],
    [
      14,
      7,
      3,
      7,
      11,
      1,
      2
    ],
    [
      13,
      7,
      3,
      7,
      10,
      1,
      1
    ],
    [
      12,
      7,
      3,
      7,
      9,
      1,
      1
    ],
    [
      11,
      7,
      3,
      7,
      8,
      1,
      1
    ],
    [
      10,
      7,
      3,
      7,
      7,
      1,
      1
    ],
    [
      9,
      7,
      3,
      7,
      6,
      1,
      1
    ],
    [
      8,
      7,
      3,
      7,
      5,
      1,
      1
    ],
    [
      7,
      7,
      3,
      7,
      4,
      1,
      1
    ],
    [
      6,
      7,
      3,
      7,
      3,
      1,
      1
    ],
    [
      5,
      7,
      3,
      7,
      2,
      1,
      1
    ],
    [
      4,
      7,
      3,
      7,
      1,
      1,
      1
    ],
    [
      3,
      7,
      6,
      17,
      10.44030650891055,
      2,
      1
    ],
    [
      3,
      8,
      6,
      17,
      9.486832980505138,
      2,
      3
    ],
    [
      3,
      9,
      6,
      17,
      8.54400374531753,
      2,
      3
    ],
    [
      3,
      10,
      6,
      17,
      7.615773105863909,
      2,
      3
    ],
    [
      3,
      11,
      6,
      17,
      6.708203932499369,
      2,
      3
    ],
    [
      3,
      12,
      6,
      17,
      5.830951894845301,
      2,
      3
    ],
    [
      4,
      12,
      6,
      17,
      5.385164807134504,
      2,
      0
    ],
    [
      5,
      12,
      6,
      17,
      5.0990195135927845,
      2,
      0
    ],
    [
      6,
      12,
      6,
      17,
      5,
      2,
      0
    ],
    [
      7,
      12,
      6,
      17,
      5.0990195135927845,
      2,
      0
    ],
    [
      8,
      12,
      6,
      17,
      5.385164807134504,
      2,
      0
    ],
    [
      8,
      13,
      6,
      17,
      4.47213595499958,
      2,
      3
    ],
    [
      8,
      14,
      6,
      17,
      3.605551275463989,
      2,
      3
    ],
    [
      8,
      15,
      6,
      17,
      2.8284271247461903,
      2,
      3
    ],
    [
      8,
      16,
      6,
      17,
      2.23606797749979,
      2,
      3
    ],
    [
      8,
      17,
      6,
      17,
      2,
      2,
      3
    ],
    [
      7,
      17,
      6,
      17,
      1,
      2,
      1
    ],
    [
      6,
      17,
      4,
      7,
      10.198039027185569,
      3,
      1
    ],
    [
      5,
      17,
      4,
      7,
      10.04987562112089,
      3,
      1
    ],
    [
      4,
      17,
      4,
      7,
      10,
      3,
      1
    ],
    [
      3,
      17,
      4,
      7,
      10.04987562112089,
      3,
      1
    ],
    [
      3,
      16,
      4,
      7,
      9.055385138137417,
      3,
      2
    ],
    [
      3,
      15,
      4,
      7,
      8.06225774829855,
      3,
      2
    ],
    [
      3,
      14,
      4,
      7,
      7.0710678118654755,
      3,
      2
    ],
    [
      3,
      13,
      4,
      7,
      6.082762530298219,
      3,
      2
    ],
    [
      3,
      12,
      4,
      7,
      5.0990195135927845,
      3,
      2
    ],
    [
      3,
      11,
      4,
      7,
      4.123105625617661,
      3,
      2
    ],
    [
      3,
      10,
      4,
      7,
      3.1622776601683795,
      3,
      2
    ],
    [
      3,
      9,
      4,
      7,
      2.23606797749979,
      3,
      2
    ],
    [
      3,
      8,
      4,
      7,
      1.4142135623730951,
      3,
      2
    ],
    [
      3,
      7,
      4,
      7,
      1,
      3,
      2
    ],
    [
      4,
      7,
      2,
      9,
      2.8284271247461903,
      4,
      0
    ],
    [
      5,
      7,
      2,
      9,
      3.605551275463989,
      4,
      0
    ],
    [
      6,
      7,
      2,
      9,
      4.47213595499958,
      4,
      0
    ],
    [
      7,
      7,
      2,
      9,
      5.385164807134504,
      4,
      0
    ],
    [
      8,
      7,
      2,
      9,
      6.324555320336759,
      4,
      0
    ],
    [
      9,
      7,
      2,
      9,
      7.280109889280518,
      4,
      0
    ],
    [
      9,
      8,
      2,
      9,
      7.0710678118654755,
      4,
      3
    ],
    [
      9,
      9,
      2,
      9,
      7,
      4,
      3
    ],
    [
      8,
      9,
      2,
      9,
      6,
      4,
      1
    ],
    [
      7,
      9,
      2,
      9,
      5,
      4,
      1
    ],
    [
      6,
      9,
      2,
      9,
      4,
      4,
      1
    ],
    [
      5,
      9,
      2,
      9,
      3,
      4,
      1
    ],
    [
      4,
      9,
      2,
      9,
      2,
      4,
      1
    ],
    [
      3,
      9,
      2,
      9,
      1,
      4,
      1
    ],
    [
      2,
      9,
      15,
      15,
      14.317821063276353,
      5,
      1
    ],
    [
      2,
      8,
      15,
      15,
      14.7648230602334,
      5,
      2
    ],
    [
      2,
      7,
      15,
      15,
      15.264337522473747,
      5,
      2
    ],
    [
      2,
      6,
      15,
      15,
      15.811388300841896,
      5,
      2
    ],
    [
      2,
      5,
      15,
      15,
      16.401219466856727,
      5,
      2
    ],
    [
      3,
      5,
      15,
      15,
      15.620499351813308,
      5,
      0
    ],
    [
      4,
      5,
      15,
      15,
      14.866068747318506,
      5,
      0
    ],
    [
      5,
      5,
      15,
      15,
      14.142135623730951,
      5,
      0
    ],
    [
      6,
      5,
      15,
      15,
      13.45362404707371,
      5,
      0
    ],
    [
      7,
      5,
      15,
      15,
      12.806248474865697,
      5,
      0
    ],
    [
      8,
      5,
      15,
      15,
      12.206555615733702,
      5,
      0
    ],
    [
      9,
      5,
      15,
      15,
      11.661903789690601,
      5,
      0
    ],
    [
      10,
      5,
      15,
      15,
      11.180339887498949,
      5,
      0
    ],
    [
      11,
      5,
      15,
      15,
      10.770329614269007,
      5,
      0
    ],
    [
      12,
      5,
      15,
      15,
      10.44030650891055,
      5,
      0
    ],
    [
      13,
      5,
      15,
      15,
      10.198039027185569,
      5,
      0
    ],
    [
      14,
      5,
      15,
      15,
      10.04987562112089,
      5,
      0
    ],
    [
      15,
      5,
      15,
      15,
      10,
      5,
      0
    ],
    [
      16,
      5,
      15,
      15,
      10.04987562112089,
      5,
      0
    ],
    [
      16,
      6,
      15,
      15,
      9.055385138137417,
      5,
      3
    ],
    [
      16,
      7,
      15,
      15,
      8.06225774829855,
      5,
      3
    ],
    [
      16,
      8,
      15,
      15,
      7.0710678118654755,
      5,
      3
    ],
    [
      16,
      9,
      15,
      15,
      6.082762530298219,
      5,
      3
    ],
    [
      16,
      10,
      15,
      15,
      5.0990195135927845,
      5,
      3
    ],
    [
      16,
      11,
      15,
      15,
      4.123105625617661,
      5,
      3
    ],
    [
      16,
      12,
      15,
      15,
      3.1622776601683795,
      5,
      3
    ],
    [
      16,
      13,
      15,
      15,
      2.23606797749979,
      5,
      3
    ],
    [
      16,
      14,
      15,
      15,
      1.4142135623730951,
      5,
      3
    ],
    [
      16,
      15,
      15,
      15,
      1,
      5,
      3
    ],
    [
      15,
      15,
      7,
      11,
      8.94427190999916,
      6,
      1
    ],
    [
      14,
      15,
      7,
      11,
      8.06225774829855,
      6,
      1
    ],
    [
      13,
      15,
      7,
      11,
      7.211102550927978,
      6,
      1
    ],
    [
      12,
      15,
      7,
      11,
      6.4031242374328485,
      6,
      1
    ],
    [
      11,
      15,
      7,
      11,
      5.656854249492381,
      6,
      1
    ],
    [
      10,
      15,
      7,
      11,
      5,
      6,
      1
    ],
    [
      9,
      15,
      7,
      11,
      4.47213595499958,
      6,
      1
    ],
    [
      8,
      15,
      7,
      11,
      4.123105625617661,
      6,
      1
    ],
    [
      7,
      15,
      7,
      11,
      4,
      6,
      1
    ],
    [
      7,
      14,
      7,
      11,
      3,
      6,
      2
    ],
    [
      7,
      13,
      7,
      11,
      2,
      6,
      2
    ],
    [
      7,
      12,
      7,
      11,
      1,
      6,
      2
    ],
    [
      7,
      11,
      1,
      12,
      6.082762530298219,
      7,
      2
    ],
    [
      7,
      10,
      1,
      12,
      6.324555320336759,
      7,
      2
    ],
    [
      7,
      9,
      1,
      12,
      6.708203932499369,
      7,
      2
    ],
    [
      7,
      8,
      1,
      12,
      7.211102550927978,
      7,
      2
    ],
    [
      7,
      7,
      1,
      12,
      7.810249675906654,
      7,
      2
    ],
    [
      6,
      7,
      1,
      12,
      7.0710678118654755,
      7,
      1
    ],
    [
      5,
      7,
      1,
      12,
      6.4031242374328485,
      7,
      1
    ],
    [
      4,
      7,
      1,
      12,
      5.830951894845301,
      7,
      1
    ],
    [
      3,
      7,
      1,
      12,
      5.385164807134504,
      7,
      1
    ],
    [
      2,
      7,
      1,
      12,
      5.0990195135927845,
      7,
      1
    ],
    [
      1,
      7,
      1,
      12,
      5,
      7,
      1
    ],
    [
      1,
      8,
      1,
      12,
      4,
      7,
      3
    ],
    [
      1,
      9,
      1,
      12,
      3,
      7,
      3
    ],
    [
      1,
      10,
      1,
      12,
      2,
      7,
      3
    ],
    [
      1,
      11,
      1,
      12,
      1,
      7,
      3
    ],
    [
      1,
      12,
      7,
      9,
      6.708203932499369,
      8,
      3
    ],
    [
      1,
      13,
      7,
      9,
      7.211102550927978,
      8,
      3
    ],
    [
      1,
      14,
      7,
      9,
      7.810249675906654,
      8,
      3
    ],
    [
      2,
      14,
      7,
      9,
      7.0710678118654755,
      8,
      0
    ],
    [
      3,
      14,
      7,
      9,
      6.4031242374328485,
      8,
      0
    ],
    [
      4,
      14,
      7,
      9,
      5.830951894845301,
      8,
      0
    ],
    [
      5,
      14,
      7,
      9,
      5.385164807134504,
      8,
      0
    ],
    [
      6,
      14,
      7,
      9,
      5.0990195135927845,
      8,
      0
    ],
    [
      7,
      14,
      7,
      9,
      5,
      8,
      0
    ],
    [
      7,
      13,
      7,
      9,
      4,
      8,
      2
    ],
    [
      7,
      12,
      7,
      9,
      3,
      8,
      2
    ],
    [
      7,
      11,
      7,
      9,
      2,
      8,
      2
    ],
    [
      7,
      10,
      7,
      9,
      1,
      8,
      2
    ],
    [
      7,
      9,
      16,
      18,
      12.727922061357855,
      9,
      2
    ],
    [
      7,
      8,
      16,
      18,
      13.45362404707371,
      9,
      2
    ],
    [
      7,
      7,
      16,
      18,
      14.212670403551895,
      9,
      2
    ],
    [
      7,
      6,
      16,
      18,
      15,
      9,
      2
    ],
    [
      8,
      6,
      16,
      18,
      14.422205101855956,
      9,
      0
    ],
    [
      9,
      6,
      16,
      18,
      13.892443989449804,
      9,
      0
    ],
    [
      10,
      6,
      16,
      18,
      13.416407864998739,
      9,
      0
    ],
    [
      11,
      6,
      16,
      18,
      13,
      9,
      0
    ],
    [
      12,
      6,
      16,
      18,
      12.649110640673518,
      9,
      0
    ],
    [
      13,
      6,
      16,
      18,
      12.36931687685298,
      9,
      0
    ],
    [
      14,
      6,
      16,
      18,
      12.165525060596439,
      9,
      0
    ],
    [
      15,
      6,
      16,
      18,
      12.041594578792296,
      9,
      0
    ],
    [
      16,
      6,
      16,
      18,
      12,
      9,
      0
    ],
    [
      17,
      6,
      16,
      18,
      12.041594578792296,
      9,
      0
    ],
    [
      17,
      7,
      16,
      18,
      11.045361017187261,
      9,
      3
    ],
    [
      17,
      8,
      16,
      18,
      10.04987562112089,
      9,
      3
    ],
    [
      17,
      9,
      16,
      18,
      9.055385138137417,
      9,
      3
    ],
    [
      17,
      10,
      16,
      18,
      8.06225774829855,
      9,
      3
    ],
    [
      17,
      11,
      16,
      18,
      7.0710678118654755,
      9,
      3
    ],
    [
      17,
      12,
      16,
      18,
      6.082762530298219,
      9,
      3
    ],
    [
      17,
      13,
      16,
      18,
      5.0990195135927845,
      9,
      3
    ],
    [
      17,
      14,
      16,
      18,
      4.123105625617661,
      9,
      3
    ],
    [
      17,
      15,
      16,
      18,
      3.1622776601683795,
      9,
      3
    ],
    [
      17,
      16,
      16,
      18,
      2.23606797749979,
      9,
      3
    ],
    [
      17,
      17,
      16,
      18,
      1.4142135623730951,
      9,
      3
    ],
    [
      17,
      18,
      16,
      18,
      1,
      9,
      3
    ],
    [
      16,
      18,
      19,
      10,
      8.54400374531753,
      10,
      1
    ],
    [
      15,
      18,
      19,
      10,
      8.94427190999916,
      10,
      1
    ],
    [
      14,
      18,
      19,
      10,
      9.433981132056603,
      10,
      1
    ],
    [
      13,
      18,
      19,
      10,
      10,
      10,
      1
    ],
    [
      13,
      17,
      19,
      10,
      9.219544457292887,
      10,
      2
    ],
    [
      13,
      16,
      19,
      10,
      8.48528137423857,
      10,
      2
    ],
    [
      13,
      15,
      19,
      10,
      7.810249675906654,
      10,
      2
    ],
    [
      13,
      14,
      19,
      10,
      7.211102550927978,
      10,
      2
    ],
    [
      13,
      13,
      19,
      10,
      6.708203932499369,
      10,
      2
    ],
    [
      14,
      13,
      19,
      10,
      5.830951894845301,
      10,
      0
    ],
    [
      15,
      13,
      19,
      10,
      5,
      10,
      0
    ],
    [
      16,
      13,
      19,
      10,
      4.242640687119285,
      10,
      0
    ],
    [
      17,
      13,
      19,
      10,
      3.605551275463989,
      10,
      0
    ],
    [
      18,
      13,
      19,
      10,
      3.1622776601683795,
      10,
      0
    ],
    [
      18,
      12,
      19,
      10,
      2.23606797749979,
      10,
      2
    ],
    [
      18,
      11,
      19,
      10,
      1.4142135623730951,
      10,
      2
    ],
    [
      18,
      10,
      19,
      10,
      1,
      10,
      2
    ],
    [
      18,
      9,
      19,
      10,
      1.4142135623730951,
      10,
      2
    ],
    [
      18,
      8,
      19,
      10,
      2.23606797749979,
      10,
      2
    ],
    [
      18,
      7,
      19,
      10,
      3.1622776601683795,
      10,
      2
    ],
    [
      17,
      7,
      19,
      10,
      3.605551275463989,
      10,
      1
    ],
    [
      16,
      7,
      19,
      10,
      4.242640687119285,
      10,
      1
    ],
    [
      15,
      7,
      19,
      10,
      5,
      10,
      1
    ],
    [
      15,
      6,
      19,
      10,
      5.656854249492381,
      10,
      2
    ],
    [
      15,
      5,
      19,
      10,
      6.4031242374328485,
      10,
      2
    ],
    [
      15,
      4,
      19,
      10,
      7.211102550927978,
      10,
      2
    ],
    [
      15,
      3,
      19,
      10,
      8.06225774829855,
      10,
      2
    ],
    [
      16,
      3,
      19,
      10,
      7.615773105863909,
      10,
      0
    ],
    [
      17,
      3,
      19,
      10,
      7.280109889280518,
      10,
      0
    ],
    [
      18,
      3,
      19,
      10,
      7.0710678118654755,
      10,
      0
    ],
    [
      19,
      3,
      19,
      10,
      7,
      10,
      0
    ],
    [
      19,
      4,
      19,
      10,
      6,
      10,
      3
    ],
    [
      19,
      5,
      19,
      10,
      5,
      10,
      3
    ],
    [
      19,
      6,
      19,
      10,
      4,
      10,
      3
    ],
    [
      19,
      7,
      19,
      10,
      3,
      10,
      3
    ],
    [
      19,
      8,
      19,
      10,
      2,
      10,
      3
    ],
    [
      19,
      9,
      19,
      10,
      1,
      10,
      3
    ],
    [
      19,
      10,
      17,
      6,
      4.47213595499958,
      11,
      3
    ],
    [
      19,
      11,
      17,
      6,
      5.385164807134504,
      11,
      3
    ],
    [
      19,
      12,
      17,
      6,
      6.324555320336759,
      11,
      3
    ],
    [
      19,
      13,
      17,
      6,
      7.280109889280518,
      11,
      3
    ],
    [
      18,
      13,
      17,
      6,
      7.0710678118654755,
      11,
      1
    ],
    [
      17,
      13,
      17,
      6,
      7,
      11,
      1
    ],
    [
      16,
      13,
      17,
      6,
      7.0710678118654755,
      11,
      1
    ],
    [
      16,
      12,
      17,
      6,
      6.082762530298219,
      11,
      2
    ],
    [
      16,
      11,
      17,
      6,
      5.0990195135927845,
      11,
      2
    ],
    [
      16,
      10,
      17,
      6,
      4.123105625617661,
      11,
      2
    ],
    [
      16,
      9,
      17,
      6,
      3.1622776601683795,
      11,
      2
    ],
    [
      16,
      8,
      17,
      6,
      2.23606797749979,
      11,
      2
    ],
    [
      16,
      7,
      17,
      6,
      1.4142135623730951,
      11,
      2
    ],
    [
      16,
      6,
      17,
      6,
      1,
      11,
      2
    ],
    [
      17,
      6,
      3,
      12,
      15.231546211727817,
      12,
      0
    ],
    [
      18,
      6,
      3,
      12,
      16.15549442140351,
      12,
      0
    ],
    [
      19,
      6,
      3,
      12,
      17.08800749063506,
      12,
      0
    ],
    [
      19,
      7,
      3,
      12,
      16.76305461424021,
      12,
      3
    ],
    [
      19,
      8,
      3,
      12,
      16.492422502470642,
      12,
      3
    ],
    [
      19,
      9,
      3,
      12,
      16.278820596099706,
      12,
      3
    ],
    [
      19,
      10,
      3,
      12,
      16.1245154965971,
      12,
      3
    ],
    [
      19,
      11,
      3,
      12,
      16.0312195418814,
      12,
      3
    ],
    [
      19,
      12,
      3,
      12,
      16,
      12,
      3
    ],
    [
      18,
      12,
      3,
      12,
      15,
      12,
      1
    ],
    [
      17,
      12,
      3,
      12,
      14,
      12,
      1
    ],
    [
      16,
      12,
      3,
      12,
      13,
      12,
      1
    ],
    [
      15,
      12,
      3,
      12,
      12,
      12,
      1
    ],
    [
      14,
      12,
      3,
      12,
      11,
      12,
      1
    ],
    [
      13,
      12,
      3,
      12,
      10,
      12,
      1
    ],
    [
      12,
      12,
      3,
      12,
      9,
      12,
      1
    ],
    [
      11,
      12,
      3,
      12,
      8,
      12,
      1
    ],
    [
      10,
      12,
      3,
      12,
      7,
      12,
      1
    ],
    [
      9,
      12,
      3,
      12,
      6,
      12,
      1
    ],
    [
      8,
      12,
      3,
      12,
      5,
      12,
      1
    ],
    [
      7,
      12,
      3,
      12,
      4,
      12,
      1
    ],
    [
      6,
      12,
      3,
      12,
      3,
      12,
      1
    ],
    [
      5,
      12,
      3,
      12,
      2,
      12,
      1
    ],
    [
      4,
      12,
      3,
      12,
      1,
      12,
      1
    ],
    [
      3,
      12,
      9,
      15,
      6.708203932499369,
      13,
      1
    ],
    [
      2,
      12,
      9,
      15,
      7.615773105863909,
      13,
      1
    ],
    [
      2,
      11,
      9,
      15,
      8.06225774829855,
      13,
      2
    ],
    [
      2,
      10,
      9,
      15,
      8.602325267042627,
      13,
      2
    ],
    [
      2,
      9,
      9,
      15,
      9.219544457292887,
      13,
      2
    ],
    [
      2,
      8,
      9,
      15,
      9.899494936611665,
      13,
      2
    ],
    [
      3,
      8,
      9,
      15,
      9.219544457292887,
      13,
      0
    ],
    [
      4,
      8,
      9,
      15,
      8.602325267042627,
      13,
      0
    ],
    [
      5,
      8,
      9,
      15,
      8.06225774829855,
      13,
      0
    ],
    [
      6,
      8,
      9,
      15,
      7.615773105863909,
      13,
      0
    ],
    [
      7,
      8,
      9,
      15,
      7.280109889280518,
      13,
      0
    ],
    [
      8,
      8,
      9,
      15,
      7.0710678118654755,
      13,
      0
    ],
    [
      9,
      8,
      9,
      15,
      7,
      13,
      0
    ],
    [
      9,
      9,
      9,
      15,
      6,
      13,
      3
    ],
    [
      9,
      10,
      9,
      15,
      5,
      13,
      3
    ],
    [
      9,
      11,
      9,
      15,
      4,
      13,
      3
    ],
    [
      9,
      12,
      9,
      15,
      3,
      13,
      3
    ],
    [
      9,
      13,
      9,
      15,
      2,
      13,
      3
    ],
    [
      9,
      14,
      9,
      15,
      1,
      13,
      3
    ],
    [
      9,
      15,
      17,
      11,
      8.94427190999916,
      14,
      3
    ],
    [
      8,
      15,
      17,
      11,
      9.848857801796104,
      14,
      1
    ],
    [
      7,
      15,
      17,
      11,
      10.770329614269007,
      14,
      1
    ],
    [
      6,
      15,
      17,
      11,
      11.704699910719626,
      14,
      1
    ],
    [
      5,
      15,
      17,
      11,
      12.649110640673518,
      14,
      1
    ],
    [
      4,
      15,
      17,
      11,
      13.601470508735444,
      14,
      1
    ],
    [
      4,
      14,
      17,
      11,
      13.341664064126334,
      14,
      2
    ],
    [
      4,
      13,
      17,
      11,
      13.152946437965905,
      14,
      2
    ],
    [
      4,
      12,
      17,
      11,
      13.038404810405298,
      14,
      2
    ],
    [
      4,
      11,
      17,
      11,
      13,
      14,
      2
    ],
    [
      4,
      10,
      17,
      11,
      13.038404810405298,
      14,
      2
    ],
    [
      5,
      10,
      17,
      11,
      12.041594578792296,
      14,
      0
    ],
    [
      6,
      10,
      17,
      11,
      11.045361017187261,
      14,
      0
    ],
    [
      7,
      10,
      17,
      11,
      10.04987562112089,
      14,
      0
    ],
    [
      8,
      10,
      17,
      11,
      9.055385138137417,
      14,
      0
    ],
    [
      9,
      10,
      17,
      11,
      8.06225774829855,
      14,
      0
    ],
    [
      10,
      10,
      17,
      11,
      7.0710678118654755,
      14,
      0
    ],
    [
      11,
      10,
      17,
      11,
      6.082762530298219,
      14,
      0
    ],
    [
      12,
      10,
      17,
      11,
      5.0990195135927845,
      14,
      0
    ],
    [
      13,
      10,
      17,
      11,
      4.123105625617661,
      14,
      0
    ],
    [
      14,
      10,
      17,
      11,
      3.1622776601683795,
      14,
      0
    ],
    [
      15,
      10,
      17,
      11,
      2.23606797749979,
      14,
      0
    ],
    [
      16,
      10,
      17,
      11,
      1.4142135623730951,
      14,
      0
    ],
    [
      17,
      10,
      17,
      11,
      1,
      14,
      0
    ],
    [
      17,
      11,
      19,
      6,
      5.385164807134504,
      15,
      3
    ],
    [
      17,
      12,
      19,
      6,
      6.324555320336759,
      15,
      3
    ],
    [
      17,
      13,
      19,
      6,
      7.280109889280518,
      15,
      3
    ],
    [
      17,
      14,
      19,
      6,
      8.246211251235321,
      15,
      3
    ],
    [
      17,
      15,
      19,
      6,
      9.219544457292887,
      15,
      3
    ],
    [
      16,
      15,
      19,
      6,
      9.486832980505138,
      15,
      1
    ],
    [
      15,
      15,
      19,
      6,
      9.848857801796104,
      15,
      1
    ],
    [
      14,
      15,
      19,
      6,
      10.295630140987,
      15,
      1
    ],
    [
      13,
      15,
      19,
      6,
      10.816653826391969,
      15,
      1
    ],
    [
      12,
      15,
      19,
      6,
      11.40175425099138,
      15,
      1
    ],
    [
      11,
      15,
      19,
      6,
      12.041594578792296,
      15,
      1
    ],
    [
      11,
      14,
      19,
      6,
      11.313708498984761,
      15,
      2
    ],
    [
      11,
      13,
      19,
      6,
      10.63014581273465,
      15,
      2
    ],
    [
      11,
      12,
      19,
      6,
      10,
      15,
      2
    ],
    [
      11,
      11,
      19,
      6,
      9.433981132056603,
      15,
      2
    ],
    [
      11,
      10,
      19,
      6,
      8.94427190999916,
      15,
      2
    ],
    [
      11,
      9,
      19,
      6,
      8.54400374531753,
      15,
      2
    ],
    [
      11,
      8,
      19,
      6,
      8.246211251235321,
      15,
      2
    ],
    [
      11,
      7,
      19,
      6,
      8.06225774829855,
      15,
      2
    ],
    [
      12,
      7,
      19,
      6,
      7.0710678118654755,
      15,
      0
    ],
    [
      13,
      7,
      19,
      6,
      6.082762530298219,
      15,
      0
    ],
    [
      14,
      7,
      19,
      6,
      5.0990195135927845,
      15,
      0
    ],
    [
      15,
      7,
      19,
      6,
      4.123105625617661,
      15,
      0
    ],
    [
      16,
      7,
      19,
      6,
      3.1622776601683795,
      15,
      0
    ],
    [
      17,
      7,
      19,
      6,
      2.23606797749979,
      15,
      0
    ],
    [
      18,
      7,
      19,
      6,
      1.4142135623730951,
      15,
      0
    ],
    [
      19,
      7,
      19,
      6,
      1,
      15,
      0
    ],
    [
      19,
      6,
      13,
      6,
      6,
      16,
      2
    ],
    [
      19,
      5,
      13,
      6,
      6.082762530298219,
      16,
      2
    ],
    [
      19,
      4,
      13,
      6,
      6.324555320336759,
      16,
      2
    ],
    [
      19,
      3,
      13,
      6,
      6.708203932499369,
      16,
      2
    ],
    [
      19,
      2,
      13,
      6,
      7.211102550927978,
      16,
      2
    ],
    [
      19,
      1,
      13,
      6,
      7.810249675906654,
      16,
      2
    ],
    [
      19,
      0,
      13,
      6,
      8.48528137423857,
      16,
      2
    ]
]

df_pred = pd.DataFrame(prediction, columns=['direction'])
df_data = pd.DataFrame(data_to_eval, columns=['a','b','c','d','e','f','direction'])
dictio = {0:'right', 1:'left', 2:'up', 3:'down'}
df_data['direction'] = df_data['direction'].map(dictio)

#print(type(df_pred))
#print(type(df_data))
#print(df_data.head())
#print(df_pred.head())
df = pd.DataFrame()
df['eval'] = df_data['direction'] == df_pred['direction']
print(df['eval'].value_counts())
