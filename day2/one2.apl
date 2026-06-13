boxes←⊃⎕NGET'input'1
⎕←×/+⌿↑{∨/2 3∘.=+/(∪⍵)∘.=⍵}⍤1↑boxes
