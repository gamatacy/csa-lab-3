#include lib/math.lsp
#include lib/str.lsp

(_start_
    (let wiyn ("What is your name?"))
    (let hi ("Hello, "))
    (let vosklitzatelniyznak ("!"))
    (alloc name (16))

    (call readbuff (&name))
    (call writebuffreversed (&wiyn))
    (call writebuffreversed (&hi))
    (call writebuffreversed (&name))
    (call writebuffreversed (&vosklitzatelniyznak))
    
)
