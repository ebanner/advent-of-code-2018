boxes←⊃⎕NGET'input'1
n←⍴boxes
sim←boxes∘.{+/⍺≠⍵}boxes
min←I←(⍳n)∘.=⍳n ⋄ ⌊/⌊/(I×n)+sim
correct←↑boxes[⊃⍸min=sim]
⎕←(=⌿correct)/correct[1;]
