class LiteralToken(Token):

    pass


class StringLiteral(LiteralToken):

    quote_type = '\''
    prefix = ''
    content = ''
