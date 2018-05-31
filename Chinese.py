"""
Chinese Word/Sentence Bank
Stores all Chinese sentences and translations.
"""

# Bank of vocab verbs
# Bank of default verbs and sentences
chineseVerbs = [("要", "want", "我要一个苹果.", "wǒ yào yī gè píng guǒ.", \
            "I want an apple."),
        ("吃", "eat", "我在吃面.", "wǒ zài chī miàn.", "I am eating noodles."),
        ("喝", "drink", "我喝茶.", "wǒ hē chá.", "I drink tea."),
        ("拿", "take", "请拿上这本书.","qǐng ná shàng zhè běn shū.", \
            "Please take the book."),
        ("给", "give", "请给我.", "qǐng gěi wǒ.", "Please give me."),
        ("开", "open", "开门.", "kāi mén.", "Open the door."),
        ("有", "have", "我有一个弟弟.", "wǒ yǒu yī gè dì di.", \
            "I have a younger brother."),
        ("知道", "know", "我知道.", "wǒ zhī dao.", "I know."),
        ("喜欢", "like", "我喜欢她.", "wǒ xǐ huan tā.", "I like her."),
        ("爱", "love", "我爱他.", "wǒ ài tā.", "I love him."),
        ("是", "am", "我是一个老师.", "wǒ shì yī gè lǎo shī.", \
            "I am a teacher."),
        ("做", "make", "每天我都做晚饭.", "měi tiān wǒ dōu zuò wǎn fàn.", \
            "I make dinner every day."),
        ("坐", "sit", "当我去图书馆我习惯坐那里.", \
            "dāng wǒ qù tú shū guǎn wǒ xí guàn zuò nà li.", \
            "I usually sit there when I go to the library."),
        ("看", "watch", "我喜欢看电影.", "wǒ xǐ huan kàn diàn yǐng.", \
            "I like to watch movies."),
        ("去", "go", "我经常去北京.", "wǒ jīng cháng qù běi jīng.", \
            "I go to Beijing often."),
        ("用", "use", "我用手机的频率太高了.", \
            "wǒ yòng shǒu jī de pín lǜ tài gāo le.", \
            "I use my mobile phone too much."),
        ("找", "find", "我可以找到那本书.", "wǒ kě yǐ zhǎo dào nà běn shū.", \
            "I can find the book."),
        ("告诉", "tell", "告诉我他的电话号码.", \
            "gào su wǒ tā de diàn huà hào mǎ.", \
            "Tell me his phone number."),
        ("问", "ask", "请问你的朋友.", "qǐng wèn nǐ de péng you.", \
            "Please ask your friend."),
        ("觉得", "think", "我觉得很奇怪.", "wǒ jué de hěn qí guài.", \
            "I think it’s strange.")]
# IF TESTING CUSTOMIZE FEATURE, USE THE SMALLER WORD BANK BELOW
# BY COMMENTING OUT THE WORD BANK ABOVE AND UNCOMMENTING THE WORD BANK BELOW
# chineseVerbs = [("要", "want", "我要一个苹果.", "wǒ yào yī gè píng guǒ.", \
#             "I want an apple.")]

# Bank of all char
chineseChar = ['我', '要', '一', '个', '苹', '果', '我', '在', '吃', '面', '我', 
        '喝', '茶', '请', '拿', '上', '这', '本', '书', '请', '给', '我', '开', 
        '门', '我', '有', '一', '个', '弟', '弟', '我', '知', '道', '我', '喜', 
        '欢', '她', '我', '爱', '他', '我', '是', '一', '个', '老', '师', '每', 
        '天', '我', '都', '做', '晚', '饭', '当', '我', '去', '图', '书', '馆', 
        '我', '习', '惯', '坐', '那', '里', '我', '喜', '欢', '看', '电', '影', 
        '我', '经', '常', '去', '北', '京', '我', '用', '手', '机', '的', '频', 
        '率', '太', '高', '了', '我', '可', '以', '找', '到', '那', '本', '书', 
        '告', '诉', '我', '他', '的', '电', '话', '号', '码', '请', '问', '你', 
        '的', '朋', '友', '我', '觉', '得', '很', '奇', '怪']