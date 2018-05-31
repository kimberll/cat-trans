"""
Korean Word/Sentence Bank
Stores all Korean sentences and translations.
"""

# Bank of vocab verbs
koreanVerbs = [("원해", "want", "나는 애플 원해.", "naneun sagwaleul wonhae.", \
            "I want an apple."),
        ("먹다", "eat", "나는 국수를 먹고있다.", "naneun gugsuleul meoggoissda.", \
            "I am eating noodles."),
        ("마신다", "drink", "나는 차를 마신다.", "naneun chaleul masinda.", \
            "I drink tea."),
        ("가져", "take", "이 책을 가져 가세요.","i chaeg-eul gajyeo gaseyo.", \
            "Please take the book."),
        ("그걸 나에게주", "give", "그걸 나에게주세요.", "geugeol na-egejuseyo.", \
            "Please give me."),
        ("열어", "open", "문 열어.", "mun yeol-eo.", "Open the door."),
        ("이있다", "have", "나는 남동생이있다.", "naneun namdongsaeng-iissda.", \
            "I have a younger brother."),
        ("알아", "know", "알아.", "al-a.", "I know."),
        ("좋아", "like", "나는 그녀가 좋아.", "naneun geunyeoga joh-a.", "I like her."),
        ("사랑", "love", "나는 그를 사랑합니다.", "naneun geuleul salanghabnida.", "I love him."),
        ("나는", "am", "나는 선생님이다.", "naneun seonsaengnim-ida.", \
            "I am a teacher."),
        ("을한다", "make", "나는 매일 저녁을한다.", "naneun maeil jeonyeog-eulhanda.", \
            "I make dinner every day."),
        ("앉아", "sit", "나는 도서관에 갈 때 거기에 앉아있다.", \
            "naneun doseogwan-e gal ttae geogie anj-aissda.", \
            "I usually sit there when I go to the library."),
        ("감상을", "watch", "영화 감상을 좋아해.", "yeonghwa gamsang-eul joh-ahae.", \
            "I like to watch movies."),
        ("간다", "go", "나는 자주 베이징에 간다.", "naneun jaju beijing-e ganda.", \
            "I go to Beijing often."),
        ("사용한다", "use", "나는 휴대 전화를 너무 많이 사용한다.", \
            "naneun hyudae jeonhwaleul neomu manh-i sayonghanda.", \
            "I use my mobile phone too much."),
        ("찾을", "find", "나는 그 책을 찾을 수있다.", \
            "naneun geu chaeg-eul chaj-eul su-issda.", \
            "I can find the book."),
        ("말해줘", "tell", "전화 번호를 말해줘.", \
            "jeonhwa beonholeul malhaejwo.", \
            "Tell me his phone number."),
        ("물어보", "ask", "친구에게 물어보십시오.", "chinguege mul-eobosibsio.", \
            "Please ask your friend."),
        ("생각한다", "think", "나는 그것이 이상하다고 생각한다.", \
            "naneun geugeos-i isanghadago saeng-gaghanda.", \
            "I think it’s strange.")]
# IF TESTING CUSTOMIZE FEATURE, USE THE SMALLER WORD BANK BELOW
# BY COMMENTING OUT THE WORD BANK ABOVE AND UNCOMMENTING THE WORD BANK BELOW
# koreanVerbs = [("원해", "want", "나는 애플 원해.", "naneun sagwaleul wonhae.", \
#              "I want an apple.")]

# Bank of all char
koreanChar = ['나', '는', '애', '플', '원', '해', '나', '는', '국', '수', '를', '먹', '고', \
        '있', '다', '나', '는',    '차', '를', '마', '신', '다', '이', '책', '을', \
        '가', '져', '가', '세', '요', '그', '걸', '나', '에', '게', '주', '세', '요', \
        '문', '열', '어', '나', '는', '남', '동', '생', '이', '있', '다', '알', '아', \
        '나', '는', '그', '녀', '가', '좋', '아', '나', '는', '그', '를', '사', '랑', \
        '합', '니', '다', '나', '는', ' ', '선', '생', '님', '이', '다', '나', '는', \
        '매', '일', '저', '녁', '을', '한', '다', '나', '는', '도', '서', '관', '에', \
        '갈', '때', '거', '기', '에', '앉', '아', '있', '다', '영', '화', '감', '상', \
        '을', '좋', '아', '해', '나', '는', '자', '주', '베', '이', '징', '에', '간', \
        '다', '나', '는', '휴', '대', '전', '화', '를', '너', '무', '많', '이', '사', \
        '용', '한', '다', '나', '는', '그', '책', '을', '찾', '을', ' ', '수', '있', \
        '다', '전', '화', '번', '호', '를', '말', '해', '줘', '친', '구', '에', '게', \
        '물', '어', '보', '십', '시', '오', '나', '는', '그', '것', '이', '이', '상', \
        '하', '다', '고', '생', '각', '한', '다']
