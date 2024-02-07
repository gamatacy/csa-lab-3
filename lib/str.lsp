(
    defun readstr(var)(
        (let tmpchr (1))
        (let tmpcnd (0))
        (let startaddr (0))
        (setaddr (startaddr var))
        (while (= tmpcnd 0) do (
            (read tmpchr (735))
            (save tmpchr (startaddr)) 
            (incaddr startaddr)
            (if (= tmpchr 0) 
               ( save tmpcnd (0))
            )
        ))
        (ret var)
    )
)