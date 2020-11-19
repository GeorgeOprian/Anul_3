#TEMA: Rescrieti functia de mai sus astfel incat sa nu se mai bazeze pe apelul 
#functiei f_respingere


f_respingere_n <- function(n)
{ 
  X <- c()
  K <- c()
  for(i in 1:n) {
    ok <- F
    k <- 0
    while(ok==F)
    {
      y <- runif(1,0.8,1)
      u <- runif(1)
      if(u<=125*y*(1-y)^3) {
        x <- y
        ok <- T
      }
      k <- k+1
    }
    X <- c(X,x)
    K <- c(K,k)
  }
  #vom concatena cu functia rbind()
  return(rbind(X,K))
}
m <- f_respingere_n(10^4)
m[,1:5]
