from logic import *


AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

ASaysAKnight = Symbol("A says he's a Knight")
ASaysAKnave = Symbol("A says he's a Knave")
ASaysBKnight = Symbol("A says B's a Knight")
ASaysBKnave = Symbol("A says B's a Knave")
BSaysAKnight = Symbol("B says A's a Knight")
BSaysAKnave = Symbol("B says A's a Knave")
BSaysBKnight = Symbol("B says he's a Knight")
BSaysBKnave = Symbol("B says he's a Knave")
BSaysCKnave = Symbol("B says C's a Knave")
CSaysAKnight = Symbol("C says A's a Knight")


base_knowledge = [
    Biconditional(AKnight, Not(AKnave)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(CKnight, Not(CKnave)),
]

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(And(ASaysAKnight, ASaysAKnave), AKnave),
    ASaysAKnight,
    ASaysAKnave,
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    *base_knowledge,
    Implication(And(ASaysAKnave, ASaysBKnave), AKnave),
    Implication(And(ASaysBKnave, AKnave), BKnight),
    Or(AKnight, AKnave),
    ASaysAKnave,
    ASaysBKnave,
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    *base_knowledge,
    Implication(Or(And(AKnight, BKnight), And(AKnave, BKnave)), And(AKnight, BKnave)),
    Implication(Or(And(AKnave, BKnight), And(AKnight, BKnave)), And(BKnight, AKnave)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    *base_knowledge,
    Biconditional(And(BSaysCKnave, BKnight), CKnave),
    Biconditional(And(CSaysAKnight, CKnight), AKnight),
    # "I am a knave." is an impossible sentence, therefore A can only say "I am a knight."
    # and B must be a knave
    BKnave,
    BSaysCKnave,
    CSaysAKnight,
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
