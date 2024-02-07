(
    defun readstr(var)(
        (let tmpchr (1))
        (let tmpcnd (0))
        (let startaddr (0))
        (save startaddr (var))
        (while (= tmpcnd 0) do (
            (read tmpchr (735))
            (if (= tmpchr 0) 
               ( save tmpcnd (0))
            )
            (save tmpchr (var))
            (add (+ 1 var))
        ))
        (save var (startaddr))
        (ret startaddr)
    )
)