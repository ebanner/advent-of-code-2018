boxes ← ⊃ ⎕NGET 'input' 1

n ← ⍴ boxes
I ← (⍳n) ∘.= ⍳n
min ← ⌊/ ⌊/ (I×n) + boxes ∘.{+/ ~ ⍺ = ⍵} boxes
correct ← ↑ boxes[⊃ ⍸ min = boxes ∘.{+/ ⍺ ≠ ⍵} boxes]
⎕ ← (=⌿ correct) / correct[1;]
