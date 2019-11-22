class LiteralToken(Token):

    pass


class StringLiteral(LiteralToken):

    prefix = ''
    content = ''


class IntLiteral(LiteralToken):

    value = 0


class FloatLiteral(LiteralToken):

    value = 0