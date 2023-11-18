class Codec:
    def encode(self, strs: list[str]) -> str:
        return "\x00".join(strs)



    def decode(self, s: str) -> list[str]:
        return s.split("\x00")



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
