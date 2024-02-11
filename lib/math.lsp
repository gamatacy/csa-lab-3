(let res (0))
(let mathindex (0))
(let rorl (0))
(let mathvar1 (0))
(let mathvar2 (0))
(let mathvar3 (0))

(
    defun bits (bits1)
    (
        (save res (0))
        (while (>= bits1 1) do (
            (save bits1 ((>> bits1 1)))
            (+ 1 res)
        ))
        (ret res)
    )
)

(
    defun divide (divide1 divide2)
        (
            (save mathvar1 (0))
            (save mathvar2 (0))
            (save mathvar3 (0))

            (save mathindex (call bits (divide1)))
            (- mathindex 1)

            (while (>= mathindex 0) do (

                (save mathvar1 ((<< mathvar1 1)))
                (save mathvar2 ((<< mathvar2 1)))

                (save rorl (mathindex))
                (save mathvar3 (divide1))

                (if (>= rorl 1) (
                    (while (>= rorl 1) do (
                    (save mathvar3 ((>> mathvar3 1)) )
                    (- rorl 1)
                     ))
                ))

                (save mathvar3 ((&& mathvar3 1)))
                (+ mathvar3 mathvar1)

                (if (>= mathvar1 divide2 ) (
                    (- mathvar1 divide2)
                    (+ 1 mathvar2)
                ))

                (- mathindex 1)

            ))

            (ret mathvar2)

        )

)

(
    defun remainder (remainder1 remainder2)
        (
            (save mathvar1 (0))
            (save mathvar2 (0))
            (save mathvar3 (0))

            (save mathindex (call bits (remainder1)))
            (- mathindex 1)

            (while (>= mathindex 0) do (

                (save mathvar1 ((<< mathvar1 1)))
                (save mathvar2 ((<< mathvar2 1)))

                (save rorl (mathindex))
                (save mathvar3 (remainder1))

                (if (>= rorl 1) (
                    (while (>= rorl 1) do (
                    (save mathvar3 ((>> mathvar3 1)) )
                    (- rorl 1)
                     ))
                ))

                (save mathvar3 ((&& mathvar3 1)))
                (+ mathvar3 mathvar1)

                (if (>= mathvar1 remainder2 ) (
                    (- mathvar1 remainder2)
                    (+ 1 mathvar2)
                ))

                (- mathindex 1)

            ))

            (ret mathvar1)

        )

)

(
    defun multiply (multiply1 multiply2) (
        (save mathvar1 (0))
        (while (!= multiply2 0) do (
            (+ multiply1 mathvar1)
            (- multiply2 1)
        ))
        (ret mathvar1)
    )
)

(
    defun gcd (gcd1 gcd2)(
        (while (!= gcd2 0) do (
            (save mathvar1 (gcd1))
            (save gcd1 (gcd2))
            (save gcd2 (call remainder (mathvar1 gcd2)))
        ))
        (ret gcd1)
    )
)

(
    defun lcm (lcm1 lcm2) (
        (let mult (0))
        (let gcdres (0))
        (save res (0))

        (save mult (call multiply (lcm1 lcm2)))
        (save gcdres (call gcd(lcm1 lcm2)))
        (save res (call divide(mult gcdres)))
        
        (ret res)
    )
)

(
    defun probfive(probfive1) (
        (let idx (1))
        (let multiple (1))

        (while (>= probfive1 1) do (
            (save multiple (call lcm(multiple idx)))
            (+ 1 idx)
            (- probfive1 1)
        ))

        (ret multiple)
    )
)
