#include lib/math.lsp
#include lib/str.lsp

(_start_
    (alloc string (64))
    (call readbuff (&string))
    (call writebuffreversed (&string))
)
