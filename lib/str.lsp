(
    (let tmpchr (0))
    (let tmpcnd (0))
    (let index (0))
)

(
    defun readbuff(readbuff1)(
        (save tmpchr (1))
        (save tmpcnd (1))
        (save index (0))
        (while (= tmpcnd 0) do (
            (read tmpchr (735))
            (save offset (tmpchr + readbuff1 index)) 
            (+ 1 index)
            (if (= tmpchr 0) 
               ( save tmpcnd (0) )
            )
        ))
        (ret readbuff1)
    )
)

(
    defun writebuff(writebuff1)(
        (save tmpchr (1))
        (save tmpcnd (1))
        (save index (0))
        
        (while (= tmpcnd 0) do (
            (load offset (tmpchr + writebuff1 index)) 
            (+ 1 index)
            (if (= tmpchr 0) 
               ( save tmpcnd (0) )
            )
        ))

        (save tmpcnd (1))

        (while (= tmpcnd 0) do (
            (load offset (tmpchr + writebuff1 index)) 
            (write tmpchr (735))
            (- index 1)
            (if (< index 0) 
               ( save tmpcnd (0) )
            )
        ))

        (ret writebuff1)
    )
)

(
    defun writebuffreversed (writebuffreversed1)(
        (save tmpchr (1))
        (save tmpcnd (1))
        (save index (0))
        
        (while (= tmpcnd 0) do (
            (load offset (tmpchr + writebuffreversed1 index)) 
            (write tmpchr (735))
            (+ 1 index)
            (if (= tmpchr 0) 
               ( save tmpcnd (0) )
            )
        ))

        (ret writebuffreversed1)
    )
)

(alloc writeintbuffer (15))

(defun savewithoffsetplease(saveval addr offset) (
    (save offset (saveval + addr offset)) 
    (ret addr)
))

(
    defun writeint (writeint1)(
        (let intchr (0))
        (let intbase (10))
        (save index (0))

        

        (while (>= writeint1 1) do (

            (save intchr (call remainder (writeint1 intbase)))

            (+ 48 intchr)
            (call savewithoffsetplease (intchr &writeintbuffer index))

            (save writeint1 (call divide (writeint1 intbase))) 

            (+ 1 index)

        ))

        (call writebuff(&writeintbuffer))
        (ret writeint1)
    )
)