lines ← ⊃ ⎕NGET 'input' 1
claims ← ⍎¨ lines

n m ← 1000 1000

get_grid ← {(j i) (w h) ← ⍵ ⋄ zeros ← n m ⍴ 0 ⋄ zeros[i + ⍳h ; j + ⍳w] ← 1 ⋄ zeros}

fabric ← ⊃ {⍵ + get_grid ⍺}/ (⌽ claims) , ⊂ (n m ⍴ 0)

⎕ ← {(j i) (w h) ← ⍵ ⋄ ∧/ ∧/ 1 = fabric[i + ⍳h ; j + ⍳w]}¨ claims
