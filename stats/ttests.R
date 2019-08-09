# ttests.R
# 07/09/19 - ryan pili
#
# script to run bonferroni corrected t.tests for vgcmd

# smileflag. if = 1, include smiles. if = 0, exclude smiles
smileflag = 1;
if(flag == 1){
# vis with smiles
ao_vis = c(79, 69, 76, 110, 34)
av_vis = c(69, 46, 85, 119, 32)
} else if(flag == 0){
# vis without smiles
ao_vis = c(16, 22, 11, 30, 9)
av_vis = c(9, 15, 16, 43, 8)
}

# in-game mechanics
ao_igm = c(1, 0, 3, 1, 2)
av_igm = c(1, 0, 0, 2 ,0)

# verbal BC
ao_verb = c(33, 45)
av_verb = c(70, 60)

ci.mean1 <- function(alpha, m, sd, n) {
  # Computes confidence interval for a population mean
  # Arguments: 
  #   alpha: alpha level for 1-alpha confidence
  #   m:     sample mean
  #   sd:    sample standard deviation
  #   n:     sample size
  # Returns:
  #   estimate of population mean, SE, lower limit and upper limit
  df <- n - 1
  tcrit <- qt(1 - alpha/2, df)
  se <- sd/sqrt(n)
  ll <- m - tcrit*se
  ul <- m + tcrit*se
  out <- t(c(m, se, ll, ul))
  colnames(out) <- c("Estimate", "SE",  "LL", "UL")
  return(out)
}

# bonferroni correction before running t.tests - update as data comes in and more tests are run
alpha = 0.05/2

# run t.tests
t.test(ao_vis, av_vis, paired = T, conf.level = 1 - alpha)
t.test(ao_igm, av_igm, paired = T, conf.level = 1 - alpha)

