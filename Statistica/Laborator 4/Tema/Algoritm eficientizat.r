val <- 1:5
prob <- c(1/3,1/30,2/15,7/30,4/15)
u <- runif(1)


sum = 0
for (i in 1:length(prob)){
  sum = sum + prob[i]
  if (u < sum){
    x = val[i]
    break
  }
}







