## sav파일 로드
install.packages('foreign')
install.packages('readxl')

library(foreign)
library(readxl)

welfare = read.spss(file = "./csv/Koweps_hpc10_2015_beta1.sav ", 
                    to.data.frame = T)

view(welfare)

welfare = rename(welfare,
                 gender = h10_g3,
                 birth = h10_g4,
                 marriage = h10_g10,
                 religion = h10_g11,
                 income = p1002_8aq1,
                 code_job = h10_eco9,
                 code_region = h10_reg7)
welfare %>%
  select(gender, birth, marriage, religion,
         income, code_job, code_region) -> welfare_copy

view(welfare_copy)

# 성별 
