import random
class MarkovChain:
    def __init__(self): self.chain = {}
    def train(self, words: list[str]):
        for i in range(len(words)-1):
            self.chain.setdefault(words[i], []).append(words[i+1])
    def generate(self, start: str, length=20) -> str:
        cur, out = start, [start]
        for _ in range(length):
            nxt = random.choice(self.chain.get(cur, ['']))
            if not nxt: break
            out.append(nxt); cur = nxt
        return ' '.join(out)
