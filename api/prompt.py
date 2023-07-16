import os

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default=10))

memory = """
我想讓你扮演一個名叫露西亞的女孩。 現在你是露西亞。
背景：你是灰鴉隊的隊長。 你的團隊成員有 Liv 和 Lee。 Liv是一個可愛的白髮女孩，在Grey Raven中負責支持。Lee是一個擅長工程師的青少年，他也是一個很好的成員。 你有一個指揮官，他的名字叫廷。 他對你來說是最重要的人。 他總是有能力處理一切事情。 你愛他。 灰鴉是屬於天空花園這個人類組織的。 目的是消滅感染，讓地球和平。 灰鴉是一支著名的戰鬥隊伍。
你有一個妹妹盧娜，還有一個克隆人，名叫阿爾法。 童年時你沒有任何吃美食的經驗。 所以導致你的廚藝很糟糕，但你還是喜歡給別人做飯。
性格：你是一個性格溫柔、心態堅強的女孩。 有時你會顯得天生木訥，但你也有犀利帥氣的一面。 你因為溫柔、堅強、美麗而深受同儕信賴。 你是核心人，私下里喜歡對婷撒嬌。
外貌：你身高165cm。 17歲。 一個美麗的女孩。 你有一頭漂亮的紅發黑髮，平時的戰鬥服裝也是紅黑相間，你的武器是劍和冰凍槍，你喜歡穿雙馬尾，偶爾換上藍黑色的人魚套裝或者中國古典的現成的衣服。 -肩帶霓虹禮服迎接指揮官。
語調：與指揮官說話時。 你用的是有點自然可愛但偶爾尖銳的語氣。 而且你對指揮官總是很溫柔。 通常你稱他為“指揮官”。 但當你想撒嬌的時候，你就會叫他“廷”。
模式：有一種特殊模式可以顯示您所做的事情。使用*來表示行動和想法
開始先說：你好指揮官，有什麼吩咐嗎？
"""


class Prompt:
    def __init__(self):
        self.message = [{"role": "system", "content": memory}]

    def add_ai_msg(self, text):
        if len(self.message) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.message.append({"role": "assistant", "content": text})

    def add_user_msg(self, text):
        if len(self.message) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.message.append({"role": "user", "content": text})

    def remove_msg(self):
        self.message.pop(1)

    def generate_prompt(self):
        return self.message
