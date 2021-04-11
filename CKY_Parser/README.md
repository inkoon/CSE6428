### Requirements
- Python 3.8.5

### Run
```python
python3 main.py
```

### Results
output.txt : parse tree
used_grammar.txt : grammar history used in order

#### Examples
- input.txt
```txt
I saw a man on the hill with the telescope
time flies like an arrow
```

- output.txt
```txt
I saw a man on the hill with the telescope
(S (NP (n I))(VP (VP (v saw))(NP (DT (det a))(NP (NP (n man))(PP (P (p on))(NP (DT (det the))(NP (NP (n hill))(PP (P (p with))(NP (DT (det the))(NP (n telescope)))))))))))
(S (NP (n I))(VP (VP (v saw))(NP (DT (det a))(NP (NP (n man))(PP (P (p on))(NP (NP (DT (det the))(NP (n hill)))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))))))
(S (NP (n I))(VP (VP (v saw))(NP (DT (det a))(NP (NP (NP (n man))(PP (P (p on))(NP (DT (det the))(NP (n hill)))))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))))
(S (NP (n I))(VP (VP (v saw))(NP (NP (DT (det a))(NP (n man)))(PP (P (p on))(NP (DT (det the))(NP (NP (n hill))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))))))
(S (NP (n I))(VP (VP (v saw))(NP (NP (DT (det a))(NP (n man)))(PP (P (p on))(NP (NP (DT (det the))(NP (n hill)))(PP (P (p with))(NP (DT (det the))(NP (n telescope)))))))))
(S (NP (n I))(VP (VP (v saw))(NP (NP (DT (det a))(NP (NP (n man))(PP (P (p on))(NP (DT (det the))(NP (n hill))))))(PP (P (p with))(NP (DT (det the))(NP (n telescope)))))))
(S (NP (n I))(VP (VP (v saw))(NP (NP (NP (DT (det a))(NP (n man)))(PP (P (p on))(NP (DT (det the))(NP (n hill)))))(PP (P (p with))(NP (DT (det the))(NP (n telescope)))))))
(S (NP (n I))(VP (VP (VP (v saw))(NP (DT (det a))(NP (n man))))(PP (P (p on))(NP (DT (det the))(NP (NP (n hill))(PP (P (p with))(NP (DT (det the))(NP (n telescope)))))))))
(S (NP (n I))(VP (VP (VP (v saw))(NP (DT (det a))(NP (n man))))(PP (P (p on))(NP (NP (DT (det the))(NP (n hill)))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))))
(S (NP (n I))(VP (VP (VP (v saw))(NP (DT (det a))(NP (NP (n man))(PP (P (p on))(NP (DT (det the))(NP (n hill)))))))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))
(S (NP (n I))(VP (VP (VP (v saw))(NP (NP (DT (det a))(NP (n man)))(PP (P (p on))(NP (DT (det the))(NP (n hill))))))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))
(S (NP (n I))(VP (VP (VP (VP (v saw))(NP (DT (det a))(NP (n man))))(PP (P (p on))(NP (DT (det the))(NP (n hill)))))(PP (P (p with))(NP (DT (det the))(NP (n telescope))))))

time flies like an arrow
(S (NP (n time))(VP (VP (v flies))(PP (P (p like))(NP (DT (det an))(NP (n arrow))))))
(S (NP (NP (n time))(VP (v flies)))(VP (VP (v like))(NP (DT (det an))(NP (n arrow)))))
```

- used_grammar.txt
```txt
I saw a man on the hill with the telescope
n -> I
NP -> n
v -> saw
n -> saw
VP -> v
NP -> n
S -> NP VP
NP -> NP VP
det -> a
DT -> det
n -> man
v -> man
NP -> n
VP -> v
NP -> DT NP
VP -> VP NP
S -> NP VP
NP -> NP VP
p -> on
P -> p
det -> the
DT -> det
n -> hill
NP -> n
NP -> DT NP
PP -> P NP
NP -> NP PP
VP -> VP PP
NP -> DT NP
NP -> NP PP
VP -> VP NP
VP -> VP NP
VP -> VP PP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
NP -> NP PP
p -> with
P -> p
det -> the
DT -> det
n -> telescope
NP -> n
NP -> DT NP
PP -> P NP
NP -> NP PP
NP -> DT NP
NP -> NP PP
PP -> P NP
PP -> P NP
NP -> NP PP
NP -> NP PP
VP -> VP PP
VP -> VP PP
NP -> NP PP
VP -> VP PP
NP -> DT NP
NP -> DT NP
NP -> DT NP
NP -> NP PP
NP -> NP PP
NP -> NP PP
NP -> NP PP
VP -> VP NP
VP -> VP NP
VP -> VP NP
VP -> VP NP
VP -> VP NP
VP -> VP NP
VP -> VP NP
VP -> VP PP
VP -> VP PP
VP -> VP PP
VP -> VP PP
VP -> VP PP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
S -> NP VP
NP -> NP VP
NP -> NP PP
NP -> NP PP
NP -> NP PP
NP -> NP PP
NP -> NP PP
NP -> NP PP

time flies like an arrow
n -> time
v -> time
NP -> n
VP -> v
n -> flies
v -> flies
NP -> n
VP -> v
S -> NP VP
NP -> NP VP
VP -> VP NP
p -> like
v -> like
P -> p
VP -> v
S -> NP VP
NP -> NP VP
VP -> VP NP
S -> NP VP
NP -> NP VP
det -> an
DT -> det
n -> arrow
NP -> n
NP -> DT NP
PP -> P NP
VP -> VP NP
NP -> NP PP
S -> NP VP
NP -> NP VP
VP -> VP PP
S -> NP VP
NP -> NP VP
VP -> VP NP
VP -> VP NP
NP -> NP PP
S -> NP VP
NP -> NP VP
VP -> VP PP
VP -> VP NP
```
