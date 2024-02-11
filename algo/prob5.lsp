#include lib/math.lsp
#include lib/str.lsp

(_start_
   (let a (20))
   (let c (0))
   (save c (call probfive(a)))
   (call writeint(c))
)
