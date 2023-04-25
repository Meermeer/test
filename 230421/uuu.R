library(dplyr)
library(ggplot2)

# 극단치
view(mpg)

# 극단치를 확인
boxxplot(mpg$cty)
# 극단치를 수치로 표현
boxplot(mpg$cty)$stats


mpg = ggplot2::mpg

# 이상치는 26초과이거나 9미만인 경우
# 이상치를 결측치로 변환
# 결측치의 개수를 확인
ifelse(mpg$cty > 26 | mpg$cty < 9, NA, mpg$cty)
table(is.na(mpg$cty))

# d