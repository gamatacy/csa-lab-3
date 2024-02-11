#include lib/str.lsp

(_start_
    (let string ("hello world!"))
    (call writebuffreversed (&string))
)
