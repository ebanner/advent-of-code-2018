lines ← ⊃⎕NGET 'guards.csv' 1

n ← ≢ lines

rows ← (n÷2) 6 ⍴ ↑ {⍎¨ 3 ↑ ⍵}¨ (≠∘','⊆⊢)¨ n ↑ lines
rows ← rows[; 1 2 5 6]

N ← ⌈/ rows[;1]

times ← N 60 ⍴ 0

result ← ⊃ +/ {
  guard start stop _ ← ⍵ ⋄
  idxs ← guard ,¨ start + ⍳ stop - start ⋄
  (+∘1) @ idxs ⊢ times
}¨ ↓ rows

G ← ⊃ ⍒ +/ result

gid ← ⊃ (rows ⌿⍨ rows[;1] = G)[;4]

gid × -∘1 ⊃ ⍒ result[G;]
