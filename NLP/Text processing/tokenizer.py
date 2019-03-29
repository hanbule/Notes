# 1
  def tokenize_1(text):
    tokens = re.split("(?<! т.е)(?<!\\.)\\. +(?!\\.)(?!com)|(?<![0-9]), *(?![0-9])| +", text)
    return tokens
